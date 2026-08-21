import re
import sys

def transform_md_images(text: str) -> str:
    """将标准 Markdown 图片语法 ![](url) 替换为 ![url](url)"""
    pattern = r'!\[([^)]*)\]\(([^)]+)\)'

    def replacer(m):
        alt = m.group(1).strip()
        url = m.group(2).strip()
        if alt == '':
            return f'![{url}]({url})'
        return m.group(0)

    return re.sub(pattern, replacer, text)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            content = f.read()
        result = transform_md_images(content)
        with open('res.md', 'w', encoding = 'utf-8') as ff:
            ff.write(result)
    else:
        content = sys.stdin.read()
        result = transform_md_images(content)
        print(result, end='')
