class CIRCULARARRAYQUEUE:

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * CIRCULARARRAYQUEUE.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        item_to_dequeue = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return item_to_dequeue

    def enqueue(self, element):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the capacity

        back_of_the_queue = (self._front + self._size) % len(self._data)
        self._data[back_of_the_queue] = element
        self._size += 1

    def _resize(self, new_capacity):
        old_data = self._data
        self._data = [None] * new_capacity

        current_index = self._front
        for item in range(self._size):
            self._data[item] = old_data[current_index]
            current_index = (current_index + 1) % len(old_data)

        self._front = 0


class Empty(Exception):
    def __init__(self, message="Queue is empty"):
        self.message = message
        super().__init__(self.message)


if __name__ == "__main__":
    queue = CIRCULARARRAYQUEUE()

    print("QUEUES USING CIRCULAR ARRAYS")
    print(f"The initial queue size is: {len(queue)}")
    print(f"Is queue empty? {queue.is_empty()}")

    print("\n Enqueueing our Queue")
    elements_to_enqueue = ['Alice', 'Bob', 'William', 'Dorothy', 'Jessica']

    for person in elements_to_enqueue:
        queue.enqueue(person)
        print(f"Added {person}. Queue size is now: {len(queue)}")

    print(f"\n Person at the front of the line: {queue.first()}")

    print("\nServing people from the front of the queue:")
    for i in range(3):
        served_person = queue.dequeue()
        print(f"Served: {served_person}. Queue size is now: {len(queue)}")

    print("\n Adding more people to induce a wrap around in the array")
    more_people = ['Frank', 'Linda', 'Ford']

    for person in more_people:
        queue.enqueue(person)
        print(f"Added {person}. Queue size is now: {len(queue)}")

    print(f"\nPerson currently at the front: {queue.first()}")
    print(f"Total people still in queue: {len(queue)}")

    print(f"\nInternal details:")
    print(f"Front index: {queue._front}")
    print(f"Array contents: {queue._data}")