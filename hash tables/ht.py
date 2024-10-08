## 1. ONE WAY
## 2. DETERMINISTIC

class HashTable:
    def __init__(self, size=7) -> None:
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 21) % len(self.data_map)

        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        


my_hash_table = HashTable()
my_hash_table.print_table()