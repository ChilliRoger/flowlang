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

        if t == "RETURN":
            self.eat("RETURN")
            return Return(self.expr())

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

    def peek(self):
        """Look at current token without consuming it"""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def expr(self):
        """Parse expression with operator precedence"""
        return self.comparison()

    def comparison(self):
        """Parse comparison operators: <, >, <=, >=, ==, !="""
        left = self.addition()
        
        while self.peek() and self.peek()[0] == "OP" and self.peek()[1] in ["<", ">", "=", "!"]:
            op_tok = self.eat("OP")
            # Handle == and !=
            if op_tok[1] in ["=", "!"] and self.peek() and self.peek()[0] == "OP" and self.peek()[1] == "=":
                self.eat("OP")
                op = op_tok[1] + "="
            else:
                op = op_tok[1]
            right = self.addition()
            left = BinOp(left, op, right)
        
        return left

    def addition(self):
        """Parse addition and subtraction: +, -"""
        left = self.multiplication()
        
        while self.peek() and self.peek()[0] == "OP" and self.peek()[1] in ["+", "-"]:
            op = self.eat("OP")[1]
            right = self.multiplication()
            left = BinOp(left, op, right)
        
        return left

    def multiplication(self):
        """Parse multiplication and division: *, /"""
        left = self.primary()
        
        while self.peek() and self.peek()[0] == "OP" and self.peek()[1] in ["*", "/"]:
            op = self.eat("OP")[1]
            right = self.primary()
            left = BinOp(left, op, right)
        
        return left

    def primary(self):
        """Parse primary expressions: numbers, strings, variables, function calls, parentheses"""
        tok = self.peek()
        
        if not tok:
            raise SyntaxError("Unexpected end of input")
        
        # Numbers
        if tok[0] == "NUMBER":
            self.eat("NUMBER")
            return Number(int(tok[1]))
        
        # Strings
        if tok[0] == "STRING":
            self.eat("STRING")
            # Handle escape sequences
            string_value = tok[1][1:-1]  # Remove quotes
            string_value = string_value.replace('\\n', '\n')
            string_value = string_value.replace('\\t', '\t')
            string_value = string_value.replace('\\r', '\r')
            string_value = string_value.replace('\\\\', '\\')
            return String(string_value)
        
        # Parenthesized expressions
        if tok[0] == "LPAREN":
            self.eat("LPAREN")
            expr = self.expr()
            self.eat("RPAREN")
            return expr
        
        # Identifiers (variables or function calls)
        if tok[0] == "IDENT":
            name = self.eat("IDENT")[1]
            
            # Check if it's a function call
            if self.peek() and self.peek()[0] == "LPAREN":
                self.eat("LPAREN")
                args = []
                
                # Parse arguments
                if self.peek() and self.peek()[0] != "RPAREN":
                    args.append(self.expr())
                    while self.peek() and self.peek()[0] == "COMMA":
                        self.eat("COMMA")
                        args.append(self.expr())
                
                self.eat("RPAREN")
                return Call(name, args)
            else:
                return Var(name)
        
        raise SyntaxError(f"Unexpected token: {tok}")
