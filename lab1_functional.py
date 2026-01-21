from typing import Optional, Dict, List, TypeVar, Tuple, Any
import copy

T = TypeVar('T')  # Generic type parameter

# ========== QUEUE (Очередь) Функциональный стиль ==========

def create_queue() -> Dict[str, List[T]]:
    """
    Создать новую пустую очередь
    Возвращает словарь с ключом 'items' для хранения элементов
    """
    return {"items": []}


def queue_enqueue(queue: Dict[str, List[T]], item: T) -> Dict[str, List[T]]:
    """
    Добавить элемент в конец очереди
    Возвращает новую очередь (не изменяет исходную)
    """
    new_queue = copy.deepcopy(queue)
    new_queue["items"].append(item)
    return new_queue


def queue_dequeue(queue: Dict[str, List[T]]) -> Tuple[Optional[T], Dict[str, List[T]]]:
    """
    Удалить и вернуть элемент из начала очереди
    Возвращает кортеж: (извлеченный_элемент, новая_очередь)
    """
    if not queue["items"]:
        return None, queue
    
    new_queue = copy.deepcopy(queue)
    item = new_queue["items"].pop(0)
    return item, new_queue


def queue_peek(queue: Dict[str, List[T]]) -> Optional[T]:
    """
    Посмотреть элемент в начале очереди без удаления
    """
    if not queue["items"]:
        return None
    return queue["items"][0]


def queue_is_empty(queue: Dict[str, List[T]]) -> bool:
    """Проверить, пуста ли очередь"""
    return len(queue["items"]) == 0


def queue_size(queue: Dict[str, List[T]]) -> int:
    """Получить размер очереди"""
    return len(queue["items"])


def queue_to_string(queue: Dict[str, List[T]]) -> str:
    """Получить строковое представление очереди"""
    return f"Queue({queue['items']})"


# ========== STACK (Стек) Функциональный стиль ==========

def create_stack() -> Dict[str, List[T]]:
    """
    Создать новый пустой стек
    Возвращает словарь с ключом 'items' для хранения элементов
    """
    return {"items": []}


def stack_push(stack: Dict[str, List[T]], item: T) -> Dict[str, List[T]]:
    """
    Добавить элемент на вершину стека
    Возвращает новый стек (не изменяет исходный)
    """
    new_stack = copy.deepcopy(stack)
    new_stack["items"].append(item)
    return new_stack


def stack_pop(stack: Dict[str, List[T]]) -> Tuple[Optional[T], Dict[str, List[T]]]:
    """
    Удалить и вернуть элемент с вершины стека
    Возвращает кортеж: (извлеченный_элемент, новый_стек)
    """
    if not stack["items"]:
        return None, stack
    
    new_stack = copy.deepcopy(stack)
    item = new_stack["items"].pop()
    return item, new_stack


def stack_peek(stack: Dict[str, List[T]]) -> Optional[T]:
    """
    Посмотреть элемент на вершине стека без удаления
    """
    if not stack["items"]:
        return None
    return stack["items"][-1]


def stack_is_empty(stack: Dict[str, List[T]]) -> bool:
    """Проверить, пуст ли стек"""
    return len(stack["items"]) == 0


def stack_size(stack: Dict[str, List[T]]) -> int:
    """Получить размер стека"""
    return len(stack["items"])


def stack_to_string(stack: Dict[str, List[T]]) -> str:
    """Получить строковое представление стека"""
    return f"Stack({stack['items']})"


# Демонстрация работы функциональной реализации
if __name__ == "__main__":
    print("=== Демонстрация функциональной реализации ===")
    
    # Тестирование Queue
    print("\n1. Тестирование Queue (Очередь):")
    q = create_queue()
    
    q = queue_enqueue(q, 100)
    q = queue_enqueue(q, 200)
    q = queue_enqueue(q, 300)
    
    print(f"   Очередь после добавления: {queue_to_string(q)}")
    print(f"   Размер очереди: {queue_size(q)}")
    print(f"   Первый элемент: {queue_peek(q)}")
    
    item, q = queue_dequeue(q)
    print(f"   Извлекаем: {item}")
    print(f"   Очередь после извлечения: {queue_to_string(q)}")
    print(f"   Очередь пуста? {queue_is_empty(q)}")
    
    # Тестирование Stack
    print("\n2. Тестирование Stack (Стек):")
    s = create_stack()
    
    s = stack_push(s, "HTML")
    s = stack_push(s, "CSS")
    s = stack_push(s, "JavaScript")
    
    print(f"   Стек после добавления: {stack_to_string(s)}")
    print(f"   Размер стека: {stack_size(s)}")
    print(f"   Верхний элемент: {stack_peek(s)}")
    
    item, s = stack_pop(s)
    print(f"   Извлекаем: {item}")
    print(f"   Стек после извлечения: {stack_to_string(s)}")
    print(f"   Стек пуст? {stack_is_empty(s)}")
