import random
import string

class StringHelper:
    @staticmethod
    def generate_name(length=10):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))
