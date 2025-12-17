# FlowLang Quick Reference

## Syntax at a Glance

### Variables
```flow
let x = 42
let name = "FlowLang"
```

### Operators
- Arithmetic: `+`, `-`, `*`, `/`
- Comparison: `<`, `>`, `<=`, `>=`, `==`, `!=`

### Control Flow
```flow
if condition {
  // code
}

while condition {
  // code
}
```

### Functions
```flow
func name(param1, param2) {
  return value
}
```

### Built-in Functions

**Utility:**
- `print(value)` - Output to console
- `len(value)` - Get length
- `type(value)` - Get type
- `str(value)` - Convert to string
- `int(value)` - Convert to integer
- `range(start, end)` - Create number list
- `input(prompt)` - Read user input

**HTTP:**
- `http_get(url)` - GET request
- `http_post(url, data)` - POST request

**File I/O:**
- `read_file(path)` - Read file
- `write_file(path, content)` - Write file

## Common Patterns

### API Call with Error Handling
```flow
let data = http_get("https://api.example.com/data")
if type(data) == "dict" {
  write_file("data.json", str(data))
}
```

### Data Processing Loop
```flow
let ids = range(1, 10)
let count = 1

while count < 10 {
  let url = "https://api.example.com/item/" + str(count)
  let item = http_get(url)
  write_file("item_" + str(count) + ".txt", str(item))
  let count = count + 1
}
```

### Function Composition
```flow
func fetch(id) {
  return http_get("https://api.example.com/" + str(id))
}

func save(data, filename) {
  return write_file(filename, str(data))
}

let user = fetch(1)
let result = save(user, "user.txt")
```

## Tips

1. **String concatenation:** Use `+` operator
2. **Type conversion:** Use `str()` and `int()` built-ins
3. **Truthy values:** 0 is falsy, non-zero is truthy
4. **Return values:** Functions without explicit `return` return `None`
5. **HTTP responses:** Auto-parsed as JSON if possible

## Example Workflows

### Simple API Test
```flow
let response = http_get("https://api.github.com")
print response
```

### Data Backup
```flow
let data = http_get("https://api.example.com/important")
write_file("backup.txt", str(data))
print "Backup complete"
```

### Batch Processing
```flow
func process(id) {
  let data = http_get("https://api.example.com/" + str(id))
  write_file("output_" + str(id) + ".txt", str(data))
  return "Done"
}

let i = 1
while i < 6 {
  process(i)
  let i = i + 1
}
```
