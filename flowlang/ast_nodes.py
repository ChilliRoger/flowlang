class Number: 
    def __init__(self, value): self.value = value

class String: 
    def __init__(self, value): self.value = value

class Var: 
    def __init__(self, name): self.name = name

class BinOp:
    def __init__(self, left, op, right):
        self.left, self.op, self.right = left, op, right

class Assign:
    def __init__(self, name, value):
        self.name, self.value = name, value

class Print:
    def __init__(self, value): self.value = value

class Block:
    def __init__(self, statements): self.statements = statements

class If:
    def __init__(self, condition, block):
        self.condition, self.block = condition, block

class While:
    def __init__(self, condition, block):
        self.condition, self.block = condition, block

class Function:
    def __init__(self, name, params, block):
        self.name, self.params, self.block = name, params, block

class Call:
    def __init__(self, name, args):
        self.name, self.args = name, args

class Return:
    def __init__(self, value):
        self.value = value
