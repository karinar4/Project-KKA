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
#BLOM TAK CEK KE DIRECTORY ASLINE
# lantai g
g.addVertex("h&m lantai g")
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

#lantai 1
g.addVertex("eskalator 11") #dari deket lantai 1 yg deket max
g.addVertex("lift 1")
g.addVertex("uniqlo")
g.addVertex("amarissa")
g.addVertex("eskalator 12") #ke lantai 2
g.addVertex("bridges eyewear")
g.addVertex("cheesecake")
g.addVertex("colorbox")
g.addVertex("the executive")
g.addVertex("kkv lantai 1")
g.addVertex("urban")
g.addVertex("koi")
g.addVertex("h&m lantai 1")
g.addVertex("locknlock")
g.addVertex("miniso")
g.addVertex("carla")
g.addVertex("parkiran") #?? gamudeng
g.addVertex("eskalator 13") #eskalator deket miniso
g.addVertex("spec")
g.addVertex("stopngo")
g.addVertex("levis")
g.addVertex("watchclub")
g.addVertex("polo")
g.addVertex("glamon")

# Add edges with weights
#lantai 1
g.addEdge("h&m lantai g", "djournal", 29)
g.addEdge("djournal", "h&m lantai g", 29)
g.addEdge("h&m lantai g", "starbuck", 29)
g.addEdge("starbuck", "h&m lantai g", 29)
g.addEdge("djournal", "starbuck", 8)
g.addEdge("starbuck", "djournal", 8)
g.addEdge("h&m lantai g", "mark&spencer", 12)
g.addEdge("mark&spencer", "h&m lantai g", 12)
g.addEdge("mark&spencer", "pandora", 17)
g.addEdge("pandora", "mark&spencer", 17)
g.addEdge("h&m lantai g", "frank&co", 18)
g.addEdge("frank&co", "h&m lantai g", 18)
g.addEdge("pandora", "tumi", 6)
g.addEdge("tumi", "pandora", 6)
g.addEdge("pintu keluar 10", "tumi", 23)
g.addEdge("tumi", "pintu keluar 10", 23)
g.addEdge("elemis", "mondial", 6)
g.addEdge("mondial", "elemis", 6)
g.addEdge("sociolla", "lings", 6)
g.addEdge("lings", "sociolla", 6)
g.addEdge("mondial", "lings", 5)
g.addEdge("lings", "mondial", 5)
g.addEdge("eskalator g2", "tumi", 7)
g.addEdge("tumi", "eskalator g2", 7)
g.addEdge("melisa", "adele", 14)
g.addEdge("adele", "melisa", 14)
g.addEdge("eskalator g2", "elemis", 9)
g.addEdge("elemis", "eskalator g2", 9)
g.addEdge("melisa", "timberland", 7)
g.addEdge("timberland", "melisa", 7)
g.addEdge("timberland", "hyundai", 11)
g.addEdge("hyundai", "timberland", 11)
g.addEdge("hyundai", "elevatione", 7)
g.addEdge("elevatione", "hyundai", 7)
g.addEdge("max fashion", "the gourmet", 4)
g.addEdge("the gourmet", "max fashion", 4)
g.addEdge("the gourmet", "pintu keluar 9", 19)
g.addEdge("pintu keluar 9", "the gourmet", 19)
g.addEdge("eskalator g3", "timberland", 5)
g.addEdge("timberland", "eskalator g3", 5)
g.addEdge("max fashion", "lift g", 15)
g.addEdge("lift g", "max fashion", 15)
g.addEdge("max fashion", "eskalator g3", 25)
g.addEdge("eskalator g3", "max fashion", 25)
g.addEdge("pandora", "frank&co", 10)
g.addEdge("frank&co", "pandora", 10)
g.addEdge("elemis", "frank&co", 19)
g.addEdge("frank&co", "elemis", 19)
g.addEdge("marquine", "tumi", 7)
g.addEdge("tumi", "marquine", 7)
g.addEdge("marquine", "eskalator g2", 3)
g.addEdge("eskalator g2", "marquine", 3)
g.addEdge("marquine", "axel", 6)
g.addEdge("axel", "marquine", 6)
g.addEdge("axel", "adele", 7)
g.addEdge("adele", "axel", 7)
g.addEdge("adele", "sociolla", 15)
g.addEdge("sociolla", "adele", 15)
g.addEdge("sociolla", "elevatione", 17)
g.addEdge("elevatione", "sociolla", 17)
g.addEdge("hyundai", "max fashion", 27)
g.addEdge("max fashion", "hyundai", 27)
g.addEdge("hyundai", "the gourmet", 27)
g.addEdge("the gourmet", "hyundai", 27)
g.addEdge("max fashion", "pintu keluar x", 14)
g.addEdge("pintu keluar x", "max fashion", 14)
g.addEdge("the gourmet", "pintu keluar x", 21)
g.addEdge("pintu keluar x", "the gourmet", 21)
g.addEdge("max fashion", "eskalator g3", 25)
g.addEdge("eskalator g3", "max fashion", 25)
g.addEdge("hyundai", "kopi kenangan", 16)
g.addEdge("kopi kenangan", "hyundai", 16)

#lantai 2


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
