class Queue:
    """ 
    Initialises a new queue object
    """
    def __init__(self):
        self.list = []
        self.n_items = 0
    
    """
    Returns the number of items in the queue
    """
    @property
    def n_items(self) -> int:
        return self._n_items

    """ 
    Sets the number of items in the queue
    @param: the number of items in the queue
    """
    @n_items.setter
    def n_items(self, items: int) -> None:
        self._n_items = items

    """ 
    Adds and item to the end of the queue
    @param src: the source vertex of the edge
    @param to: the destination vertex
    @param weight: weight of the edge
    """
    def enqueue(self, src: int, to: int, weight: int) -> None:
        self.list.append({"from": src, "to": to, "weight": weight})
        self.n_items = self.n_items + 1
    
    """ 
    Removes an item from the start of the queue
    """
    def dequeue(self) -> dict[int, int, int]:
        if not self.is_empty():
            item = self.list[0]
            del self.list[0]
            self.n_items = self.n_items - 1
            return item

    """ 
    Checks if the queue is empty
    """
    def is_empty(self) -> bool:
        if self.n_items == 0:
            return True 
        else:
            return False

    """ 
    Returns the first item in the queue without dequeuing it
    """
    def peek(self) -> None:
        try:
            print("from:", self.list[0]["from"], "to:", self.list[0]["to"], "weight: ", self.list[0]["weight"])
        except IndexError:
            print("The queue is empty")
