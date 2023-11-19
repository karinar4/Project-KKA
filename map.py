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
g.addVertex("djournal coffee bar")
g.addVertex("starbucks reserve")
g.addVertex("mark & spencer")
g.addVertex("pandora")
g.addVertex("frank&co")
g.addVertex("tumi")
g.addVertex("pintu keluar 10")
g.addVertex("elemis")
g.addVertex("miss mondial")
g.addVertex("sociolla")
g.addVertex("ling's sister jewelery")
g.addVertex("eskalator g1") #deket h&m
g.addVertex("eskalator g2") #eska tengah lobby
g.addVertex("melissa clube")
g.addVertex("adelle jewelerry")
g.addVertex("timberland")
g.addVertex("hyundai")
g.addVertex("elevatione")
g.addVertex("max fashion")
g.addVertex("the gourmet")
g.addVertex("pintu keluar 9")
g.addVertex("lift g")
g.addVertex("eskalator g3") #deket gourmet
g.addVertex("marquine")
g.addVertex("axel vinesse")
g.addVertex("kopi kenangan")
g.addVertex("pintu keluar x") #aku ga tau ini pintu keluar no berapa
g.addVertex("venchi") #INI BARU
g.addVertex("loccitane") #INI JUGA BARU

#lantai 1
g.addVertex("eskalator 11") #dari deket lantai 1 yg deket max
g.addVertex("lift 1") #ini yg terusan dari lift g
g.addVertex("uniqlo")
g.addVertex("amarissa")
g.addVertex("eskalator 12") #ke lantai 2
g.addVertex("bridges optical")
g.addVertex("cheskee")
g.addVertex("colorbox")
g.addVertex("the executive")
g.addVertex("kkv lantai 1")
g.addVertex("urban & co")
g.addVertex("koi the")
g.addVertex("h&m lantai 1")
g.addVertex("locknlock")
g.addVertex("miniso")
g.addVertex("carla")
g.addVertex("parkiran") #?? gamudeng
g.addVertex("eskalator 13") #eskalator deket miniso
g.addVertex("dr. specs")
g.addVertex("stop n go")
g.addVertex("levi's")
g.addVertex("watch club")
g.addVertex("polo")
g.addVertex("glamon")
g.addVertex("fossil")
g.addVertex("optik seis signature")
g.addVertex("owl optical")
g.addVertex("zeiss vision center")
g.addVertex("lift 12") #INI lift yg tembusnya ke dalem h&m nek ga salah

# Add edges with weights
#lantai 1
g.addEdge("h&m lantai g", "djournal coffee bar", 29)
g.addEdge("djournal coffee bar", "h&m lantai g", 29)
g.addEdge("h&m lantai g", "starbucks reserve", 29)
g.addEdge("starbucks reserve", "h&m lantai g", 29)
g.addEdge("djournal coffee bar", "starbucks reserve", 8)
g.addEdge("starbucks reserve", "djournal coffee bar", 8)
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
g.addEdge("elemis", "miss mondial", 6)
g.addEdge("miss mondial", "elemis", 6)
g.addEdge("sociolla", "ling's sister jewellery", 6)
g.addEdge("ling's sister jewellery", "sociolla", 6)
g.addEdge("miss mondial", "ling's sister jewellery", 5)
g.addEdge("ling's sister jewellery", "miss mondial", 5)
g.addEdge("eskalator g2", "tumi", 7)
g.addEdge("tumi", "eskalator g2", 7)
g.addEdge("melissa clube", "adelle jewelerry", 14)
g.addEdge("adelle jewelerry", "melissa clube", 14)
g.addEdge("eskalator g2", "elemis", 9)
g.addEdge("elemis", "eskalator g2", 9)
g.addEdge("melissa clube", "timberland", 7)
g.addEdge("timberland", "melissa clube", 7)
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
g.addEdge("marquine", "axel vinesse", 6)
g.addEdge("axel vinesse", "marquine", 6)
g.addEdge("axel vinesse", "adelle jewelerry", 7)
g.addEdge("adelle jewelerry", "axel vinesse", 7)
g.addEdge("adelle jewelerry", "sociolla", 15)
g.addEdge("sociolla", "adelle jewelerry", 15)
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
g.addEdge("venchi", "elemis", 9)
g.addEdge("elemis", "venchi", 9)
g.addEdge("venchi", "frank&co", 18)
g.addEdge("frank&co", "venchi", 18)
g.addEdge("loccitane", "sociolla", 8)
g.addEdge("sociolla", "loccitane", 8)
g.addEdge("elevatione", "loccitane", 9)
g.addEdge("loccitane", "elevatione", 9)
 


