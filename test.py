from lexer import Lexer
from parser import Parser
from ast import *

def main():
    with open("calculator.stub", "r") as f:
        code = f.read()
    lexer = Lexer(code)
    parser = Parser(lexer)
    program = parser.parse()
    program.run()

if __name__ == "__main__":
    main()
