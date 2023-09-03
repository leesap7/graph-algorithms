from queue import Queue

def main():
    test_queue()
    test_queue_basic()
    test_queue_n_items()
    test_queue_multiple()
    test_queue_empty()
    test_dequeue_order()

def test_queue_basic():
    q = Queue()
    q.enqueue(1, 2, 3)
    assert q.dequeue() == {"from": 1, "to": 2, "weight": 3}

def test_queue_multiple():
    q = Queue()
    q.enqueue(1, 2, 3)
    q.enqueue(4, 5, 6)
    assert q.dequeue() == {"from": 1, "to": 2, "weight": 3}
    assert q.dequeue() == {"from": 4, "to": 5, "weight": 6}

def test_queue_empty():
    q = Queue()
    assert q.is_empty() == True 
    q.enqueue(1, 2, 3)
    assert q.is_empty() == False 
    q.dequeue()
    assert q.is_empty() == True 
    q.dequeue()

def test_dequeue_order():
    q = Queue()
    for i in range(25):
        q.enqueue(i, i + 1, i)
    for i in range(25):
        assert q.dequeue() == {"from": i, "to": i + 1, "weight": i}

def test_queue_n_items():
    q = Queue()
    assert q.n_items == 0
    for i in range(25):
        q.enqueue(i, i + 1, i)
        assert q.n_items == i + 1

def test_queue():
    q = Queue()
    assert q.is_empty() == True
    q.enqueue(1, 2, 3)
    assert q.is_empty() == False
    q.enqueue(7, 3, 2)
    q.enqueue(1, 2, 3)
    q.enqueue(3, 5, 1)
    q.enqueue(2, 1, 34)
    q.enqueue(5, 2, 18)
    q.enqueue(6, 3, 9)
    q.enqueue(4, 6, 7)
    q.enqueue(4, 1, 5)
    assert q.n_items == 9
    q.enqueue(5, 7, 87)
    assert q.n_items == 10
    assert q.is_empty() == False
    assert q.dequeue() == {"from": 1, "to": 2, "weight": 3}
    assert q.n_items == 9
    assert q.dequeue() == {"from": 7, "to": 3, "weight": 2}
    assert q.dequeue() == {"from": 1, "to": 2, "weight": 3}
    assert q.dequeue() == {"from": 3, "to": 5, "weight": 1}
    assert q.dequeue() == {"from": 2, "to": 1, "weight": 34}
    assert q.dequeue() == {"from": 5, "to": 2, "weight": 18}
    assert q.dequeue() == {"from": 6, "to": 3, "weight": 9}
    assert q.dequeue() == {"from": 4, "to": 6, "weight": 7}
    assert q.dequeue() == {"from": 4, "to": 1, "weight": 5}
    assert q.is_empty() == False
    assert q.n_items == 1
    assert q.dequeue() == {"from": 5, "to": 7, "weight": 87}
    assert q.n_items == 0
    assert q.is_empty() == True