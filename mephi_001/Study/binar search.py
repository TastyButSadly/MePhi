def to_camel_case(text):
    text.split('_')
    print(text)
    return ''.join(word.title() for word in text.split('-'))

text = input()
print(to_camel_case(text))