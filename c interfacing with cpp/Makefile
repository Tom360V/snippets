
HEADER="**********"
SRC_C=c.c
SRC_CPP=cpp.cpp c2cpp.cpp
APP:=app.exe

OBJSC:=$(SRC_C:.c=.o)
OBJSCPP=$(SRC_CPP:.cpp=.o)

all: pre $(APP)
	@echo $(HEADER)
	@echo done

clean:
	@echo $(HEADER)
	@echo Clean
	rm -f $(OBJSC)
	rm -f $(OBJSCPP)
	rm -f $(APP)
	
.PHONY: clean pre app

pre:
	@echo $(HEADER)
	@echo C: $(OBJSC)
	@echo CPP: $(OBJSCPP)
	
$(APP): $(OBJSC) $(OBJSCPP)
	@echo $(HEADER)
	@echo "Build APP: $@"
	@echo "Use: $^"
	gcc -Wall $^ -o $@
	
%.o : %.c
	@echo $(HEADER)
	@echo "Build C: $< $@"
	gcc -Wall -O0 -c $^ -o $@
	@echo ' '

%.o : %.cpp
	@echo $(HEADER)
	@echo "Build CPP: $< $@"
	g++ -Wall -O0 -c $^ -o $@
	@echo ' '
