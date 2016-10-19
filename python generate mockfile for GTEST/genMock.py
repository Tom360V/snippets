#!/usr/bin/env python

from os.path import basename
import os
import sys
import re

DEBUG = True
#DEBUG = False

def log(s):
    if DEBUG:
        print s


vartypes = ["void", "bool", "int", "uint", "tmErrorCode_t", "err_t"
            , "u8_t", "u16_t", "u32_t"]

functionkeywords = ["static", "extern", "inline"]
nonefunctionkeywords = ["struct", "typedef", "{", "}", "=", "."]
            
def add(data):
    log(data)
    f_out.write(data+'\r')

def printHeader_CPP( name ):
    add("#include \"MOCK_" + name + ".h\"")
    add("")
    add("static MOCK_" + name +"* mock_" + name + " = NULL;" )
    add("")
    add("MOCK_" + name +"::MOCK_" + name +"()");
    add("{");
    add("    if(mock_" + name +" != NULL)");
    add("    {");
    add("        throw std::invalid_argument(\"Mock already exists\");");
    add("    }");
    add("    mock_" + name +" = this;");
    add("}");
    add("");
    add("MOCK_" + name +"::~MOCK_" + name +"()");
    add("{");
    add("    mock_" + name +" = NULL;");
    add("}");
    add("");

def printFuncBody( mockname, rval, func, parm ):
    add(rval + " " + func + parm)
    add("{")
    r = "return "
    if(rval == "void"):
        r=""

#    params = re.findall(r"[a-zA-Z0-9_]+[\* ]+([a-zA-Z0-9_]*[\,]?)", parm)
    params = re.findall(r"[a-zA-Z0-9_]+[\* ]+([a-zA-Z0-9_ ]*[\,\)])", parm)
    params = ' '.join(params)
    params = params.replace(')','')
    
    add("    " + r + mockname + "->" + func + "(" + params + ");")
    add("}")
    add("")


def printHeader_H( name ):
    add("#include \"" + name + ".h\"")
    add("#include \"gmock/gmock.h\"")
    add("")

    add("class " + name)
    add("{")
    add("public:")

def printFooter_H( name ):
    add("};")
    add("")
#    add("extern MOCK_" + name + "* mock_" + name + ";")


def printPart2( name ):
    add("};")
    add("")
    add("class MOCK_" + name + " : public " + name)
    add("{")
    add("public:")
    add("    MOCK_" + name + "();")
    add("    ~MOCK_" + name + "();")
    add("")

def printProto( rval, func, parm ):
    add("    virtual " + rval + " " + func + parm + " = 0;")

def printMockProto( rval, func, parm ):
    cnt = parm.count(',') + 1
    if( cnt == 1 and
        parm.count(' ') == 0 ):
        cnt = 0;
    add("    MOCK_METHOD" + str(cnt) +"(" + func + ", " + rval + parm + ");")


def searchForFunctionPrototypes( fname ):
    with open(fname) as f:
        content = f.readlines()
    functionProtos = []
    protoStr = ""
    for row in content:
        row = row.strip()   #remove leading/trailing spaces
        
        #first check for comments and defines
        if( row.startswith("/*") or
            row.startswith("*")  or
            row.startswith("#")  or
            row.startswith("//") ):
            continue
        
        if any(x in row for x in nonefunctionkeywords):
            continue

        #replace functionkeywords, is this necessary???
        for k in functionkeywords:
            row = row.replace(k,'')
       
        if row.find(";")>=0:
            protoStr += str(row)

            #remove overhead
            protoStr = protoStr.rstrip('\n')        #remove end of line
            protoStr = protoStr.replace("\t"," ")   #replace tabs by spaces
            protoStr = re.sub(' +', ' ', protoStr)  #remove double spaces
            protoStr = protoStr.strip()             #remove leading/trailing spaces

            if( protoStr.find('(')>=0 and
                protoStr.find(')')>=0 and
                protoStr.find(';')>=0 ):
                functionProtos.append(protoStr)
            protoStr = ""
        elif row.find("(")>=0:
            protoStr = str(row)
        else:
            protoStr += str(row)
            
                #check if row can contain a function prototype
    return functionProtos
    
   
if __name__ == "__main__":
    funcProtoList=[]
    rval=[]
    func=[]
    parm=[]
    cnt=0;
    if len(sys.argv) < 2:
        print "Not enough parameters, correct usage:"
        print ">> python "+ basename(sys.argv[0]) + " [filename.h]"
        sys.exit()
    filename = sys.argv[1]
    log(filename)
    if(os.path.isfile(filename)):
        log("is a file")
        funcProtoList = searchForFunctionPrototypes(filename)
    else:
        print "is NOT a file"
        sys.exit()

    mockname = os.path.splitext(basename(filename))[0]

    for f in funcProtoList:
        log("function prototype: " + f)
#       reParse = re.compile(r'(?P<rtrn>\b\w+\b)[ ]*(?P<func>\b\w+\b)[\s]*(?P<parm>\([\)\S\s\)\*]*);')
        reParse = re.compile(r'(?P<rtrn>\b\w+\b)[\* ]*(?P<func>\b\w+\b)[\s]*(?P<parm>\([\)\S\s\)\*]*);')

        m = reParse.search(f)
        rval.append(m.group('rtrn'))
        func.append(m.group('func'))
        parm.append(m.group('parm'))

    print
    print "***** CREATE HEADER FILE ******"
    f_out = open("MOCK_"+mockname+".h", 'w+')
    printHeader_H(mockname)

    for i in range(0,len(rval)):
        printProto(rval[i], func[i], parm[i])

    printPart2(mockname)

    for i in range(0,len(rval)):
        printMockProto(rval[i], func[i], parm[i])

    printFooter_H(mockname)
    
    f_out.close()
    
  
    print "***** CREATE BODY FILE ******"
    f_out = open("MOCK_"+mockname+".cpp", 'w+')
    printHeader_CPP(mockname)
    for i in range(0,len(rval)):
        printFuncBody("mock_"+mockname ,rval[i], func[i], parm[i])

    f_out.close()
