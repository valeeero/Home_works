import json


def open_json():
    with open("HW.json", 'r') as json_file:
        dict_data = json.load(json_file)
    return dict_data


def dict_types(result_dict):
    employee = result_dict['employee']
    main_dict = {}
    for j in employee:
        first_name = j.get('firstName')
        last_name = j.get('lastName')
        total_name = f"{first_name} {last_name}"
        int_ = []
        string_ = []
        float_ = []
        none_ = []
        bool_ = []
        for k, v in j.items():
            if type(v).__name__ == 'int':
                int_.append(k)
            elif type(v).__name__ == 'str':
                string_.append(k)
            elif type(v).__name__ == 'float':
                float_.append(k)
            elif type(v).__name__ == 'NoneType':
                none_.append(k)
            elif type(v).__name__ == 'bool':
                bool_.append(k)
        dict_types = {'int': int_, 'string': string_, 'float': float_, 'None': none_, 'bool': bool_}
        dict_names = {total_name: dict_types}
        main_dict.update(dict_names)
        result_dict.update({'employee': main_dict})
    return result_dict


def finish(result_dict):
    with open('./HW_result.json', 'w') as file:
        json.dump(result_dict, file, indent=1)


def main():
    finish(dict_types(open_json()))


main()

print('File save in HW_result.json. This file you make open in main directory.')
