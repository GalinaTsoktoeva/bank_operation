import json
from _datetime import datetime

def download_data(filename):
    """
    function for downloads from file json
    :param filename: file name for downloads
    :return: data from file json
    """

    with open(filename, 'r', encoding='utf-8') as file:
        data_ex = json.load(file)

    sort_data = sorted(data_ex, key=lambda x: x.get('date', ""), reverse=True)

    return sort_data


def refactor_account(array):

    if array[0] == "Счет":
        str_from = array[1][-4:]
        array[1] = "**" + str_from
    else:
        array[-1] = array[-1][:4] + " " + array[-1][4:6] + "XX" + " " + "XXXX" + " " + array[-1][-4:]

    return " ".join(array)


def refactor_amount(operation_amount):
    res = operation_amount["amount"] + " " + operation_amount["currency"]['name']
    return res


def refactor_string(text):
    result = ""
    if text["state"].lower() == "EXECUTED".lower():
        # 14.10.2018 Перевод организации
        # Visa Platinum 7000 79** **** 6361 -> Счет **9638
        # 82771.72 руб.
        date_mod = datetime.strptime(text['date'], '%Y-%m-%dT%H:%M:%S.%f')
        date = datetime.strftime(date_mod, '%d.%m.%Y')

        result += date + " " + text["description"] + "\n"
        if "from" in text:
            account_from = refactor_account(text["from"].split())
            result += account_from + " -> "

        account_to = refactor_account(text["to"].split())
        result += account_to

        res_amount = refactor_amount(text["operationAmount"])
        result += "\n" + res_amount

        print(result)
        return result


