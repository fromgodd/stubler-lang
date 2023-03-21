import argparse
from lexer import Lexer
from parser import Parser

def main():
    parser = argparse.ArgumentParser(description='Run a .stub file')
    parser.add_argument('file', type=str, help='the .stub file to run')
    args = parser.parse_args()

    # read the contents of the .stub file
    with open(args.file, 'r') as f:
        code = f.read()

    # tokenize the code
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    print(tokens)

    # parse and execute the code
    parser = Parser(tokens)
    parser.parse()
    
if __name__ == '__main__':
    main()
