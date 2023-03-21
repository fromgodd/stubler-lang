# Stubler

Assembly-like programming language that initially was written in Pascal when I was 12 y.o :) Now rewritten in Python

## Examples

Here is simple "Hello, World!"
```
M$
MSG "Hello, World!"
p
```

M$ - is header function that will indicate this is main program <br>
MSG means print something in console <br>
and P is pause in console (interruption)


Second example is calculator
```
M$
@int a
@int b
@int c
MSG "Enter A"
RS a
MSG "Enter B"
RS b
c = a + b
MEM c i@+
MSG c
```
Here is M$ - main program <br>
@int means integer (we define @int to a,b,c) <br>
RS means read line <br>
MEM means memory. MEM c i@+ means to put c into memory. Put function is i@+
