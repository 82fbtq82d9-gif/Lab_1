from typing import Optional, List, TypeVar, Generic

T = TypeVar('T')  # Generic type parameter

class Queue(Generic[T]):
    """
    Queue (Очередь) - структура данных FIFO (First-In-First-Out)
    ООП реализация с использованием Generic для типизации
    """
    
    def __init__(self) -> None:
        """Инициализация пустой очереди"""
        self._items: List[T] = []
    
    def enqueue(self, item: T) -> None:
        """Добавить элемент в конец очереди"""
        self._items.append(item)
    
    def dequeue(self) -> Optional[T]:
        """Удалить и вернуть элемент из начала очереди"""
        if self.is_empty():
            return None
        return self._items.pop(0)
    
    def peek(self) -> Optional[T]:
        """Посмотреть элемент в начале очереди без удаления"""
        if self.is_empty():
            return None
        return self._items[0]
    
    def is_empty(self) -> bool:
        """Проверить, пуста ли очередь"""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Получить размер очереди"""
        return len(self._items)
    
    def __str__(self) -> str:
        """Строковое представление очереди"""
        return f"Queue({self._items})"
    
    def __repr__(self) -> str:
        """Представление для отладки"""
        return f"Queue{self._items}"


class Stack(Generic[T]):
    """
    Stack (Стек) - структура данных LIFO (Last-In-First-Out)
    ООП реализация с использованием Generic для типизации
    """
    
    def __init__(self) -> None:
        """Инициализация пустого стека"""
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        """Добавить элемент на вершину стека"""
        self._items.append(item)
    
    def pop(self) -> Optional[T]:
        """Удалить и вернуть элемент с вершины стека"""
        if self.is_empty():
            return None
        return self._items.pop()
    
    def peek(self) -> Optional[T]:
        """Посмотреть элемент на вершине стека без удаления"""
        if self.is_empty():
            return None
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """Проверить, пуст ли стек"""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Получить размер стека"""
        return len(self._items)
    
    def __str__(self) -> str:
        """Строковое представление стека"""
        return f"Stack({self._items})"
    
    def __repr__(self) -> str:
        """Представление для отладки"""
        return f"Stack{self._items}"


# Демонстрация работы ООП реализации
if __name__ == "__main__":
    print("=== Демонстрация ООП реализации ===")
    
    # Тестирование Queue
    print("\n1. Тестирование Queue (Очередь):")
    queue = Queue[int]()
    
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    
    print(f"   Очередь после добавления: {queue}")
    print(f"   Размер очереди: {queue.size()}")
    print(f"   Первый элемент: {queue.peek()}")
    print(f"   Извлекаем: {queue.dequeue()}")
    print(f"   Очередь после извлечения: {queue}")
    print(f"   Очередь пуста? {queue.is_empty()}")
    
    # Тестирование Stack
    print("\n2. Тестирование Stack (Стек):")
    stack = Stack[str]()
    
    stack.push("Python")
    stack.push("Java")
    stack.push("C++")
    
    print(f"   Стек после добавления: {stack}")
    print(f"   Размер стека: {stack.size()}")
    print(f"   Верхний элемент: {stack.peek()}")
    print(f"   Извлекаем: {stack.pop()}")
    print(f"   Стек после извлечения: {stack}")
    print(f"   Стек пуст? {stack.is_empty()}")
