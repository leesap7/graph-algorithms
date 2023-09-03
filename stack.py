class Stack:
    """
    Initialises a new stack object
    """
    def __init__(self) -> None:
        self.list = []
        self.n_items = 0

    """
    Adds an item to the top of the stack
    @param src: the source vertex of the edge
    @param to: the destination vertex
    @param weight: weight of the edge
    """
    def push(self, src: int, to: int, weight: int) -> None:
        self.list.insert(0, {"from": src, "to": to, "weight": weight})
        self.n_items = self.n_items + 1
    
    """ 
    Removes an item from the top of the stack
    """
    def pop(self):
        if not self.is_empty():
            item = self.list[0]
            del self.list[0]
            self.n_items = self.n_items - 1
            return item
    
    """
    Returns the number of items in the stack
    """
    @property
    def n_items(self) -> int:
        return self._n_items

    """
    Sets the number of items in the stack
    @param: the number of items in the stack
    """
    @n_items.setter
    def n_items(self, items: int) -> None:
        self._n_items = items

    """
    Returns the item at the top of the stack without removing it
    """
    def peek(self) -> None:
        try:
            print("from:", self.list[0]["from"], "to:", self.list[0]["to"], "weight: ", self.list[0]["weight"])
        except IndexError:
            print("The stack is empty")

    """ 
    Checks if the stack is empty
    """
    def is_empty(self) -> bool:
        if self.n_items == 0:
            return True 
        else:
            return False
