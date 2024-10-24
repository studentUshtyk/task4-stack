class MyQueue:

    def __init__(self):
        self.stack1 = []  # Основний стек для додавання елементів
        self.stack2 = []  # Стек для вилучення елементів

    def push(self, x: int) -> None:
        """Додає елемент x до черги"""
        self.stack1.append(x)

    def pop(self) -> int:
        """Видаляє і повертає перший елемент черги"""
        if not self.stack2:
            # Якщо stack2 порожній, перенесемо всі елементи з stack1 в stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        """Повертає перший елемент черги без вилучення"""
        if not self.stack2:
            # Якщо stack2 порожній, перенесемо всі елементи з stack1 в stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        """Перевіряє, чи є черга порожньою"""
        return not self.stack1 and not self.stack2

# Приклад використання:
myQueue = MyQueue()
myQueue.push(1)  # черга: [1]
myQueue.push(2)  # черга: [1, 2]
print(myQueue.peek())  # повертає 1
print(myQueue.pop())   # повертає 1, черга тепер: [2]
print(myQueue.empty()) # повертає False
