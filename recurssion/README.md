### RECURSION

##### Overview.
    ✅ Recursion is a programming technique where a function calls itself directly or indirectly.

    ✅ It involves solving a problem by breaking it down into smaller, more manageable sub-problems of the same type.

    ✅ A recursive function must have a Base Case to terminate the recursion and a Recursive Case that reduces  the problem size.


##### Implementation in Programming.
    ✅ Base Case: The condition under which the functin stops calling itself to prevent infinite recursion

    ✅ Recursive Case: The part of the function where it calls itself with a smaller or simpler problem.

##### Example: Fibonacci Sequence.

~~~
    def fibonacci(n):
        # Base case: return n if it is 0 or 1
        if n == 0 or n == 1:
            return n
        # Recursive case: sum of the two preceding numbers
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    print(fibonacci(5))  # Output: 5
~~~

##### Use Cases.
    ✳️ Divide & Conquer Algorithms. Algorithms like merge sort and quick sort use recursion to divide the problem into sub-problems.

    ✳️ Dynamic Programming - Some dynamic programming problems, like Fibonnaci Sequence, can be solved recursively with memoization.

    ✳️ Tree Traversals - Recursion is natural for traversing tree data structures(eg. binary trees).

    ✳️ Backtracking Algorithms - Problems like solving a maze, N-queens, and sudoku use recursion to explore possibilites.

    ✳️ Mathematical Computations - Computing powers, factorials, and fibonacci numbers are classic examples.

    ✳️ Graph Traversals - Depth-first search  (DFS) in graphs is often implemented using  recursion.


##### Real World Applications Of Recursion. 
###### File System Navigation: Navigating directories and files in a file system.

~~~
    import os

    def list_files(directory):
        for entry in os.listdir(directory):
            path = os.path.join(directory, entry)
            if os.path.isdir(path):
                list_files(path)
            else:
                print(path)

    list_files("/path/to/directory")
~~~

###### Web Crawlers: Recursively traversing web pages to gather data.

~~~
import requests
from bs4 import BeautifulSoup

def web_crawler(url, depth):
    if depth == 0:
        return
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a'):
        next_url = link.get('href')
        if next_url:
            web_crawler(next_url, depth - 1)

web_crawler('https://example.com', 3)
~~~

###### Games & Simulations: Implementing algorithms for solving puzzles and games(eg. chess, tic-tac-toe)

~~~
    def solve_maze(maze, position, end):
        x, y = position
        if position == end:
            return True
        if maze[x][y] == 1:
            return False

        maze[x][y] = 1  # mark as visited

        # Move right
        if solve_maze(maze, (x, y + 1), end):
            return True
        # Move down
        if solve_maze(maze, (x + 1, y), end):
            return True
        # Move left
        if solve_maze(maze, (x, y - 1), end):
            return True
        # Move up
        if solve_maze(maze, (x - 1, y), end):
            return True

        maze[x][y] = 0  # unmark if no solution found
        return False

    maze = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    start = (0, 0)
    end = (3, 3)
    print(solve_maze(maze, start, end))  # Output: True or False
~~~

###### Parsing Expressions: Recursively evaluating expressions in compilers and interpreters.

~~~
    def evaluate(expression):
        tokens = expression.split()
        if len(tokens) == 1:
            return int(tokens[0])
        else:
            op = tokens.pop()
            right = evaluate(tokens.pop())
            left = evaluate(tokens.pop())
            if op == '+':
                return left + right
            elif op == '-':
                return left - right

    expression = "3 4 + 2 * 7 /"
    print(evaluate(expression))  # Output: 2

~~~