#lantai 2
g.addEdge("eskalator 11","lift 1",6)
g.addEdge("lift 1","eskalator 11",6)
g.addEdge("uniqlo","lift 1",15)
g.addEdge("lift 1","uniqlo",15)
g.addEdge("uniqlo","amarissa", 29)
g.addEdge("amarissa","uniqlo", 29)
g.addEdge("uniqlo","eskalator 12",19)
g.addEdge("eskalator 12","uniqlo",19)
g.addEdge("amarissa","bridges optical", 17)
g.addEdge("bridges optical","amarissa", 17)
g.addEdge("cheskee","bridges optical",5)
g.addEdge("bridges optical","cheskee",5)
g.addEdge("colorbox","cheskee",5)
g.addEdge("cheskee","colorbox",5)
g.addEdge("colorbox","the executive",15)
g.addEdge("the executive","colorbox",15)
g.addEdge("kkv lantai 1","urban & co", 9)
g.addEdge("urban & co","kkv lantai 1", 9)
g.addEdge("kkv lantai 1","koi the",4)
g.addEdge("koi the","kkv lantai 1",4)
g.addEdge("koi the","h&m lantai 1",12)
g.addEdge("h&m lantai 1","koi the",12)
g.addEdge("locknlock","miniso",4)
g.addEdge("miniso","locknlock",4)
g.addEdge("miniso","carla",10)
g.addEdge("carla","miniso",10)
g.addEdge("carla","h&m lantai 1",11)
g.addEdge("h&m lantai 1","carla",11)
g.addEdge("eskalator 13","carla", 4)
g.addEdge("carla","eskalator 13", 4)
g.addEdge("stop n go","dr. specs",7)
g.addEdge("dr. specs","stop n go",7)
g.addEdge("the executive","urban & co",8)
g.addEdge("urban & co","the executive",8)
g.addEdge("levi's","watch club",6)
g.addEdge("watch club","levi's",6)
g.addEdge("watch club","polo",15)
g.addEdge("polo","watch club",15)
g.addEdge("polo","glam on",6)
g.addEdge("glam on","polo",6)
g.addEdge("glam on","locknlock",6)
g.addEdge("locknlock","glam on",6)
g.addEdge("eskalator 23","miniso",9)
g.addEdge("miniso","eskalator 23",9)
g.addEdge("h&m lantai 1","lift 12", 16)
g.addEdge("lift 12","h&m lantai 1",16)

places = {
    "h&m lantai g": {
        "lvl": 0,
        "lat": -7.275760544619828,
        "lon": 112.78073383888068
    },
    "djournal coffe bar": {
        "lvl": 0,
        "lat": -7.276125502559864,
        "lon": 112.78065470125432
    },
    "starbucks reserve": {
        "lvl": 0,
        "lat": -7.276210888903719,
        "lon": 112.78063387556341
    },
    "mark & spencer": {
        "lvl": 0,
        "lat": -7.27635824916716,
        "lon": 112.78058805904277
    },
    "pandora": {
        "lvl": 0,
        "lat": -7.276370643953641,
        "lon": 112.78037008347354
    },
    "frank&co": {
        "lvl": 0,
        "lat": -7.276060774192601,
        "lon": 112.78045893975707
    },
    "tumi": {
        "lvl": 0,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "pintu keluar 10": {
        "lvl": 0,
        "lat": -7.275735431786899,
        "lon": 112.78065697106541
    },
    "elemis": {
        "lvl": 0,
        "lat": -7.275735431786899,
        "lon": 112.78065697106541
    },
    "miss mondial": {
        "lvl": 0,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "sociolla": {
        "lvl": 0,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "ling's sister jewelerry": {
        "lvl": 0,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "eskalator g1": {
        "lvl": 0,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "eskalator g2": {
        "lvl": 0,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "melissa clube": {
        "lvl": 0,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "adelle jewelerry": {
        "lvl": 0,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "timberland": {
        "lvl": 0,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "hyundai": {
        "lvl": 0,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "elevatione": {
        "lvl": 0,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "max fashion": {
        "lvl": 0,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "the gourmet": {
        "lvl": 0,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "pintu keluar 9": {
        "lvl": 0,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "lift g": {
        "lvl": 0,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "eskalator g3": {
        "lvl": 0,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "marquine": {
        "lvl": 0,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "axel vinesse": {
        "lvl": 0,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "kopi kenangan": {
        "lvl": 0,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "pintu keluar x": {
        "lvl": 0,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "venchi": {
        "lvl": 0,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "loccitane": {
        "lvl": 0,
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
