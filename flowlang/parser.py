from flowlang.ast_nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def eat(self, t=None):
        tok = self.tokens[self.pos]
        if t and tok[0] != t:
            raise SyntaxError(tok)
        self.pos += 1
        return tok

    def parse(self):
        stmts = []
        while self.pos < len(self.tokens):
            stmts.append(self.statement())
        return Block(stmts)

    def statement(self):
        t = self.tokens[self.pos][0]

        if t == "LET":
            self.eat("LET")
            name = self.eat("IDENT")[1]
            self.eat("OP")
            return Assign(name, self.expr())

        if t == "PRINT":
            self.eat("PRINT")
            return Print(self.expr())

        if t == "IF":
            self.eat("IF")
            cond = self.expr()
            return If(cond, self.block())

        if t == "WHILE":
            self.eat("WHILE")
            cond = self.expr()
            return While(cond, self.block())

        if t == "FUNC":
            self.eat("FUNC")
            name = self.eat("IDENT")[1]
            self.eat("LPAREN")
            params = []
            while self.tokens[self.pos][0] != "RPAREN":
                params.append(self.eat("IDENT")[1])
                if self.tokens[self.pos][0] == "COMMA":
                    self.eat("COMMA")
            self.eat("RPAREN")
            return Function(name, params, self.block())

        return self.expr()

    def block(self):
        self.eat("LBRACE")
        stmts = []
        while self.tokens[self.pos][0] != "RBRACE":
            stmts.append(self.statement())
        self.eat("RBRACE")
        return Block(stmts)

    def expr(self):
        tok = self.eat()
        if tok[0] == "NUMBER": return Number(int(tok[1]))
        if tok[0] == "STRING": return String(tok[1][1:-1])
        if tok[0] == "IDENT": return Var(tok[1])
