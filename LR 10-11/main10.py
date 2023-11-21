import json

INPUT_FILENAME = 'input.json'

def task_1(files):
    list_ = []
    with open(files, 'r') as f:
        a = json.load(f)

        for index in range(len(a)):
            m = a[index]['score'] * a[index]['weight']
            list_.append(m)

    return f'{sum(list_):.3f}'

print(task_1(INPUT_FILENAME))


