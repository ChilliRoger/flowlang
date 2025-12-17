class Interpreter:
    def __init__(self):
        self.env = {}
        self.funcs = {}

    def eval(self, node):
        from flowlang.ast_nodes import *

        if isinstance(node, Block):
            for s in node.statements:
                self.eval(s)

        elif isinstance(node, Number): return node.value
        elif isinstance(node, String): return node.value
        elif isinstance(node, Var): return self.env.get(node.name, 0)

        elif isinstance(node, Assign):
            self.env[node.name] = self.eval(node.value)

        elif isinstance(node, Print):
            print(self.eval(node.value))

        elif isinstance(node, If):
            if self.eval(node.condition):
                self.eval(node.block)

        elif isinstance(node, While):
            while self.eval(node.condition):
                self.eval(node.block)

        elif isinstance(node, Function):
            self.funcs[node.name] = node

        elif isinstance(node, Call):
            fn = self.funcs[node.name]
            local = dict(zip(fn.params, map(self.eval, node.args)))
            old = self.env
            self.env = {**self.env, **local}
            self.eval(fn.block)
            self.env = old
