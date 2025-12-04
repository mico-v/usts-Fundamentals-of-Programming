import keyword
import tokenize
import builtins
from io import BytesIO

def transform_source_code(input_file, output_file):
    with open(input_file, 'rb') as f:
        source_bytes = f.read()

    tokens = list(tokenize.tokenize(BytesIO(source_bytes).readline))
    
    # 获取所有内置函数和异常名，避免将 print, int, ValueError 等转换为大写导致无法运行
    builtin_names = set(dir(builtins))
    
    # 针对本实验特定文件 GuessNumber.py 的额外保留词，防止 import 错误
    # random 是模块名，randint 是函数名，转换为大写会导致 ImportError
    extra_keeps = {'random', 'randint'}
    
    # 我们需要修改的是 NAME 类型的 token
    # 但 tokenize 返回的 token 包含了位置信息，直接修改 token string 再 untokenize 可能会丢失原始格式（如空格）
    # 更精确的方法是根据 token 的位置在源代码上进行替换，或者使用 untokenize (虽然 untokenize 有时并不完美还原)
    # 这里使用 untokenize 简便处理，通常对标准代码效果不错
    
    new_tokens = []
    for token in tokens:
        token_type = token.type
        token_string = token.string
        
        if token_type == tokenize.NAME:
            # 如果不是关键字 且 不是内置名称 且 不是额外保留词，则转换为大写
            if (not keyword.iskeyword(token_string) and 
                token_string not in builtin_names and 
                token_string not in extra_keeps):
                token_string = token_string.upper()
        
        new_tokens.append((token_type, token_string))

    transformed_code = tokenize.untokenize(new_tokens)
    
    # untokenize 返回的是 bytes，在某些 Python 版本中可能已经是 str，因此只在 bytes 情况下解码
    if isinstance(transformed_code, bytes):
        decoded_code = transformed_code.decode('utf-8')
    else:
        decoded_code = transformed_code

    # 使用 newline='' 避免在 Windows 下写入时再次转换换行符，导致多余的空行
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        f.write(decoded_code)
    
    print(f"转换完成。输出文件: {output_file}")

if __name__ == "__main__":
    input_filename = "GuessNumber.py"
    output_filename = "GuessNumber_upper.py"
    
    try:
        transform_source_code(input_filename, output_filename)
        
        # 尝试运行生成的代码以验证（可选，题目要求生成的代码能被正确执行）
        print("-" * 20)
        print("尝试验证生成的代码语法...")
        with open(output_filename, 'r', encoding='utf-8') as f:
            compile(f.read(), output_filename, 'exec')
        print("语法验证通过！")
        
    except Exception as e:
        print(f"发生错误: {e}")