import time
import os
logo = """

 _____   _____     _             _       _ 
/  __ \ |_   _|   | |           (_)     | |
| /  \/   | |_   _| |_ ___  _ __ _  __ _| |
| |       | | | | | __/ _ \| '__| |/ _` | |
| \__/\   | | |_| | || (_) | |  | | (_| | |
 \____/   \_/\__,_|\__\___/|_|  |_|\__,_|_|
                                           
 """                                          
info = """
by hanicraft
instagram : mohamadhanijanaty85
github : hanicraft
aparat : hanicraft2
reddit : u/mhjhacker1

"""

menu = """
1 - basic info about c
2 - variables
3 - operators
4 - if/else
5 - while
6 - functions
7 - stdio functions (default library)
8 - arrays
9 - python to c converter (got python code. convert it using this tool)
10 - how to use a c compiler
11 - exit
"""
basic = """
C is a general-purpose computer programming language. It was created in the 1970s by Dennis Ritchie, and remains very widely used and influential. By design, C's features cleanly reflect the capabilities of the targeted CPUs. It has found lasting use in operating systems, device drivers, protocol stacks, though decreasingly[7] for application software. C is commonly used on computer architectures that range from the largest supercomputers to the smallest microcontrollers and embedded systems.

"""
vars = """
variables in c are

int - Integer variable used to store whole numbers.

float - Floating-point variable used to store decimal numbers.

double - Double-precision floating-point variable used to store decimal numbers with more precision than a float.

char - Character variable used to store a single character.

bool - Boolean variable used to store true/false values.

void - Void variable used to represent the absence of type.
"""

operator = """
Operators in C are symbols or keywords used to perform operations on operands, which can be variables, constants, or expressions. There are several types of operators in C, including arithmetic, relational, logical, bitwise, and assignment operators.

Arithmetic operators: Used to perform mathematical calculations. They include:

+ (addition)
- (subtraction)
* (multiplication)
/ (division)
% (modulus, returns the remainder of a division)
Assignment operators: Used to assign a value to a variable. They include:

= (simple assignment)
+= (add and assign)
-= (subtract and assign)
*= (multiply and assign)
/= (divide and assign)
%= (modulus and assign)
Comparison operators: Used to compare values. They include:

== (equal to)
!= (not equal to)
< (less than)
> (greater than)
<= (less than or equal to)
>= (greater than or equal to)

"""
ifelse = """
The if-else statement is a fundamental control flow statement in C programming. It is used to execute a certain block of code based on a condition. Here's a brief explanation of how if-else works in C:

The if statement begins with the keyword "if", followed by a condition in parentheses. If the condition is true, the block of code inside the if statement is executed. If the condition is false, the block of code inside the if statement is skipped.

The else statement is optional and is used in conjunction with the if statement. If the condition in the if statement is false, the block of code inside the else statement is executed.

heres a code example

__________________________
if (condition) {
   // block of code to be executed if the condition is true
}
else {
   // block of code to be executed if the condition is false
}
__________________________
"""
whiles = """
The while loop is another fundamental control flow statement in C programming. It allows you to execute a block of code repeatedly while a certain condition is true.

The while loop begins with the keyword "while", followed by a condition in parentheses. The block of code inside the while loop is executed repeatedly as long as the condition is true. If the condition is false, the block of code is skipped, and the program continues with the next statement after the while loop.

heres a code example
__________________________
while (condition) {
   // block of code to be executed repeatedly while the condition is true
}
__________________________
"""
funcs = """
In C programming, a function is a block of code that performs a specific task. Functions are used to modularize programs and make them easier to read, understand, and maintain. They can take input parameters and return output values, and they can be called from other parts of the program. Functions can be defined either in the same file or in separate files and can be declared in header files.

heres a code example
__________________________
void main(){
    // block of code to be executed
}
__________________________

"""
stdio = """
Here are some of the most commonly used basic stdio c functions and what they do:

printf() - Used for outputting formatted text to the console or other output stream.

scanf() - Used for reading input from the console or other input stream.

fopen() - Used for opening a file for reading, writing, or appending.

fclose() - Used for closing an open file.

fprintf() - Used for outputting formatted text to a file.

fscanf() - Used for reading input from a file.

putchar() - Used for outputting a single character to the console or other output stream.

getchar() - Used for reading a single character from the console or other input stream.

rewind() - Used for resetting the file pointer to the beginning of an open file.

fseek() - Used for moving the file pointer to a specific position within an open file.

ftell() - Used for getting the current position of the file pointer within an open file.

feof() - Used for checking whether the end of an open file has been reached.

note : this is not all of the functions. we removed some unsafe ones and things that you should avoid
"""

arrays = """

array is a collection of elements of the same data type, stored in contiguous memory locations. heres how you can use it
__________________________
#include <stdio.h>

int main() {
   int nums[5] = {1, 2, 3, 4, 5};

   return 0;
}
__________________________

and heres how you can call a data from an array or modify it
__________________________
// to call it
nums[0]
nums[1]
nums[2]
// to modify it
nums[1] = 10;
__________________________



"""

howtousecompiler = """
Compile your code: Open a terminal or command prompt and navigate to the directory where your code file is saved. To compile your code, enter the following command:

__________________________
gcc -o output_file_name input_file_name
__________________________

Replace output_file_name with the name you want to give to the compiled output file and input_file_name with the name of the file containing your code.

Run your program: Once the compilation is successful, you can run your program by entering the following command in the terminal:

__________________________
./output_file_name
__________________________

This will execute your compiled program, and you should see the output on the terminal.

"""

def txtprint(txt, speed, color=None):
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'purple': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m'
    }
    if color in colors:
        txt = colors[color] + txt + colors['reset']
    for char in txt:
        print(char, end='', flush=True)
        time.sleep(speed)

def menulogic():
    id = input(txtprint("\n what would you like to learn \n", 0.1))
    if id == "1":
        txtprint(basic, 0.09, 'yellow')
        menulogic()
    elif id == "2":
        txtprint(vars, 0.09, 'yellow')
        menulogic()
    elif id == "3":
        txtprint(operator, 0.09, 'yellow')
        menulogic()
    elif id == "4":
        txtprint(ifelse, 0.09, 'yellow')
        menulogic()
    elif id == "5":
        txtprint(whiles, 0.09, 'yellow')
        menulogic()
    elif id == "6":
        txtprint(funcs, 0.09, 'yellow')
        menulogic()
    elif id == "7":
        txtprint(stdio, 0.09, 'yellow')
        menulogic()
    elif id == "8":
        txtprint(arrays, 0.09, 'yellow')
        menulogic()
    elif id == "9":
        os.system("python PythonToCConverter.py")
        menulogic()
    elif id == "10":
        txtprint(howtousecompiler, 0.09, 'yellow')
        menulogic()
    elif id == "11":
        txtprint("Good Bye", 0.09, 'yellow')
        os.system(quit)
    else:
        print("invalid number")
        menulogic()
        
        



print(logo)
print(info)
txtprint(menu, 0.1, 'blue')
menulogic()
