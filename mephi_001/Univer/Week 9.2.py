def file_replace(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        res = ''
        n = 10
        for i in range(n - 1):
            text = file.readline()
            res += text.replace(' ', ';')

    with open(file_path, 'r+', encoding='utf-8') as file:
        file.write(res)


file_path = 'l9d5.txt'
file_replace(file_path)
