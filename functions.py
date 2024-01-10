import json, os.path
import datetime
from pprint import pprint


def load_operations():
    """список всех операций"""
    operations_json = os.path.join('src', 'operations.json')
    with open(operations_json, 'r', encoding="utf-8") as file:
        convert_js = json.load(file)
        return convert_js


convert_js = load_operations()


def last_operations():
    """Вывод последних 5-ти операций"""
    list_convert_js = []
    counter = 0
    for i in convert_js:
        if i['state'] == 'EXECUTED':
            counter += 1
            list_convert_js.append(i)
            if counter == 5:
                break
    return list_convert_js


a = last_operations()

a.sort(key=lambda x: x.get('date'), reverse=True)




for i in a:
    data_list = i['date']
    dt = datetime.datetime.fromisoformat(data_list)
    card = i['from']
    card_number = card.split()[-1]
    name_card = card.split()[0]
    private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
    chunks, chunk_size = len(private_number), len(private_number) // 4
    card_show_to = i['to']
    name_card_to = card_show_to.split()[0]
    card_to = i['to'][-4:].rjust(len(i['to'][-6:]), "*")
    print(dt.date().strftime('%d.%m.%Y'), i['description'])
    print(name_card, " ".join([private_number[i:i + chunk_size] for i in range(0, chunks, chunk_size)]), '->',name_card_to, card_to)
    print(i['operationAmount']['amount'], i['operationAmount']['currency']['name'])
    print()