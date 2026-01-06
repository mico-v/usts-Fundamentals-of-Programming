# Python 文件读写操作详解

Python 均提供了内置的 `open()` 函数来处理文件读写，配合 `with` 语句使用非常方便。无需导入任何外部库即可使用。

## 1. 打开文件 `open()`

基本语法：
```python
open(file, mode='r', encoding=None, ...)
```

- `file`: 文件路径（相对路径或绝对路径）。
- `mode`: 打开模式，默认为 `'r'` (只读)。
- `encoding`: 编码格式，推荐使用 `'utf-8'`。

### 常用模式 (Mode)对照表

| 模式 | 描述 | 注意事项 |
| :--- | :--- | :--- |
| `'r'` | **只读** (Read) | 默认模式。文件必须存在，否则抛出 `FileNotFoundError`。 |
| `'w'` | **写入** (Write) | 文件不存在则创建；**文件存在则清空原内容**从头写入。 |
| `'a'` | **追加** (Append) | 文件不存在则创建；文件存在则在**末尾**追加内容，不移动光标。 |
| `'b'` | **二进制模式** (Binary) | 与其它模式组合使用，如 `'rb'`, `'wb'`。用于非文本文件（图片、音频等）。 |
| `'t'` | **文本模式** (Text) | 默认模式。与其它模式组合，如 `'rt'`（等同于 `'r'`）。 |
| `'+'` | **更新** (Update) | 可读可写。如 `'r+'` (读写，指针在开头), `'w+'` (读写，先清空)。 |

---

## 2. 核心利器：`with` 语句 (上下文管理器)

**强烈推荐**使用 `with` 关键字来进行文件操作。它可以自动管理上下文，确保文件在操作完成后（或发生异常时）自动关闭，避免资源泄露。

**对比：**

❌ **不推荐写法** (容易忘记 close，异常时无法关闭)：
```python
f = open('data.txt', 'w', encoding='utf-8')
f.write('Hello')
# 如果这里报错，close() 就不会执行
f.close()
```

✅ **推荐写法**：
```python
file_path = 'data.txt'
with open(file_path, 'w', encoding='utf-8') as f:
    f.write('Hello Python!\n')
    f.write('这是第二行。')
# 离开缩进块后，文件 f 会由 python 自动调用 .close() 关闭
```

---

## 3. 写入文件操作

### `write(str)`
写入一个字符串。注意：`write` 不会自动添加换行符 `\n`，需要手动添加。

### `writelines(list_of_str)`
写入一个字符串列表。注意：它也不会自动添加换行符，只是将列表中的字符串拼接写入。

**示例：**
```python
lines = ["第一行数据\n", "第二行数据\n", "End"]

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write("=== 开始记录 ===\n")
    f.writelines(lines) 
```

---

## 4. 读取文件操作

假设我们要读取上面生成的 `output.txt`。

### (1) `read(size=-1)`
读取整个文件内容（或者指定字符数）。
```python
with open('output.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
```

### (2) `readline()`
每次只读取一行（包含末尾的换行符 `\n`）。适合大文件，逐行处理。
```python
with open('output.txt', 'r', encoding='utf-8') as f:
    line1 = f.readline()
    print(f"Line 1: {line1.strip()}") # strip() 去除首尾空白符/换行符
    line2 = f.readline()
    print(f"Line 2: {line2.strip()}")
```

### (3) `readlines()`
一次性读取所有行，返回一个列表 `list`。
```python
with open('output.txt', 'r', encoding='utf-8') as f:
    lines_list = f.readlines()
    print(lines_list) 
    # 输出: ['=== 开始记录 ===\n', '第一行数据\n', '第二行数据\n', 'End']
```

### (4) ⭐ 最佳实践：直接遍历文件对象
这是最 Pythonic 且内存最高效的方法，特别适合读取超大文件（GB级别），因为它一次只读一行到内存。
```python
with open('output.txt', 'r', encoding='utf-8') as f:
    for line in f:
        # line 包含末尾的 '\n'
        print(line.strip())
```

---

## 5. 文件指针 (Cursor) - 进阶

文件就像磁带，读写都有一个“磁头”指针。

- **`tell()`**: 返回当前指针的位置（字节偏移量）。
- **`seek(offset, whence)`**: 移动指针。
    - `offset`: 偏移量。
    - `whence`: 
        - `0`: 文件开头 (默认)
        - `1`: 当前位置
        - `2`: 文件末尾

**场景**：读完文件后想再读一遍。
```python
with open('output.txt', 'r', encoding='utf-8') as f:
    print(f.read()) # 读完后指针在末尾
    
    print("--- 再次读取为空 ---")
    print(f.read()) # 这里读不到内容
    
    f.seek(0) # 指针重置到开头
    print("--- 重置后读取 ---")
    print(f.read())
```

---

## 6. 常见避坑指南

1.  **编码报错 (`UnicodeDecodeError`)**: 
    - Windows中文系统默认编码是 `GBK`，而现有大部分文件是 `UTF-8`。
    - **解决**：永远在 `open()` 中显式指定 `encoding='utf-8'`。
    
2.  **路径转义问题**:
    - Windows 路径使用反斜杠 `\`，如 `C:\new\text.txt`，其中 `\n` 和 `\t` 会被转义。
    - **解决**：
        - 字符串前加 `r`：`r'C:\new\text.txt'`
        - 使用正斜杠 `/`：`'C:/new/text.txt'`
        - 使用 `os.path.join`。

3.  **文件未找到 (`FileNotFoundError`)**:
    - 确保路径正确。使用相对路径时，要注意当前工作目录（CWD）在哪里。
