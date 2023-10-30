words = {
    'hello' : 'Xin chao',
    'table': 'Ban',
    'sky': 'bau troi'
}

def output_dict():
    count = 0
    for k, v in words.items():
        print(f'{k} - > {v}')
        count += 1
    print(f"Tu dien co {count} tu")


def add(w, m):
    if w not in words:
        words[w] = m


def delete(w):
    if w in words:
        del words[w]


def find(w):
    if w in words:
        print(words[w])
    else:
        print('Khong tim thay')


if __name__ == '__main__':
    add('test', 'Kiem tra')
    delete('sky')
    output_dict()
    find('sky')