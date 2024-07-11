## GRAPH DATA STRUCTURES

#### Overview
###### 📌 Graph:
    - A collection of nodes(or vertices) connected by edges.

###### 📌 Vertex(Node): 
    - A fundamental unit of a graph.

###### 📌 Edge:
    - A connection between two vertices.

###### 📌 Directed Graph:
    - A graph where edges have a direction, going from one vertex to another.

###### 📌 Undirected Graph:
    - A graph where edges do not have a direction; the connection is bidirectional.

###### 📌 Weighted Graph:
    - A graph where edges have weights(or costs) associated with them.

###### 📌 Unweighted Graph:
    - A graph where all edges have the same weight or no weight at all.


#### Types of Graphs.
##### 📈 1. Directed Graph(Digraph)
    - Edges have a direction.
    - Example: Web pages linked by hyperlinks.

##### 📈 2. Undirected Graph
    - Edges do not have a direction.
    - Example: Social Networks where connections are mutual.

##### 📈 3. Weighted Graph
    - Edges have weights representing costs, distances, or capacities.
    - Examples: Road networks with distances or travel times.

##### 📈 4. Unweighted Graph
    - Edges do not have weights or all weights are equal.
    - Example: Simple Social Networks.

##### 📈 5. Cyclic Graph
    - Contains at least one cycle(a path that starts and ends at the same vertex)
    - Example: Transportation networks with circular routes.

##### 📈 6. Acyclic Graph
    - Does not contain any cycles.
    - Example: Family trees, task scheduling.

##### 📈 7. Tree
    - A connected acyclic graph.
    - Example: Hierarchical structures like organizational charts.

##### 📈 8. DAG(Directed Acyclic Graph)
    - A directed graph with no cycles.
    - Example: Task Scheduling, version Control Systems.


#### Properties
###### 📌 Adjacency
    - Two vertices are adjacent if there is an edge connecting them.

###### 📌 Degree
    - The number of edges connected to a vertex.
        * In a directed graph, each vertex has an in-degree and out-degree

###### 📌 Path
    - A sequence of vertices connected by edges.

###### 📌 Cycle
    - A path that starts and ends at the same vertex.

###### 📌 Connected Graph
    - A graph where there is a path between any two vertices.

###### 📌 Disconnected Graph
    - A graph where some vertices are not connected by paths.



#### Implementation
###### 📌 Adjacency Matrix:
    - A 2D array where "matrix[i][j]" indicates the presence(and possibly weight) of an edge 
     between  vertices "i" and "j".

###### 📌 Adjacency List
    - An array or dictionary where each index(or key) represents a vertex and stores a list of adjacent vertices.


#### Use Cases
###### 📌 Navigation & Routing
    - Finding the shortest or optimal path in road networks, flight routes, etc.
Example:
    - Google maps & GPS Navigation use weighted graphs to represent road networks and find
    the shortest paths between locations using algorithms like Dijkstra's or A*.
   ~~~
    import heapq

    def dijkstra(graph, start):
        queue = []
        heapq.heappush(queue, (0, start))
        distances = {vertex: float('infinity') for vertex in graph}
        distances[start] = 0

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in graph[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

        return distances

    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    print(dijkstra(graph, 'A'))

   ~~~
###### 📌 Social Networks
    - Representing relationships and connections betweeen users.
Example:
    - Social networks use graphs to represent friendships, connections, and recommendations.
    - 
   ~~~
    class SocialNetwork:
    def __init__(self):
        self.network = {}

    def add_user(self, user):
        if user not in self.network:
            self.network[user] = []

    def add_friendship(self, user1, user2):
        if user1 in self.network and user2 in self.network:
            self.network[user1].append(user2)
            self.network[user2].append(user1)

    sn = SocialNetwork()
    sn.add_user('Alice')
    sn.add_user('Bob')
    sn.add_friendship('Alice', 'Bob')
    print(sn.network)  # Output: {'Alice': ['Bob'], 'Bob': ['Alice']}

   ~~~
###### 📌 Network Analysis
    - Analyzing communication or data flow in computer networks.

###### 📌 Recommendation Systems
    - Finding similarities between users or products.

Example:
    - Recommendation systems use graphs to recommend items based on user interactions &
      similarities (eg. Amazon, Netflix).

   ~~~
   class RecommendationSystem:
        def __init__(self):
            self.graph = {}

        def add_interaction(self, user, item):
            if user not in self.graph:
                self.graph[user] = []
            self.graph[user].append(item)

        def recommend(self, user):
            recommendations = set()
            if user in self.graph:
                for item in self.graph[user]:
                    for other_user in self.graph:
                        if other_user != user and item in self.graph[other_user]:
                            recommendations.update(self.graph[other_user])
                recommendations.difference_update(self.graph[user])
            return list(recommendations)

    rs = RecommendationSystem()
    rs.add_interaction('Alice', 'Book1')
    rs.add_interaction('Alice', 'Book2')
    rs.add_interaction('Bob', 'Book1')
    rs.add_interaction('Bob', 'Book3')
    print(rs.recommend('Alice'))  # Output: ['Book3']

   ~~~

###### 📌 Scheduling
    - Task scheduling and dependency resolution.
   

###### 📌 Web Crawling
    - Analyzing and traversing the structure of websites.

Example:
~~~
    import requests
    from bs4 import BeautifulSoup

    def web_crawler(url, max_depth):
        visited = set()

        def crawl(url, depth):
            if depth > max_depth or url in visited:
                return
            visited.add(url)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a['href'] for a in soup.find_all('a', href=True)]
            for link in links:
                crawl(link, depth + 1)

        crawl(url, 0)

    web_crawler('https://example.com', 2)
   ~~~