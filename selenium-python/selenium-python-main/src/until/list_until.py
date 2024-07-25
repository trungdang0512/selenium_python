from typing import List


class ListUtils:
    @staticmethod
    def sort_string_list_ignore_case(string_list: List[str]) -> List[str]:
        """
        Sắp xếp danh sách chuỗi không phân biệt chữ hoa chữ thường.

        :param string_list: Danh sách chuỗi cần sắp xếp.
        :return: Danh sách đã được sắp xếp.
        """
        return sorted(string_list, key=str.lower)
