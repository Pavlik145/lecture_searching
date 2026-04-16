import os
import json
from operator import index

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as file_obj:
        data = json.load(file_obj)
    if field in data.keys():
        return data[field]
    else:
        print(f"Field {field} not exist")
        return None

def linear_search(sekvence, hodnota):
    slovnik = {}
    pozice = []
    pocet = 0
    for i in range(len(sekvence)-1):
        if sekvence[i] == hodnota:
            pocet += 1
            pozice.append(i)
    slovnik["positions"] = pozice
    slovnik["count"] = pocet

    return slovnik

def binary_search(sekvence,hodnota):

        left = 0
        right = int(len(sekvence) - 1)
        while True:
            middle = int(len(sekvence[left:right]) / 2)
            if sekvence[middle] == hodnota:
                return middle
            elif sekvence[middle] < hodnota:
                left = middle + 1
            elif sekvence[middle] > hodnota:
                right = middle - 1
            else:
                return None

def main():
    pass

if __name__ == '__main__':
    main()
    json_filename = "sequential.json"
    my_data = read_data(json_filename, "unordered_numbers")
    my_data_ordered = read_data(json_filename, "ordered_numbers")
    print(my_data)
    print(linear_search(my_data,0))
    print(binary_search(my_data_ordered,2))

