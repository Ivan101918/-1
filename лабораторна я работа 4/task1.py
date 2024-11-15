import json


# TODO решите задачу
def task() -> float:
    with open('input.json', 'r') as f:
        return round(sum([k['score'] * k['weight'] for k in json.load(f)]), 3)


print(task())
