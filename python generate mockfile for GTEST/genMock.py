#!/usr/bin/env python

from os.path import basename

import os
import sys
import re
import pprint

#DEBUG = True
DEBUG = False

def log(s):
    if DEBUG:
        print s


vartypes = ["void", "bool", "int", "uint", "tmErrorCode_t", "err_t",
            "int8_t",   "int16_t",  "int32_t",
            "uint8_t",  "uint16_t", "uint32_t",
            "u8_t",     "u16_t",    "u32_t"]

functionkeywords = ["static", "extern", "inline"]
nonefunctionkeywords = ["struct", "typedef", "{", "}", "=", "."]

def deleteFile(filename):
    if os.path.exists(filename):
        os.remove(filename)
            
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

    if(False):
        #Old solution
        #params = re.findall(r"[a-zA-Z0-9_]+[\* ]+([a-zA-Z0-9_]*[\,]?)", parm)
        params = re.findall(r"[a-zA-Z0-9_]+[\* ]+([a-zA-Z0-9_ ]*[\,\)])", parm)
        params = ' '.join(params)
        params = params.replace(')','')
    else:
        #New solution, better parameter parsing"
        params=[]
        parm = re.sub('[()]', '', parm)
        parm = parm.replace("void", "")
        if(parm!=""):
            parmList = parm.split(",")
            for p in parmList:
                p = p.replace('*','').split(" ")
                params.append(p[-1])
        params = ", ".join(params)
    
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
    blockFound=0
    for row in content:
        row = row.strip()   #remove leading/trailing spaces
        
        # Handle block comments AND braces
        if( "/*" in row or
            "{"  in row ):
            blockFound=True
        
        if( "*/" in row or
            "}"  in row ):
            blockFound=False
            continue;

        if(blockFound==True):
            continue;


        #first check for comments and defines
        if( row.startswith("*")  or
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
    outputpath="./"

    if len(sys.argv) <= 1:
        print "Usage: python "+ basename(sys.argv[0]) + " [filename] [output path] [mockname]"
        print "This script will generate mock files based on existing headerfiles"
        print
        print "  [filename]                 : header file which will be used to generate the mock file"
        print "  [output path] (optional)   : output path where the generated files will be placed"
        print "  [mockname]    (optional)   : override the generated mockname with your own mockname"
        sys.exit()

    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        print("** Make mock for: " + filename)
        log(filename)
        if(os.path.isfile(filename)):
            log("is a file")
        else:
            print "is NOT a file"
            sys.exit()

    if len(sys.argv) >= 3:
        outputpath=sys.argv[2]
        if not outputpath.endswith('/'):
            outputpath = outputpath + '/'
        log("** write mock files to: " + outputpath)

    mockname = os.path.splitext(basename(filename))[0]
    if len(sys.argv) >= 4:
        mockname=sys.argv[3]
        log("** mockname: " + mockname)


    try:
        funcProtoList = searchForFunctionPrototypes(filename)
        lastFunction = "none"
        for f in funcProtoList:
            log("function prototype: " + f)
            lastFunction = f
           #reParse = re.compile(r'(?P<rtrn>\b\w+[ ]?[*]?\b)[\* ]*(?P<func>\b\w+\b)[\s]*(?P<parm>\([\)\S\s\)\*]*);')
            reParse = re.compile(r'(?P<rtrn>\b\w*[ ]*\w+[ ]*[*]?\b)[\* ]*(?P<func>\b\w+\b)[\s]*(?P<parm>\([\)\S\s\)\*]*);')
            m = reParse.search(f)
            if(m==None):
                print "WARNING, Could not parse row: " + f
                continue
            
            #print "Found: " + m.group('rtrn') + " " + m.group('func') + " " + m.group('parm') +" \n"
            rval.append(m.group('rtrn'))
            func.append(m.group('func'))
            parm.append(m.group('parm'))
    except:
            print "ERROR, failed to parse the headerfile: ", sys.exc_info()[0], " Parsing function: ", lastFunction


    try:
        log("***** CREATE HEADER FILE ******")
        f_out = open(outputpath+"MOCK_"+mockname+".h", 'w+')
        printHeader_H(mockname)

        for i in range(0,len(rval)):
            printProto(rval[i], func[i], parm[i])

        printPart2(mockname)

        for i in range(0,len(rval)):
            printMockProto(rval[i], func[i], parm[i])

        printFooter_H(mockname)
        
        f_out.close()
    except:
        print "ERROR, failed to create mock-headerfile: ", sys.exc_info()[0]


    try:
        log("***** CREATE BODY FILE ******")
        f_out = open(outputpath+"MOCK_"+mockname+".cpp", 'w+')
        printHeader_CPP(mockname)
        for i in range(0,len(rval)):
            printFuncBody("mock_"+mockname ,rval[i], func[i], parm[i])

        f_out.close()
    except:
        print "ERROR, failed to create mock-bodyfile ", sys.exc_info()[0]
        deleteFile(outputpath+"MOCK_"+filename+".cpp")
        deleteFile(outputpath+"MOCK_"+filename+".h")
        sys.exit(-1)
    sys.exit(0)
