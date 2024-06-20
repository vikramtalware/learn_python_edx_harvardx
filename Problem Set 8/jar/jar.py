class Jar:
    def __init__(self, capacity=12):
        if capacity > 0:
            self._capacity = capacity
            self._size = 0
        else:
            raise ValueError("Overfull or Please enter a +ve Number.")

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if (self.size + n > self.capacity) or (n > self.capacity):
            raise ValueError("Capacity Exceeded")
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError(f"Only {self.size} cookies are left.")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar()
    print(jar)

if __name__ == "__main__":
    main()
