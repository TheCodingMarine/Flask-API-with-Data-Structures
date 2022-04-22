class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def custom_hash(self, key):
        """Create a custom hash value using ordinals of input characters."""
        hash_value = 0
        for i in key:
            hash_value += ord(i)
            hash_value = (hash_value * (i)) % self.table_size
        return hash_value

    def add_key_value(self, key, value):
        hashed_key = self.custom_hash
        if self.hash_table[hashed_key] is None:
            self.hash_table[hashed_key] = Node(Data(key, value), None)
        else: 