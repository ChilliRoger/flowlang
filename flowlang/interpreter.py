from flowlang.ast_nodes import *

class ReturnValue(Exception):
    """Exception used to implement return statements"""
    def __init__(self, value):
        self.value = value

class Interpreter:
    def __init__(self):
        self.env = {}
        self.funcs = {}
        self._setup_builtins()
    
    def _setup_builtins(self):
        """Setup built-in functions"""
        self.builtins = {
            'len': lambda args: len(args[0]) if args else 0,
            'type': lambda args: type(args[0]).__name__ if args else 'None',
            'str': lambda args: str(args[0]) if args else '',
            'int': lambda args: int(args[0]) if args else 0,
            'range': lambda args: list(range(*[int(a) for a in args])),
            'input': lambda args: input(args[0] if args else ''),
            'http_get': self._http_get,
            'http_post': self._http_post,
            'read_file': self._read_file,
            'write_file': self._write_file,
        }
    
    def _http_get(self, args):
        """HTTP GET request"""
        try:
            import urllib.request
            import json
            url = args[0] if args else ''
            with urllib.request.urlopen(url) as response:
                data = response.read().decode('utf-8')
                try:
                    return json.loads(data)
                except:
                    return data
        except Exception as e:
            return f"Error: {str(e)}"
    
    def _http_post(self, args):
        """HTTP POST request"""
        try:
            import urllib.request
            import json
            url = args[0] if args else ''
            data = json.dumps(args[1] if len(args) > 1 else {}).encode('utf-8')
            req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
            with urllib.request.urlopen(req) as response:
                resp_data = response.read().decode('utf-8')
                try:
                    return json.loads(resp_data)
                except:
                    return resp_data
        except Exception as e:
            return f"Error: {str(e)}"
    
    def _read_file(self, args):
        """Read file contents"""
        try:
            filename = args[0] if args else ''
            with open(filename, 'r') as f:
                return f.read()
        except Exception as e:
            return f"Error: {str(e)}"
    
    def _write_file(self, args):
        """Write to file"""
        try:
            filename = args[0] if args else ''
            content = args[1] if len(args) > 1 else ''
            with open(filename, 'w') as f:
                f.write(str(content))
            return f"Written to {filename}"
        except Exception as e:
            return f"Error: {str(e)}"

    def eval(self, node):
        if isinstance(node, Block):
            for s in node.statements:
                self.eval(s)

        elif isinstance(node, Number): return node.value
        elif isinstance(node, String): return node.value
        elif isinstance(node, Var): return self.env.get(node.name, 0)

        elif isinstance(node, Assign):
            self.env[node.name] = self.eval(node.value)

        elif isinstance(node, BinOp):
            left = self.eval(node.left)
            right = self.eval(node.right)
            op = node.op
            
            # Arithmetic operators
            if op == "+": return left + right
            elif op == "-": return left - right
            elif op == "*": return left * right
            elif op == "/": return left // right if isinstance(left, int) and isinstance(right, int) else left / right
            
            # Comparison operators
            elif op == "<": return left < right
            elif op == ">": return left > right
            elif op == "<=": return left <= right
            elif op == ">=": return left >= right
            elif op == "==": return left == right
            elif op == "!=": return left != right
            
            else:
                raise RuntimeError(f"Unknown operator: {op}")

        elif isinstance(node, Print):
            print(self.eval(node.value))

        elif isinstance(node, Return):
            raise ReturnValue(self.eval(node.value))

        elif isinstance(node, If):
            if self.eval(node.condition):
                self.eval(node.block)

        elif isinstance(node, While):
            while self.eval(node.condition):
                self.eval(node.block)

        elif isinstance(node, Function):
            self.funcs[node.name] = node

        elif isinstance(node, Call):
            # Check if it's a built-in function
            if node.name in self.builtins:
                args = [self.eval(arg) for arg in node.args]
                return self.builtins[node.name](args)
            
            # User-defined function
            if node.name not in self.funcs:
                raise RuntimeError(f"Undefined function: {node.name}")
            
            fn = self.funcs[node.name]
            local = dict(zip(fn.params, map(self.eval, node.args)))
            old = self.env
            self.env = {**self.env, **local}
            
            try:
                self.eval(fn.block)
                return None  # Function without explicit return
            except ReturnValue as ret:
                return ret.value
            finally:
                self.env = old
