from flask import Flask, request, render_template, jsonify

import heapq

class Graph:
    def __init__(self):
        self.graph = {} # Dictionary to store the graph
        self.vertices = [] # Dictionary to store heuristic values for each vertex

    # Function to add heuristic value
    def addVertex(self, vertex):
        self.vertices.append(vertex)

    # Function to add an edge with a weight
    def addEdge(self, start, end, weight):
        if start not in self.graph:
            self.graph[start] = {}
        self.graph[start][end] = weight

    def dijkstra(self, start, finish):
        distance = {vertex: float('inf') for vertex in self.vertices}
        distance[start] = 0

        # Dictionary to store visited vertices
        visited = {vertex: False for vertex in self.vertices}

        came_from = {vertex: None for vertex in self.vertices}
        came_from[start] = start

        # Priority queue to store vertices based on their distance
        queue = [(0, start)]

        while queue:
            print(queue)
            current_distance, current_vertex = heapq.heappop(queue)

            print(current_vertex)
            visited[current_vertex] = True

            if current_vertex == finish:
                path = [current_vertex]
                while current_vertex != start:
                    current_vertex = came_from[current_vertex]
                    path.append(current_vertex)
                return path[::-1] 

            if current_vertex in self.graph:
                for next_vertex, weight in self.graph[current_vertex].items():
                    print(current_vertex, next_vertex)
                    if not visited[next_vertex]:
                        if (current_distance + weight < distance[next_vertex]):
                            distance[next_vertex] = current_distance + weight
                            came_from[next_vertex] = current_vertex
                            heapq.heappush(queue, (distance[next_vertex], next_vertex))

        return None

g = Graph() # Create an instance of the Graph class

# Add vertices with heuristic values to the graph
# lantai 1
g.addVertex("h&m lantai 1")
g.addVertex("djournal")
g.addVertex("starbuck")
g.addVertex("mark&spencer")
g.addVertex("pandora")
g.addVertex("frank&co")
g.addVertex("tumi")
g.addVertex("pintu keluar 10")
g.addVertex("elemis")
g.addVertex("mondial")
g.addVertex("sociolla")
g.addVertex("lings")
g.addVertex("mondial")
g.addVertex("eskalator g1") #deket h&m
g.addVertex("eskalator g2") #eska tengah lobby
g.addVertex("melisa")
g.addVertex("adele")
g.addVertex("timberland")
g.addVertex("hyundai")
g.addVertex("elevatione")
g.addVertex("max fashion")
g.addVertex("the gourmet")
g.addVertex("pintu keluar 9")
g.addVertex("lift g")
g.addVertex("eskalator g3") #deket gourmet
g.addVertex("marquine")
g.addVertex("axel")
g.addVertex("kopi kenangan")
g.addVertex("pintu keluar x") #aku ga tau ini pintu keluar no berapa

# Add edges with weights
g.addEdge("max fashion", "starbucks", 32)
g.addEdge("starbucks", "max fashion", 32)
g.addEdge("starbucks", "h&m", 7)
g.addEdge("h&m", "starbucks", 7)
g.addEdge("h&m", "samsung", 12)
g.addEdge("samsung", "h&m", 12)
g.addEdge("samsung", "uniqlo", 20)
g.addEdge("uniqlo", "samsung", 20)
g.addEdge("uniqlo", "miniso", 25)
g.addEdge("miniso", "uniqlo", 25)
g.addEdge("miniso", "the gourmet", 31)
g.addEdge("the gourmet", "miniso", 31)
g.addEdge("the gourmet", "eskalator g1", 5)
g.addEdge("eskalator g1", "the gourmet", 5)
g.addEdge("eskalator g1", "eskalator 11", 27)
g.addEdge("eskalator 11", "eskalator g1", 27)
g.addEdge("kkv", "eskalator 11", 5)
g.addEdge("eskalator 11", "kkv", 5)

places = {
    "max fashion": {
        "lvl": 0,
        "lat": -7.275760544619828,
        "lon": 112.78073383888068
    },
    "starbucks": {
        "lvl": 0,
        "lat": -7.276125502559864,
        "lon": 112.78065470125432
    },
    "h&m": {
        "lvl": 0,
        "lat": -7.276210888903719,
        "lon": 112.78063387556341
    },
    "samsung": {
        "lvl": 0,
        "lat": -7.27635824916716,
        "lon": 112.78058805904277
    },
    "uniqlo": {
        "lvl": 0,
        "lat": -7.276370643953641,
        "lon": 112.78037008347354
    },
    "miniso": {
        "lvl": 0,
        "lat": -7.276060774192601,
        "lon": 112.78045893975707
    },
    "the gourmet": {
        "lvl": 0,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "eskalator g1": {
        "lvl": 0,
        "lat": -7.275735431786899,
        "lon": 112.78065697106541
    },
    "eskalator 11": {
        "lvl": 1,
        "lat": -7.275735431786899,
        "lon": 112.78065697106541
    },
    "kkv": {
        "lvl": 1,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    }
}
#################################################################################
app = Flask(__name__)

polylineCoordinates = []
rute = [[] for _ in range(3)]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json.get('data')  # Ambil data dari permintaan POST
    # Pastikan data adalah list dengan dua elemen
    if len(data) == 2:
        global polylineCoordinates, rute
        rute = [[] for _ in range(3)]
        polylineCoordinates = [
            [-7.275656970435648, 112.78073720330701],
            [-7.275861870602128, 112.78094966850989] 
        ];
        data1, data2 = data
        data1 = data1.lower()
        data2 = data2.lower()
        
        path = g.dijkstra(data1, data2)

        print(path)
        
        for place in path:
            print(places[place]["lvl"])
            rute[places[place]["lvl"]].append([places[place]["lat"], places[place]["lon"]])
        
        print("ini rute", rute)
        
        return jsonify(rute)
    else:
        return "Data yang diterima tidak sesuai"
    


if __name__ == '__main__':
    app.run()
