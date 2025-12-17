import sys
from flowlang.lexer import Lexer
from flowlang.parser import Parser
from flowlang.interpreter import Interpreter

def main():
    if len(sys.argv) < 3:
        print("Usage: flow run file.flow")
        return

    with open(sys.argv[2]) as f:
        code = f.read()

    tokens = Lexer(code).tokens
    ast = Parser(tokens).parse()
    Interpreter().eval(ast)
