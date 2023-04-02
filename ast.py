class ASTNode:
    pass


class ProgramNode(ASTNode):
    def __init__(self, statements):
        self.statements = statements


class MsgNode(ASTNode):
    def __init__(self, message):
        self.message = message


class ReadlineNode(ASTNode):
    def __init__(self, var):
        self.var = var


class AssignmentNode(ASTNode):
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr


class BinaryOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class MemoryNode(ASTNode):
    def __init__(self, var):
        self.var = var


class PauseNode(ASTNode):
    pass


class IntNode(ASTNode):
    def __init__(self, value):
        self.value = value


class FloatNode(ASTNode):
    def __init__(self, value):
        self.value = value
        
class ReadlineNode(ASTNode):
    def __init__(self, var, prompt):
        self.var = var
        self.prompt = prompt