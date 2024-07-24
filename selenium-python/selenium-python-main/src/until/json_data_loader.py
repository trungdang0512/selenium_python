import json
import os


class JSONData_Loader:
    @staticmethod
    def load_json_data(filename):
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, '..', 'tests', 'data', filename)  # Điều chỉnh theo cấu trúc thư mục của bạn
        with open(file_path) as file:
            return json.load(file)