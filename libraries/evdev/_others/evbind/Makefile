objects = main.o err.o

CFLAGS = -g -Wall -Wextra -Werror
CFLAGS_ALL = $(CFLAGS) -std=c99

LDFLAGS =
LDFLAGS_ALL = $(LDFLAGS) 

CPPFLAGS =
CPPFLAGS_ALL = $(CPPFLAGS)

.PHONY : all
all : evbind

%.o : %.c
	$(CC) $(CPPFLAGS_ALL) $(CFLAGS_ALL) -o $@ -c $<

evbind : $(objects)
	$(CC) $(LDFLAGS_ALL) $(CFLAGS_ALL) -o $@ $^ -ludev

.PHONY : clean
clean :
	rm -rf $(objects)
	rm -rf evbind
