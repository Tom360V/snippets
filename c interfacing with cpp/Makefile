
HEADER="**********"
SRC_C=c.c
SRC_CPP=cpp.cpp c2cpp.cpp
APP:=app.exe

OBJS:=$(SRC_C:.c=.c.o)
OBJS+=$(SRC_CPP:.cpp=.cpp.o)

all: pre $(APP)
	@echo $(HEADER)
	@echo done

clean:
	@echo $(HEADER)
	@echo Clean
	rm -f $(OBJS)
	rm -f $(APP)
	
.PHONY: clean pre app

pre:
	@echo $(HEADER)
	@echo "PROJECT NAME:" $(APP)
	@echo "OBJECTS:"
	@echo -e  $(foreach dir,$(OBJS), "\r              $(dir)\r\n")

	
$(APP): $(OBJS) 
	@echo $(HEADER)
	@echo "Build APP: $@"
	@echo "Use: $^"
	gcc -Wall $^ -o $@
	
%.c.o : %.c
	@echo $(HEADER)
	@echo "Build C: $< $@"
	gcc -Wall -O0 -c $^ -o $@
	@echo ' '

%.cpp.o : %.cpp
	@echo $(HEADER)
	@echo "Build CPP: $< $@"
	g++ -Wall -O0 -c $^ -o $@
	@echo ' '
