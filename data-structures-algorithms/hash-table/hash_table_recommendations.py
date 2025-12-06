class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                self.table[index].pop(i)
                return True
        return False

def main():
    recommendations = HashTable(size=10)
    recommendations.insert("user491", ["a", "b", "c"])
    recommendations.insert("user202", ["x", "y"])
    print("Recommendations for user491:", recommendations.get("user491"))
    print("Recommendations for user202:", recommendations.get("user202"))
    recommendations.insert("user491", ["a", "b", "c", "d"])
    print("Updated recommendations for user491:", recommendations.get("user491"))
    recommendations.delete("user491")
    print("After deletion, user491:", recommendations.get("user491"))

if __name__ == "__main__":
    main()

