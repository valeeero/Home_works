import json


class WriteJsonFile:


    start_json_file = "./HW.json"
    result_json_file = "./HW_result.json"
    start_dict = {}

    def make_dict(self):
        """Return dictionary from json-file"""
        with open(self.start_json_file, 'r') as json_file:
            self.start_dict = json.load(json_file)
            return self.start_dict

    def dict_sort_by_type(self, some_func):
        """Return dictionary with sorted types of values"""
        employee = self.start_dict['employee']
        main_dict = {}
        for human in employee:
            first_name = human.get('firstName')
            last_name = human.get('lastName')
            total_name = f"{first_name} {last_name}"
            int_ = []
            string_ = []
            float_ = []
            none_ = []
            bool_ = []
            for k, v in human.items():
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
            my_dict_types = {'int': int_, 'string': string_, 'float': float_, 'None': none_, 'bool': bool_}
            my_dict_names = {total_name: my_dict_types}
            main_dict.update(my_dict_names)
            self.start_dict.update({'employee': main_dict})
        return self.start_dict

    def save_sorted_dict(self, func):
        """Return new json-file"""
        with open(self.result_json_file, 'w') as file:
            json.dump(self.start_dict, file, indent=3)

    def main(self):
        """Main function which start run code"""
        self.save_sorted_dict(self.dict_sort_by_type(self.make_dict()))


some_file = WriteJsonFile()

if __name__ == "__main__":
    some_file.main()
