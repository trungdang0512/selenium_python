import json
import os
from typing import List, Any

class JSONData_Loader:
    @staticmethod
    def load_json_data(filename):
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, '..', 'tests', 'data', filename)  # Điều chỉnh theo cấu trúc thư mục của bạn
        with open(file_path) as file:
            return json.load(file)

    @staticmethod
    def get_data_list_from_json(relative_path: str, key: str) -> List[Any]:
        try:
            # Xây dựng đường dẫn tuyệt đối từ đường dẫn tương đối
            project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
            file_path = os.path.join(project_root, relative_path)
            print(f"Opening file: {file_path}")

            with open(file_path, 'r') as file:
                data = json.load(file)
                print(f"Data loaded from file: {data}")
                if key in data:
                    print(f"Key '{key}' found in JSON file.")
                    return data[key]  # Định dạng đẹp với 4 khoảng trắng
                else:
                    print(f"Key '{key}' not found in JSON file.")
                    return []
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return []
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file '{file_path}'.")
            return []