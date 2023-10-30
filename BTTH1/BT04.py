import json

def read_data():
    with open('data/employee.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def output(data):
    for e in data:
        for k, v in e.items():
            if k == 'ma_nv':
                print(f'Ma nhan vien: {v}')
            elif k == 'ten_nv':
                print(f'Ten nhan vien: {v}')


def add(data, id, name):
    e = {
        "ma_nv": id,
        "ten_nv": name
    }

    data.append(e)

    with open("data/employee.json", 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def search(data, kw):
    res = []
    for e in data:
        if e['ten_nv'].find(kw) >= 0:
            res.append(e)
    return res


def search2(data, kw):
    return [e for e in data if e['ten_nv'].find(kw) >= 0]


def delete(data, id):
    for idx, e in enumerate(data):
        if e['ma_nv'] == id:
            del data[idx]
            break

    with open("data/employee.json", 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    data = read_data()
    add(id=99, name='Tran Thi B', data=data)
    # output(data)
    output(search2(kw='Nguyễn', data=data))
    delete(id=99, data=data)
    output(data)