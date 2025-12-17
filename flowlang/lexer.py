import re

TOKENS = [
    ("NUMBER", r"\d+"),
    ("STRING", r'"[^"]*"'),
    ("LET", r"let"),
    ("FUNC", r"func"),
    ("IF", r"if"),
    ("WHILE", r"while"),
    ("PRINT", r"print"),
    ("IDENT", r"[a-zA-Z_]\w*"),
    ("OP", r"[+\-*/><=]"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("LBRACE", r"\{"),
    ("RBRACE", r"\}"),
    ("COMMA", r","),
    ("SKIP", r"[ \t\n]+"),
]

class Lexer:
    def __init__(self, code):
        self.tokens = []
        while code:
            for t, r in TOKENS:
                m = re.match(r, code)
                if m:
                    if t != "SKIP":
                        self.tokens.append((t, m.group(0)))
                    code = code[m.end():]
                    break
            else:
                raise SyntaxError(code[0])
