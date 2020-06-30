# Resolve the problem!!
import re

def run():
    with open('./encoded.txt', 'r', encoding = 'utf-8') as f:
        code = f.read()
    decode=''.join(re.findall('[a-z]', code))
    print(decode)

if __name__ == '__main__':
    run()
