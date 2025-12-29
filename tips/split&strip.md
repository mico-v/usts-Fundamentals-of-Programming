# .split() 和 .strip() 的区别

在 Python 中，`.split()` 和 `.strip()` 是两个常用的字符串方法，它们的功能和用途不同。

---

## 1. `.split()` 方法
`.split()` 方法用于将字符串按照指定的分隔符拆分成一个列表。如果不指定分隔符，默认会以空白字符（空格、制表符、换行符等）作为分隔符。

### 语法：
```python
str.split(sep=None, maxsplit=-1)
```
- **`sep`**: 可选，指定分隔符，默认为 `None`（即以空白字符分隔）。
- **`maxsplit`**: 可选，指定最大分割次数，默认为 `-1`（即分割所有可能的部分）。

### 示例：
```python
text = "Hello World Python"
result = text.split()
print(result)  # 输出: ['Hello', 'World', 'Python']

text = "apple,banana,orange"
result = text.split(",")
print(result)  # 输出: ['apple', 'banana', 'orange']
```

---

## 2. `.strip()` 方法
`.strip()` 方法用于移除字符串开头和结尾的指定字符（默认为空白字符）。

### 语法：
```python
str.strip(chars=None)
```
- **`chars`**: 可选，指定要移除的字符集合，默认为 `None`（即移除空白字符）。

### 示例：
```python
text = "  Hello World  "
result = text.strip()
print(result)  # 输出: 'Hello World'

text = "***Hello***"
result = text.strip("*")
print(result)  # 输出: 'Hello'
```

---

## 区别总结
| 方法       | 功能                                   | 返回值类型 | 默认操作                     |
|------------|----------------------------------------|------------|------------------------------|
| `.split()` | 按分隔符拆分字符串，返回一个列表       | 列表       | 按空白字符分隔               |
| `.strip()` | 去除字符串两端的指定字符，返回一个字符串 | 字符串     | 去除两端的空白字符           |

---

### 示例对比
```python
text = "  apple, banana, orange  "

# 使用 .split()
result_split = text.split(",")
print(result_split)  # 输出: ['  apple', ' banana', ' orange  ']

# 使用 .strip()
result_strip = text.strip()
print(result_strip)  # 输出: 'apple, banana, orange'
```