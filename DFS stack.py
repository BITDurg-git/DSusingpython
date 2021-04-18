class Stack:
    """(LIFO) queuing policy implemented using python list."""

    def __init__(self):
        self.list = []

    def push(self, item):
        """Push 'item' onto the stack."""
        self.list.append(item)

    def pop(self):
        """Pop the most recently pushed item from the stack."""
        return self.list.pop()

    def top(self):
        """Return the last element."""
        return self.list[-1]

    def is_empty(self):
        """Returns true if the stack is empty."""
        return len(self.list) == 0


# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
def dfs(graph, start):
    stack = Stack()
    stack.push(start)
    path = []

    while not stack.is_empty():
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.push(neighbor)

path=dfs(graph,'A')
print(path)

