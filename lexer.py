import re

# Token definitions
TOKENS = [
    ('M\$', 'MAIN'),
    ('@int', 'INT_TYPE'),
    ('MSG', 'PRINT'),
    ('RS', 'READ'),
    ('MEM', 'MEM_STORE'),
    ('\+', 'PLUS'),
    ('=', 'EQUALS'),
    ('i@[\+|\-]', 'MEM_OP'),
    ('\d+', 'NUM'),
    ('\".*\"', 'STRING'),
    ('\n', 'NEWLINE'),
    ('\s+', 'SPACE'),
    ('[a-zA-Z_][a-zA-Z0-9_]*', 'ID'),
    ('.', 'UNKNOWN'),
]

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.current_char_index = 0
        self.current_char = self.source_code[self.current_char_index]

    def advance(self):
        self.current_char_index += 1
        if self.current_char_index >= len(self.source_code):
            self.current_char = None
        else:
            self.current_char = self.source_code[self.current_char_index]

    def consume_whitespace(self):
        while self.current_char != None and self.current_char.isspace():
            self.advance()

    def tokenize_integer_literal(self):
        result = ""
        while self.current_char != None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return ("INT", int(result))

    def tokenize_identifier(self):
        result = ""
        while self.current_char != None and self.current_char.isalpha():
            result += self.current_char
            self.advance()

        # Check if the identifier is a keyword
        if result == "M$":
            return ("M$", None)
        elif result == "MSG":
            return ("MSG", None)
        elif result == "p":
            return ("PAUSE", None)
        elif result == "RS":
            return ("RS", None)
        elif result == "MEM":
            return ("MEM", None)
        elif result == "int":
            return ("INT_DECLARATION", None)
        else:
            return ("IDENTIFIER", result)

    def tokenize_string_literal(self):
        self.advance()  # consume the opening quote
        result = ""
        while self.current_char != None and self.current_char != "\"":
            result += self.current_char
            self.advance()
        self.advance()  # consume the closing quote
        return ("STRING", result)

    def tokenize_operator(self):
        if self.current_char == "+":
            self.advance()
            return ("PLUS", None)
        elif self.current_char == "-":
            self.advance()
            return ("MINUS", None)
        else:
            self.error(f"Invalid operator: {self.current_char}")

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def tokenize(self):
        tokens = []
        while self.pos < len(self.text):
            if self.text[self.pos:self.pos+2] == "M$":
                tokens.append(("MAIN", "M$"))
                self.pos += 2
            elif self.text[self.pos:self.pos+4] == "MSG ":
                msg = self.text[self.pos+4:].split("\n", 1)[0]
                tokens.append(("PRINT", msg))
                self.pos += len(msg) + 5
            elif self.text[self.pos:self.pos+4] == "RS a":
                tokens.append(("READ_A", ""))
                self.pos += 4
            elif self.text[self.pos:self.pos+4] == "RS b":
                tokens.append(("READ_B", ""))
                self.pos += 4
            elif self.text[self.pos:self.pos+4] == "RS c":
                tokens.append(("READ_C", ""))
                self.pos += 4
            elif self.text[self.pos:self.pos+2] == "a=":
                val = self.text[self.pos+2:].split("\n", 1)[0]
                tokens.append(("ASSIGN_A", val))
                self.pos += len(val) + 3
            elif self.text[self.pos:self.pos+2] == "b=":
                val = self.text[self.pos+2:].split("\n", 1)[0]
                tokens.append(("ASSIGN_B", val))
                self.pos += len(val) + 3
            elif self.text[self.pos:self.pos+2] == "c=":
                val = self.text[self.pos+2:].split("\n", 1)[0]
                tokens.append(("ASSIGN_C", val))
                self.pos += len(val) + 3
            elif self.text[self.pos:self.pos+3] == "a+b":
                tokens.append(("ADD", ""))
                self.pos += 3
            elif self.text[self.pos:self.pos+4] == "MEM ":
                var = self.text[self.pos+4:].split("\n", 1)[0]
                tokens.append(("MEMORY", var))
                self.pos += len(var) + 5
            elif self.text[self.pos:self.pos+2] == "p\n":
                tokens.append(("PAUSE", ""))
                self.pos += 2
            else:
                self.pos += 1
        return tokens


    def error(self, message):
        raise Exception(message)
