# FlowLang

A lightweight interpreted programming language designed for workflow automation, data processing, and API orchestration.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Language Specification](#language-specification)
- [Built-in Functions](#built-in-functions)
- [Usage Examples](#usage-examples)
- [API Reference](#api-reference)
- [Use Cases](#use-cases)
- [Integration](#integration)
- [Contributing](#contributing)
- [License](#license)

## Overview

FlowLang is a domain-specific programming language built to address the complexity of workflow automation and API orchestration. It provides a clean, minimal syntax that prioritizes readability and ease of use while maintaining powerful capabilities for data processing tasks.

### Design Philosophy

- **Simplicity First**: Minimal syntax that's easy to learn and read
- **Zero Dependencies**: Built entirely on Python's standard library
- **Practical**: Focused on real-world automation tasks
- **Readable**: Code that serves as its own documentation

### Key Features

- Native HTTP request capabilities (`http_get`, `http_post`)
- Built-in file I/O operations
- First-class functions with return values
- Control flow structures (if, while)
- Rich set of built-in utility functions
- Automatic JSON parsing for API responses
- String escape sequence support

## Installation

### From PyPI (Recommended)

```bash
pip install flowlang-script
```

### From Source

```bash
git clone https://github.com/ChilliRoger/flowlang.git
cd flowlang
pip install -e .
```

### Verify Installation

```bash
flow run --help
```

## Quick Start

### Hello World

Create a file `hello.flow`:

```flow
print "Hello, World!"
```

Run it:

```bash
flow run hello.flow
```

### Basic Operations

```flow
let x = 10
let y = 20
let sum = x + y
print sum
```

### HTTP Request Example

```flow
let response = http_get("https://api.github.com")
print response
```

## Language Specification

### Variables

Variables are declared using the `let` keyword and are dynamically typed.

```flow
let name = "FlowLang-Script"
let version = 1
let pi = 3.14
```

### Data Types

- **Integer**: Whole numbers (`42`, `-10`)
- **String**: Text enclosed in double quotes (`"hello"`)
- **List**: Returned by built-in functions like `range()`
- **Dictionary**: Returned by JSON parsing in HTTP responses

### Operators

#### Arithmetic Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `5 + 3` returns `8` |
| `-` | Subtraction | `10 - 4` returns `6` |
| `*` | Multiplication | `3 * 4` returns `12` |
| `/` | Division | `15 / 3` returns `5` |

#### Comparison Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `<` | Less than | `5 < 10` returns `true` |
| `>` | Greater than | `10 > 5` returns `true` |
| `<=` | Less than or equal | `5 <= 5` returns `true` |
| `>=` | Greater than or equal | `10 >= 5` returns `true` |
| `==` | Equal to | `5 == 5` returns `true` |
| `!=` | Not equal to | `5 != 3` returns `true` |

### Control Flow

#### If Statements

```flow
let age = 18
if age >= 18 {
  print "Adult"
}
```

#### While Loops

```flow
let count = 5
while count > 0 {
  print count
  let count = count - 1
}
```

### Functions

Functions are defined using the `func` keyword and support parameters and return values.

```flow
func add(a, b) {
  return a + b
}

let result = add(10, 20)
print result
```

#### Function Scope

Functions have their own local scope. Variables passed as arguments are local to the function.

```flow
func increment(x) {
  let x = x + 1
  return x
}

let value = 5
let newValue = increment(value)
print newValue  # Prints 6
print value     # Prints 5 (unchanged)
```

### Comments

FlowLang currently does not support inline comments. Use descriptive variable and function names for self-documenting code.

## Built-in Functions

### I/O Functions

#### `print(value)`

Outputs a value to the console.

```flow
print "Hello"
print 42
```

#### `input(prompt)`

Reads user input from the console.

```flow
let name = input("Enter your name: ")
print name
```

### Type Conversion Functions

#### `str(value)`

Converts a value to a string.

```flow
let num = 42
let text = str(num)
```

#### `int(value)`

Converts a value to an integer.

```flow
let text = "123"
let num = int(text)
```

#### `type(value)`

Returns the type name of a value as a string.

```flow
print type(42)        # Prints: int
print type("hello")   # Prints: str
```

### Utility Functions

#### `len(value)`

Returns the length of a string or list.

```flow
let text = "FlowLang-Script"
print len(text)  # Prints: 15
```

#### `range(start, end)`

Creates a list of integers from start (inclusive) to end (exclusive).

```flow
let numbers = range(1, 5)
print numbers  # Prints: [1, 2, 3, 4]
```

### HTTP Functions

#### `http_get(url)`

Performs an HTTP GET request and returns the response.

```flow
let data = http_get("https://jsonplaceholder.typicode.com/users/1")
print data
```

**Features:**
- Automatic JSON parsing when possible
- Returns dictionary for JSON responses
- Returns string for plain text responses
- Error handling with error messages

#### `http_post(url, data)`

Performs an HTTP POST request with JSON data.

```flow
let response = http_post("https://api.example.com/data", {"key": "value"})
print response
```

### File I/O Functions

#### `read_file(path)`

Reads and returns the contents of a file.

```flow
let content = read_file("data.txt")
print content
```

#### `write_file(path, content)`

Writes content to a file.

```flow
let result = write_file("output.txt", "Hello, World!")
print result  # Prints: Written to output.txt
```

## Usage Examples

### Example 1: Simple Calculator

```flow
func calculate(a, b, operation) {
  if operation == "add" {
    return a + b
  }
  if operation == "subtract" {
    return a - b
  }
  if operation == "multiply" {
    return a * b
  }
  if operation == "divide" {
    return a / b
  }
  return 0
}

let result = calculate(10, 5, "add")
print result
```

### Example 2: API Data Fetching

```flow
let user = http_get("https://jsonplaceholder.typicode.com/users/1")
let filename = "user_data.txt"
write_file(filename, str(user))
print "Data saved successfully"
```

### Example 3: Batch Processing

```flow
func process_item(id) {
  let url = "https://jsonplaceholder.typicode.com/todos/" + str(id)
  let data = http_get(url)
  let filename = "item_" + str(id) + ".txt"
  write_file(filename, str(data))
  return "Processed item " + str(id)
}

let count = 1
while count <= 3 {
  let status = process_item(count)
  print status
  let count = count + 1
}
```

### Example 4: Data Transformation Pipeline

```flow
func fetch_and_transform() {
  print "Fetching data..."
  let raw_data = http_get("https://jsonplaceholder.typicode.com/posts/1")
  
  print "Processing data..."
  let processed = str(raw_data)
  
  print "Saving results..."
  write_file("processed_data.txt", processed)
  
  return "Pipeline complete"
}

let status = fetch_and_transform()
print status
```

## API Reference

### Command Line Interface

```bash
flow run <script.flow>
```

**Arguments:**
- `<script.flow>`: Path to the FlowLang script file

**Examples:**

```bash
flow run examples/basic.flow
flow run workflow.flow
```

### Programmatic Usage

FlowLang can be embedded in Python applications:

```python
from flowlang.lexer import Lexer
from flowlang.parser import Parser
from flowlang.interpreter import Interpreter

# Your FlowLang-Script code
code = """
let x = 10
let y = 20
print x + y
"""

# Execute
tokens = Lexer(code).tokens
ast = Parser(tokens).parse()
Interpreter().eval(ast)
```

### Custom Built-in Functions

Extend FlowLang with custom built-in functions:

```python
from flowlang.interpreter import Interpreter

interp = Interpreter()

# Add custom function
interp.builtins['custom_func'] = lambda args: args[0] * 2

# Execute code that uses it
code = "print custom_func(21)"
tokens = Lexer(code).tokens
ast = Parser(tokens).parse()
interp.eval(ast)
```

## Use Cases

### 1. API Testing and Validation

FlowLang excels at quick API testing without the overhead of larger frameworks.

```flow
let endpoint = "https://api.example.com/health"
let response = http_get(endpoint)
print "API Status:"
print response
```

### 2. Data Pipeline Automation

Create ETL (Extract, Transform, Load) workflows with minimal code.

```flow
func etl_pipeline(source_id) {
  let data = http_get("https://api.source.com/data/" + str(source_id))
  let transformed = str(data)
  write_file("output_" + str(source_id) + ".txt", transformed)
  return "Complete"
}

let ids = range(1, 10)
let i = 1
while i < 10 {
  etl_pipeline(i)
  let i = i + 1
}
```

### 3. Configuration Management

Automate configuration file generation and updates.

```flow
func generate_config(env) {
  let config = "environment=" + env
  write_file(env + "_config.txt", config)
  return "Config generated for " + env
}

generate_config("production")
generate_config("staging")
```

### 4. Microservice Orchestration

Coordinate calls across multiple microservices.

```flow
func orchestrate() {
  let users = http_get("https://api.service1.com/users")
  let orders = http_get("https://api.service2.com/orders")
  
  write_file("users.txt", str(users))
  write_file("orders.txt", str(orders))
  
  return "Orchestration complete"
}

orchestrate()
```

### 5. Scheduled Tasks and Cron Jobs

Perfect for periodic data collection and processing tasks.

```flow
func daily_report() {
  let data = http_get("https://api.example.com/daily-stats")
  let timestamp = str(data)
  write_file("daily_report.txt", timestamp)
  return "Report generated"
}

daily_report()
```

## Integration

### Integration with Python Projects

FlowLang can be embedded in Python applications for scriptable automation.

**Example: Flask Integration**

```python
from flask import Flask, request
from flowlang.lexer import Lexer
from flowlang.parser import Parser
from flowlang.interpreter import Interpreter

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_flowlang():
    code = request.json.get('code')
    
    tokens = Lexer(code).tokens
    ast = Parser(tokens).parse()
    Interpreter().eval(ast)
    
    return {'status': 'success'}
```

### Integration with CI/CD Pipelines

Use FlowLang scripts in continuous integration workflows.

**Example: GitHub Actions**

```yaml
name: Run FlowLang Script
on: [push]
jobs:
  run-script:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
      - name: Install FlowLang
        run: pip install flowlang
      - name: Execute Script
        run: flow run scripts/deploy.flow
```

### Integration with Docker

Create containerized FlowLang execution environments.

**Dockerfile Example:**

```dockerfile
FROM python:3.9-slim

WORKDIR /app

RUN pip install flowlang

COPY scripts/ /app/scripts/

CMD ["flow", "run", "scripts/main.flow"]
```

### Integration with Scheduling Systems

Use with cron or systemd timers for scheduled execution.

**Cron Example:**

```cron
# Run daily report at 9 AM
0 9 * * * /usr/local/bin/flow run /home/user/reports/daily.flow
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Make your changes
4. Run tests to ensure compatibility
5. Commit your changes (`git commit -am 'Add new feature'`)
6. Push to the branch (`git push origin feature/new-feature`)
7. Create a Pull Request

### Development Setup

```bash
git clone https://github.com/ChilliRoger/flowlang.git
cd flowlang
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
```

### Running Tests

```bash
flow run examples/test_all.flow
```

## License

MIT License

Copyright (c) 2025 FlowLang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Support and Resources

- **Documentation**: See `QUICKREF.md` for quick reference
- **Examples**: Check the `examples/` directory for sample scripts
- **Issues**: [GitHub Issues](https://github.com/ChilliRoger/flowlang/issues)
- **Discussions**: [GitHub Discussions](https://github.com/ChilliRoger/flowlang/discussions)

## Acknowledgments

FlowLang is built with Python and relies on the Python standard library for all functionality. Special thanks to the open-source community for inspiration and support.
