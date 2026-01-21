"""
Тесты для лабораторной работы 1
Проверяет корректность работы Queue и Stack в обоих стилях
"""

from lab1_oop import Queue as OOPQueue, Stack as OOPStack
from lab1_functional import (
    create_queue, queue_enqueue, queue_dequeue, queue_peek, queue_is_empty, queue_size,
    create_stack, stack_push, stack_pop, stack_peek, stack_is_empty, stack_size
)


def test_oop_implementation():
    """Тестирование ООП реализации"""
    print("=== Тестирование ООП реализации ===")
    
    # Тестирование Queue
    print("\n1. Тестирование ООП Queue:")
    q = OOPQueue[int]()
    
    assert q.is_empty() == True
    assert q.size() == 0
    
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    assert q.is_empty() == False
    assert q.size() == 3
    assert q.peek() == 1
    assert str(q) == "Queue([1, 2, 3])"
    
    assert q.dequeue() == 1
    assert q.size() == 2
    assert q.peek() == 2
    
    print("   ✓ ООП Queue: все тесты пройдены")
    
    # Тестирование Stack
    print("\n2. Тестирование ООП Stack:")
    s = OOPStack[str]()
    
    assert s.is_empty() == True
    assert s.size() == 0
    
    s.push("A")
    s.push("B")
    s.push("C")
    
    assert s.is_empty() == False
    assert s.size() == 3
    assert s.peek() == "C"
    assert str(s) == "Stack(['A', 'B', 'C'])"
    
    assert s.pop() == "C"
    assert s.size() == 2
    assert s.peek() == "B"
    
    print("   ✓ ООП Stack: все тесты пройдены")


def test_functional_implementation():
    """Тестирование функциональной реализации"""
    print("\n=== Тестирование функциональной реализации ===")
    
    # Тестирование Queue
    print("\n1. Тестирование функциональной Queue:")
    q = create_queue()
    
    assert queue_is_empty(q) == True
    assert queue_size(q) == 0
    
    q = queue_enqueue(q, 10)
    q = queue_enqueue(q, 20)
    q = queue_enqueue(q, 30)
    
    assert queue_is_empty(q) == False
    assert queue_size(q) == 3
    assert queue_peek(q) == 10
    
    item, q = queue_dequeue(q)
    assert item == 10
    assert queue_size(q) == 2
    assert queue_peek(q) == 20
    
    print("   ✓ Функциональная Queue: все тесты пройдены")
    
    # Тестирование Stack
    print("\n2. Тестирование функциональной Stack:")
    s = create_stack()
    
    assert stack_is_empty(s) == True
    assert stack_size(s) == 0
    
    s = stack_push(s, "X")
    s = stack_push(s, "Y")
    s = stack_push(s, "Z")
    
    assert stack_is_empty(s) == False
    assert stack_size(s) == 3
    assert stack_peek(s) == "Z"
    
    item, s = stack_pop(s)
    assert item == "Z"
    assert stack_size(s) == 2
    assert stack_peek(s) == "Y"
    
    print("   ✓ Функциональная Stack: все тесты пройдены")


if __name__ == "__main__":
    print("Запуск тестов для лабораторной работы 1...")
    print("=" * 50)
    
    test_oop_implementation()
    print("-" * 50)
    test_functional_implementation()
    
    print("\n" + "=" * 50)
    print("✅ Все тесты успешно пройдены!")
    print("ООП и функциональная реализации работают корректно.")
