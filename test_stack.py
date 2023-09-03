from stack import Stack

def main():
    test_stack_basic()
    test_stack_multiple()
    test_stack_empty()
    test_stack_pop_order()
    test_stack_n_items()
    test_stack()

def test_stack_basic():
    s = Stack()
    s.push(1, 2, 3)
    assert s.pop() == {"from": 1, "to": 2, "weight": 3}

def test_stack_multiple():
    s = Stack()
    s.push(1, 2, 3)
    s.push(4, 5, 6)
    assert s.pop() == {"from": 4, "to": 5, "weight": 6}
    assert s.pop() == {"from": 1, "to": 2, "weight": 3}

def test_stack_empty():
    s = Stack()
    assert s.is_empty() == True 
    s.push(1, 2, 3)
    assert s.is_empty() == False 
    s.pop()
    assert s.is_empty() == True 
    s.pop()

def test_stack_pop_order():
    s = Stack()
    for i in range(25):
        s.push(i, i + 1, i)
    for i in reversed(range(25)):
        assert s.pop() == {"from": i, "to": i + 1, "weight": i}

def test_stack_n_items():
    s = Stack()
    assert s.n_items == 0
    for i in range(25):
        s.push(i, i + 1, i)
        assert s.n_items == i + 1

def test_stack():
    s = Stack()
    assert s.is_empty() == True
    s.push(1, 2, 3)
    assert s.is_empty() == False
    s.push(7, 3, 2)
    s.push(1, 2, 3)
    s.push(3, 5, 1)
    s.push(2, 1, 34)
    s.push(5, 2, 18)
    s.push(6, 3, 9)
    s.push(4, 6, 7)
    s.push(4, 1, 5)
    assert s.n_items == 9
    s.push(5, 7, 87)
    assert s.n_items == 10
    assert s.is_empty() == False
    assert s.pop() == {"from": 5, "to": 7, "weight": 87}
    assert s.n_items == 9
    assert s.pop() == {"from": 4, "to": 1, "weight": 5}
    assert s.pop() == {"from": 4, "to": 6, "weight": 7}
    assert s.pop() == {"from": 6, "to": 3, "weight": 9}
    assert s.pop() == {"from": 5, "to": 2, "weight": 18}
    assert s.pop() == {"from": 2, "to": 1, "weight": 34}
    assert s.pop() == {"from": 3, "to": 5, "weight": 1}
    assert s.pop() == {"from": 1, "to": 2, "weight": 3}
    assert s.pop() == {"from": 7, "to": 3, "weight": 2}
    assert s.is_empty() == False
    assert s.n_items == 1
    assert s.pop() == {"from": 1, "to": 2, "weight": 3}
    assert s.n_items == 0
    assert s.is_empty() == True

if __name__ == "__main__":
    main()