class PQueue:
    """
    Initialises a new Priority Queue
    """
    def __init__(self) -> None:
        self.n_items = 0
        self.list = []
        self.list.append({"from": -1, "to": -1, "weight": -1})

    """
    Gets the number of items in the priority queue
    """
    @property
    def n_items(self) -> None:
        return self._n_items

    """
    Sets the number of items in the priority queue
    """
    @n_items.setter
    def n_items(self, items: int) -> None:
        self._n_items = items

    """
    Adds a new item to the priority queue
    """
    def enqueue(self, src: int, to: int, weight: int) -> None:
        # add the item to the end of the list
        self.list.append({"from": src, "to": to, "weight": weight})
        self.n_items = self.n_items + 1

        # fix up on the added item
        self.fix_up()

    """
    Swaps the last element up the heap if needed
    """
    def fix_up(self) -> None:
        i = len(self.list) - 1
        while i > 0:
            if self.list[i // 2]["weight"] > self.list[i]["weight"]:
                tmp = self.list[i // 2]
                self.list[i // 2] = self.list[i]
                self.list[i] = tmp
                i = i // 2
            else:
                break
    """
    Removes the item with the highest priority
    """
    def dequeue(self) -> dict[int, int, int]:
        if self.is_empty() == True:
            print("The queue is empty")
            return
        
        length = len(self.list) - 1
        # remove the first element, and replace it with the last
        item = self.list[1]
        self.list[1] = self.list[length]
        del self.list[length]
        self.n_items = self.n_items - 1

        # fix down on the first element
        self.fix_down()
        
        return item

    """
    Swaps the first element down the heap if needed
    """           
    def fix_down(self) -> None:
        length = len(self.list)
        i = 1
        while 2 * i < length:
            j = 2 * i

            # choose the largest of the two children
            if j + 1 < length:
                if self.list[j]["weight"] > self.list[j + 1]["weight"]:
                    j += 1
                
            # swap the parent with child if needed
            if self.list[i]["weight"] > self.list[j]["weight"]:
                tmp = self.list[i]
                self.list[i] = self.list[j]
                self.list[j] = tmp
                i = j
            else:
                break

    """
    Returns the item at the top of the queue without removing it.
    """
    def peek(self) -> None:
        try:
            return self.list[1]
        except IndexError:
            print("The queue is empty.")

    """
    Returns whether the queue is empty
    """
    def is_empty(self) -> bool:
        if self.n_items == 0:
            return True 
        else:
            return False
    