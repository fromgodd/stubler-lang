from lexer import TokenType

class ASTNode:
    pass

class VariableDeclarationNode(ASTNode):
    def __init__(self, variable_name, variable_type):
        self.variable_name = variable_name
        self.variable_type = variable_type

class ReadNode(ASTNode):
    def __init__(self, variable_name):
        self.variable_name = variable_name

class WriteNode(ASTNode):
    def __init__(self, value):
        self.value = value

class BinaryOperationNode(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = -1
        self.advance()

    def advance(self):
        self.current_token_index += 1
        if self.current_token_index < len(self.tokens):
            self.current_token = self.tokens[self.current_token_index]
        else:
            self.current_token = None

    def parse(self):
        self.consume(TokenType.MAIN)
        self.consume(TokenType.DOLLAR)

        program = ProgramNode()

        while self.current_token is not None:
            if self.current_token[0] == TokenType.VAR:
                program.statements.append(self.variable_declaration())
            elif self.current_token[0] == TokenType.MSG:
                program.statements.append(self.write_statement())
            elif self.current_token[0] == TokenType.RS:
                program.statements.append(self.read_statement())
            elif self.current_token[0] in [TokenType.PLUS, TokenType.MINUS, TokenType.MUL, TokenType.DIV]:
                program.statements.append(self.binary_operation())
            else:
                raise Exception(f"Unexpected token: {self.current_token[0]}")

        return program

    def variable_declaration(self):
        self.consume(TokenType.VAR)
        variable_name = self.current_token[1]
        self.consume(TokenType.ID)
        self.consume(TokenType.COLON)
        variable_type = self.current_token[1]
        self.consume(TokenType.TYPE)
        self.consume(TokenType.DOLLAR)
        return VariableDeclarationNode(variable_name, variable_type)

    def write_statement(self):
        self.consume(TokenType.MSG)
        value = self.current_token[1]
        self.consume(TokenType.STRING)
        self.consume(TokenType.DOLLAR)
        return WriteNode(value)

    def read_statement(self):
        self.consume(TokenType.RS)
        variable_name = self.current_token[1]
        self.consume(TokenType.ID)
        self.consume(TokenType.DOLLAR)
        return ReadNode(variable_name)

    def binary_operation(self):
        left = self.current_token[1]
        self.consume(TokenType.ID)
        operator = self.current_token[1]
        self.consume(self.current_token[0])
        right = self.current_token[1]
        self.consume(TokenType.ID)
        self.consume(TokenType.DOLLAR)
        return BinaryOperationNode(left, operator, right)

    def consume(self, expected_token_type):
        if self.current_token[0] == expected_token_type:
            self.advance()
        else:
            raise Exception(f"Expected token type: {expected_token_type}, but got: {self.current_token[0]}")
