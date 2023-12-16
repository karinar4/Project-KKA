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

    def removeEdge(self, start, end):
        if start in self.graph and end in self.graph[start]:
            del self.graph[start][end]
            print(f"Edge removed")
        else:
            print(f"Edge not found")

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
                return distance, path[::-1] 

            if current_vertex in self.graph:
                for next_vertex, weight in self.graph[current_vertex].items():
                    print(current_vertex, next_vertex)
                    if not visited[next_vertex]:
                        if (current_distance + weight < distance[next_vertex]):
                            distance[next_vertex] = current_distance + weight
                            came_from[next_vertex] = current_vertex
                            heapq.heappush(queue, (distance[next_vertex], next_vertex))

        return distance, None

g = Graph() # Create an instance of the Graph class

# Add vertices
#---------------------- Lantai G ----------------------#
g.addVertex("h&m lantai g")
g.addVertex("djournal coffee bar")
g.addVertex("starbucks reserve")
g.addVertex("marks & spencer")
g.addVertex("pandora")
g.addVertex("frank&co")
g.addVertex("tumi")
g.addVertex("pintu keluar 10")
g.addVertex("elemis")
g.addVertex("miss mondial")
g.addVertex("sociolla")
g.addVertex("ling's sister jewellery")
g.addVertex("eskalator g1 1") 
g.addVertex("eskalator g1 2")
g.addVertex("eskalator g1 3")
g.addVertex("melissa clube")
g.addVertex("adelle jewellery")
g.addVertex("timberland")
g.addVertex("hyundai")
g.addVertex("elevatione")
g.addVertex("max fashion")
g.addVertex("the gourmet")
g.addVertex("pintu keluar 9")
g.addVertex("lift g") 
g.addVertex("marquine")
g.addVertex("axel vinesse")
g.addVertex("kopi kenangan")
g.addVertex("pintu keluar x") 
g.addVertex("venchi")
g.addVertex("loccitane") 
g.addVertex("toilet g")

#---------------------- Lantai 1 ----------------------#
g.addVertex("eskalator 1g 1") 
g.addVertex("eskalator 1g 2") 
g.addVertex("eskalator 1g 3") 
g.addVertex("lift 1")
g.addVertex("uniqlo")
g.addVertex("amarissa")
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
g.addVertex("parkiran")
g.addVertex("dr. specs")
g.addVertex("stop n go")
g.addVertex("levi's")
g.addVertex("watch club")
g.addVertex("polo")
g.addVertex("glam on")
g.addVertex("fossil")
g.addVertex("optik seis signature")
g.addVertex("owl optical")
g.addVertex("zeiss vision center")
g.addVertex("lift 12") 

#---------------------- Lantai 2 ----------------------#
g.addVertex("home & living")
g.addVertex("malinda furniture gallery")
g.addVertex("vivere")
g.addVertex("idemu")
g.addVertex("payless shoes")
g.addVertex("padre")
g.addVertex("iuiga")
g.addVertex("urban republic")
g.addVertex("vans")
g.addVertex("asics")
g.addVertex("the athlete's foot")
g.addVertex("puma")
g.addVertex("new era")
g.addVertex("the north face")
g.addVertex("hoops")
g.addVertex("seek")
g.addVertex("kkv lantai 2")
g.addVertex("lao fook")
g.addVertex("pan & co")
g.addVertex("planet sports asia")
g.addVertex("converse")
g.addVertex("crocs")
g.addVertex("tucano's")
g.addVertex("adidas")
g.addVertex("wee nam kee")
g.addVertex("fila")

#---------------------- Lantai 3 ----------------------#
g.addVertex("jiggle jungle")
g.addVertex("reformed exodus community")
g.addVertex("magal korean bbq")
g.addVertex("saga japanese restaurant")
g.addVertex("lincafe")
g.addVertex("boncafe")
g.addVertex("natural farm")
g.addVertex("shinjuku")
g.addVertex("mi store")
g.addVertex("guardian plus")
g.addVertex("vlife medical")
g.addVertex("huawei")
g.addVertex("oppo")
g.addVertex("house of david")
g.addVertex("scoop ideas")
g.addVertex("maison feerie")
g.addVertex("pure clinic")
g.addVertex("puro clinic")
g.addVertex("justice")
g.addVertex("samsung")
g.addVertex("willio")
g.addVertex("gingersnaps")
g.addVertex("mothercare")
g.addVertex("watsons gm3")
g.addVertex("nona manis")

#---------------------- Lantai 4 ----------------------#
g.addVertex("timezone gm3")
g.addVertex("atm bca gm3")
g.addVertex("bakmi gm")
g.addVertex("fusia")
g.addVertex("ichiban sushi")
g.addVertex("steak 21")
g.addVertex("food court")
g.addVertex("poke theory")
g.addVertex("burger king")
g.addVertex("crunchaus")
g.addVertex("jack & john")
g.addVertex("international christian assembly")
g.addVertex("shaburi & kintan")

# Add edges with weights
#---------------------- Lantai G ----------------------#
g.addEdge("h&m lantai g", "djournal coffee bar", 29)
g.addEdge("djournal coffee bar", "h&m lantai g", 29)
g.addEdge("h&m lantai g", "starbucks reserve", 29)
g.addEdge("starbucks reserve", "h&m lantai g", 29)
g.addEdge("djournal coffee bar", "starbucks reserve", 8)
g.addEdge("starbucks reserve", "djournal coffee bar", 8)
g.addEdge("h&m lantai g", "marks & spencer", 12)
g.addEdge("marks & spencer", "h&m lantai g", 12)
g.addEdge("marks & spencer", "pandora", 17)
g.addEdge("marks & spencer", "eskalator g1 3", 5)
g.addEdge("eskalator g1 3", "marks & spencer", 5)
g.addEdge("h&m lantai g", "eskalator g1 3", 7)
g.addEdge("eskalator g1 3", "h&m lantai g", 7)
g.addEdge("eskalator 1g 3", "eskalator g1 3", 30)
g.addEdge("eskalator g1 3", "eskalator 1g 3", 30)
g.addEdge("pandora", "marks & spencer", 17)
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
g.addEdge("eskalator g1 2", "tumi", 7)
g.addEdge("tumi", "eskalator g1 2", 7)
g.addEdge("melissa clube", "adelle jewellery", 14)
g.addEdge("adelle jewellery", "melissa clube", 14)
g.addEdge("eskalator g1 2", "elemis", 9)
g.addEdge("elemis", "eskalator g1 2", 9)
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
g.addEdge("eskalator g1 1", "timberland", 5)
g.addEdge("timberland", "eskalator g1 1", 5)
g.addEdge("max fashion", "lift g", 15)
g.addEdge("lift g", "max fashion", 15)
g.addEdge("max fashion", "eskalator g1 1", 25)
g.addEdge("eskalator g1 1", "max fashion", 25)
g.addEdge("eskalator g1 1", "eskalator 1g 1", 30)
g.addEdge("eskalator 1g 1", "eskalator g1 1", 30)
g.addEdge("pandora", "frank&co", 10)
g.addEdge("frank&co", "pandora", 10)
g.addEdge("elemis", "frank&co", 19)
g.addEdge("frank&co", "elemis", 19)
g.addEdge("marquine", "tumi", 7)
g.addEdge("tumi", "marquine", 7)
g.addEdge("marquine", "eskalator g1 2", 3)
g.addEdge("eskalator g1 2", "marquine", 3)
g.addEdge("eskalator g1 2", "eskalator 1g 2", 30)
g.addEdge("eskalator 1g 2", "eskalator g1 2", 30)
g.addEdge("marquine", "axel vinesse", 6)
g.addEdge("axel vinesse", "marquine", 6)
g.addEdge("axel vinesse", "adelle jewellery", 7)
g.addEdge("adelle jewellery", "axel vinesse", 7)
g.addEdge("adelle jewellery", "sociolla", 15)
g.addEdge("sociolla", "adelle jewellery", 15)
g.addEdge("hyundai", "max fashion", 27)
g.addEdge("max fashion", "hyundai", 27)
g.addEdge("hyundai", "the gourmet", 27)
g.addEdge("the gourmet", "hyundai", 27)
g.addEdge("max fashion", "pintu keluar x", 14)
g.addEdge("pintu keluar x", "max fashion", 14)
g.addEdge("the gourmet", "pintu keluar x", 21)
g.addEdge("pintu keluar x", "the gourmet", 21)
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
 
#---------------------- Lantai 1 ----------------------#
g.addEdge("eskalator 1g 1", "lift 1", 6)
g.addEdge("lift 1", "eskalator 1g 1", 6)
g.addEdge("uniqlo", "lift 1", 15)
g.addEdge("lift 1", "uniqlo", 15)
g.addEdge("uniqlo", "amarissa", 29)
g.addEdge("amarissa", "uniqlo", 29)
g.addEdge("uniqlo", "eskalator 1g 1", 19)
g.addEdge("eskalator 1g 1", "uniqlo", 19)
g.addEdge("amarissa", "bridges optical", 17)
g.addEdge("bridges optical", "amarissa", 17)
g.addEdge("cheskee", "bridges optical", 5)
g.addEdge("bridges optical", "cheskee", 5)
g.addEdge("colorbox", "cheskee", 5)
g.addEdge("cheskee", "colorbox", 5)
g.addEdge("colorbox", "the executive", 15)
g.addEdge("the executive", "colorbox", 15)
g.addEdge("kkv lantai 1", "urban & co", 9)
g.addEdge("urban & co", "kkv lantai 1", 9)
g.addEdge("kkv lantai 1", "koi the", 4)
g.addEdge("koi the", "kkv lantai 1", 4)
g.addEdge("koi the", "h&m lantai 1", 12)
g.addEdge("h&m lantai 1", "koi the", 12)
g.addEdge("locknlock", "miniso", 4)
g.addEdge("miniso", "locknlock", 4)
g.addEdge("miniso", "carla", 10)
g.addEdge("carla", "miniso", 10)
g.addEdge("carla", "h&m lantai 1", 11)
g.addEdge("h&m lantai 1", "carla", 11)
g.addEdge("eskalator 1g 3", "carla", 4)
g.addEdge("carla", "eskalator 1g 3", 4)
g.addEdge("stop n go", "dr. specs", 7)
g.addEdge("dr. specs", "stop n go", 7)
g.addEdge("the executive", "urban & co", 8)
g.addEdge("urban & co", "the executive", 8)
g.addEdge("levi's", "watch club", 6)
g.addEdge("watch club", "levi's", 6)
g.addEdge("watch club", "polo", 15)
g.addEdge("polo", "watch club", 15)
g.addEdge("polo", "glam on", 6)
g.addEdge("glam on", "polo", 6)
g.addEdge("glam on", "locknlock", 6)
g.addEdge("locknlock", "glam on", 6)
g.addEdge("eskalator 1g 3", "miniso", 9)
g.addEdge("miniso", "eskalator 1g 3", 9)
g.addEdge("h&m lantai 1", "lift 12", 16)
g.addEdge("lift 12", "h&m lantai 1", 16)
g.addEdge("fossil", "levi's", 5)
g.addEdge("levi's", "fossil", 5)
g.addEdge("fossil", "optik seis signature", 5)
g.addEdge("optik seis signature", "fossil", 5)
g.addEdge("optik seis signature", "owl optical", 8)
g.addEdge("owl optical", "optik seis signature", 8)
g.addEdge("eskalator 1g 2", "optik seis signature", 4)
g.addEdge("optik seis signature", "eskalator 1g 2", 4)
g.addEdge("owl optical", "zeiss vision center", 6)
g.addEdge("zeiss vision center", "owl optical", 6)
g.addEdge("eskalator 1g 2", "owl optical", 6)
g.addEdge("owl optical", "eskalator 1g 2", 6)
g.addEdge("dr. specs", "zeiss vision center", 5)
g.addEdge("zeiss vision center", "dr. specs", 5)

#---------------------- Lantai 2 ----------------------#
g.addEdge("home living", "payless shoes", 44)
g.addEdge("payless shoes", "home living", 44)
g.addEdge("payless shoes", "padre", 12)
g.addEdge("padre", "payless shoes", 12)
g.addEdge("padre", "urban republic", 24)
g.addEdge("urban republic", "padre", 24)
g.addEdge("urban republic", "vans", 12)
g.addEdge("vans", "urban republic", 12)
g.addEdge("vans", "the north face", 6)
g.addEdge("the north face", "vans", 6)
g.addEdge("the north face", "hoops", 6)
g.addEdge("hoops", "the north face", 6)
g.addEdge("hoops", "seek", 8)
g.addEdge("seek", "hoops", 8)
g.addEdge("seek", "kkv lantai 2", 10)
g.addEdge("kkv lantai 2", "kkv 2", 10)
g.addEdge("kkv lantai 2", "lao fook", 17)
g.addEdge("lao fook", "kkv lantai 2", 17)
g.addEdge("planet sports asia", "pan & co", 17)
g.addEdge("pan & co", "planet sports asia", 17)
g.addEdge("pan & co", "lao fook", 25)
g.addEdge("lao fook", "pan & co", 25)
g.addEdge("planet sports asia", "converse", 12)
g.addEdge("converse", "planet sports asia", 12)
g.addEdge("planet sports asia", "crocs", 2)
g.addEdge("crocs", "planet sports asia", 2)
g.addEdge("crocs", "tucano's", 8)
g.addEdge("tucano's", "crocs", 8)
g.addEdge("tucano's", "adidas", 12)
g.addEdge("adidas", "tucano's", 12)
g.addEdge("adidas", "wee nam kee", 18)
g.addEdge("wee nam kee", "adidas", 18)
g.addEdge("wee nam kee", "fila", 10)
g.addEdge("fila", "wee nam kee", 10)
g.addEdge("fila", "new era", 8)
g.addEdge("new era", "fila", 8)
g.addEdge("new era", "puma", 4)
g.addEdge("puma", "new era", 4)
g.addEdge("puma", "the athlete's foot", 10)
g.addEdge("the athlete's foot", "puma", 10)
g.addEdge("the athlete's foot", "asics", 6)
g.addEdge("asics", "the athlete's foot", 6)
g.addEdge("asics", "iuiga", 8)
g.addEdge("iuiga", "asics", 8)
g.addEdge("hoops", "puma", 13)
g.addEdge("puma", "hoops", 13)
g.addEdge("lao fook", "adidas", 14)
g.addEdge("adidas", "lao fook", 14)

#---------------------- Lantai 3 ----------------------#
g.addEdge("jiggle jungle", "reformed exodus community", 12)
g.addEdge("reformed exodus community", "jiggle jungle", 12)
g.addEdge("reformed exodus community", "magal korean bbq", 13)
g.addEdge("magal korean bbq", "reformed exodus community", 13)
g.addEdge("magal korean bbq", "saga japanese restaurant", 19)
g.addEdge("saga japanese restaurant", "magal korean bbq", 19)
g.addEdge("saga japanese restaurant", "lincafe", 10)
g.addEdge("lincafe", "saga japanese restaurant", 10)
g.addEdge("lincafe", "boncafe", 9)
g.addEdge("boncafe", "lincafe", 9)
g.addEdge("boncafe", "guardian plus", 11)
g.addEdge("guardian plus", "boncafe", 11)
g.addEdge("guardian plus", "vlife medical", 6)
g.addEdge("vlife medical", "guardian plus", 6)
g.addEdge("vlife medical", "huawei", 6)
g.addEdge("huawei", "vlife medical", 6)
g.addEdge("huawei", "oppo", 6)
g.addEdge("oppo", "huawei", 6)
g.addEdge("oppo", "house of david", 6)
g.addEdge("house of david", "oppo", 6)
g.addEdge("house of david", "justice", 6)
g.addEdge("justice", "house of david", 6)
g.addEdge("justice", "samsung", 9)
g.addEdge("samsung", "justice", 9)
g.addEdge("samsung", "watsons gm3", 12)
g.addEdge("watsons gm3", "samsung", 12)
g.addEdge("watsons gm3", "nona manis", 29)
g.addEdge("nona manis", "watsons gm3", 29)
g.addEdge("nona manis", "mothercare", 14)
g.addEdge("mothercare", "nona manis", 14)
g.addEdge("mothercare", "gingersnaps", 13)
g.addEdge("gingersnaps", "mothercare", 13)
g.addEdge("gingersnaps", "willio", 8)
g.addEdge("willio", "gingersnaps", 8)
g.addEdge("willio", "puro clinic", 8)
g.addEdge("puro clinic", "willio", 8)
g.addEdge("puro clinic", "pure clinic", 6)
g.addEdge("pure clinic", "puro clinic", 6)
g.addEdge("pure clinic", "maison feerie", 8)
g.addEdge("maison feerie", "pure clinic", 8)
g.addEdge("maison feerie", "scoop ideas", 6)
g.addEdge("scoop ideas", "maison feerie", 6)
g.addEdge("scoop ideas", "mi store", 7)
g.addEdge("mi store", "scoop ideas", 7)
g.addEdge("mi store", "shinjuku", 23)
g.addEdge("shinjuku", "mi store", 23)
g.addEdge("shinjuku", "natural farm", 7)
g.addEdge("natural farm", "shinjuku", 7)
g.addEdge("natural farm", "jiggle jungle", 28)
g.addEdge("jiggle jungle", "natural farm", 28)
g.addEdge("mi store", "boncafe", 15)
g.addEdge("boncafe", "mi store", 15)
g.addEdge("pure clinic", "house of david", 13)
g.addEdge("house of david", "pure clinic", 13)

#---------------------- Lantai 4 ----------------------#

places = {
    # Lantai G
    "h&m lantai g": {
        "lvl": 0,
        "lat": -7.27611653269939,
        "lon": 112.7805770422953
    },
    "djournal coffe bar": { 
        "lvl": 0,
        "lat": -7.2757956141528695,
        "lon": 112.78075311626509
    },
    "starbucks reserve": { 
        "lvl": 0,
        "lat": -7.275835899256407,
        "lon": 112.78080591201103
    },
    "marks & spencer": { 
        "lvl": 0,
        "lat": -7.276106138078035,
        "lon": 112.7804930116227
    },
    "pandora": { 
        "lvl": 0,
        "lat": -7.276370083709992,
        "lon": 112.78046562730117
    },
    "frank&co": { 
        "lvl": 0,
        "lat": -7.276383488317819,
        "lon": 112.78054866202376
    },
    "tumi": { 
        "lvl": 0,
        "lat": -7.276425146770151,
        "lon": 112.78046238347974
    },
    "pintu keluar 10": { 
        "lvl": 0,
        "lat": -7.276483312236508,
        "lon": 112.7807051567325
    },
    "elemis": { 
        "lvl": 0,
        "lat": -7.276591916555589,
        "lon": 112.78057279021732
    },
    "miss mondial": { 
        "lvl": 0,
        "lat": -7.276643002486139,
        "lon": 112.78056654417276
    },
    "sociolla": {
        "lvl": 0,
        "lat": -7.276772608642432,
        "lon": 112.78045604842669
    },
    "ling's sister jewellery": { 
        "lvl": 0,
        "lat": -7.276702077590642,
        "lon": 112.7805381854883
    },
    "melissa clube": { 
        "lvl": 0,
        "lat": -7.276728635983375,
        "lon": 112.78023240394253
    },
    "adelle jewellery": { 
        "lvl": 0,
        "lat": -7.2767093976786015,
        "lon": 112.78031664144987
    },
    "timberland": {
        "lvl": 0,
        "lat": -7.2767412558671225,
        "lon": 112.78017024276835
    },
    "hyundai": { 
        "lvl": 0,
        "lat": -7.276839263099518,
        "lon": 112.78009735161282
    },
    "elevatione": { 
        "lvl": 0,
        "lat": -7.276813954903375,
        "lon": 112.78026235408043
    },
    "max fashion": { 
        "lvl": 0,
        "lat": -7.276810819372429,
        "lon": 112.77987295695544
    },
    "the gourmet": { 
        "lvl": 0,
        "lat": -7.276988806491687,
        "lon": 112.77989553323062
    },
    "pintu keluar 9": { 
        "lvl": 0,
        "lat": -7.277096814789843,
        "lon": 112.7799339154763
    },
    "lift g": {
        "lvl": 0,
        "lat": -7.276691800599139,
        "lon": 112.77999851778367
    },
    "marquine": {
        "lvl": 0,
        "lat": -7.276509883129208,
        "lon": 112.78043047837997
    },
    "axel vinesse": { 
        "lvl": 0,
        "lat": -7.276588926582775,
        "lon": 112.78037040799222
    },
    "kopi kenangan": { 
        "lvl": 0,
        "lat": -7.276951423634216,
        "lon": 112.77996441591858
    },
    "pintu keluar x": { 
        "lvl": 0,
        "lat": -7.2766511406737635,
        "lon": 112.77988547319165
    },
    "venchi": { 
        "lvl": 0,
        "lat": -7.276545594141922,
        "lon": 112.78057442361171
    },
    "loccitane": { 
        "lvl": 0,
        "lat": -7.2767932820116386,
        "lon": 112.78036900966748
    },
    "toilet g": { 
        "lvl": 0,
        "lat": -7.27631967552702,
        "lon": 112.78029433310826
    },
    "eskalator g1 2": {
        "lvl": 0,
        "lat": -7.276515355642729,
        "lon": 112.78046920020836
    },
    "eskalator g1 1": {
        "lvl": 0,
        "lat": -7.276751434411366,
        "lon": 112.78006785734948
    },
    "eskalator g1 3": {
        "lvl": 0,
        "lat": -7.276035075100978,
        "lon": 112.78052649408858
    },
    # Lantai 1
    "lift 1": { 
        "lvl": 1,
        "lat": -7.2766917399328435,
        "lon": 112.77999134403416
    },
    "uniqlo": { 
        "lvl": 1,
        "lat": -7.276841158338485,
        "lon": 112.77986302821762
    },
    "amarissa": {
        "lvl": 1,
        "lat": -7.276846146822336,
        "lon": 112.78009455237975
    },
    "bridges optical": { 
        "lvl": 1,
        "lat": -7.276799409539052,
        "lon": 112.78032508801687
    },
    "cheskee": { 
        "lvl": 1,
        "lat": -7.27679106359534,
        "lon": 112.78038061849804
    },
    "colorbox": { 
        "lvl": 1,
        "lat": -7.276762926183579,
        "lon": 112.7804621981461
    },
    "the executive": { 
        "lvl": 1,
        "lat": -7.27660579511398,
        "lon": 112.78058161415652
    },
    "kkv lantai 1": { 
        "lvl": 1,
        "lat": -7.276296664316362,
        "lon": 112.7805859614005
    },
    "urban & co": { 
        "lvl": 1,
        "lat": -7.276518604056193,
        "lon": 112.78055963941671
    },
    "koi the": { 
        "lvl": 1,
        "lat": -7.27607649716299,
        "lon": 112.78061891360471
    },
    "h&m lantai 1": { 
        "lvl": 1,
        "lat": -7.275951510046681,
        "lon": 112.78064411395263
    },
    "locknlock": { 
        "lvl": 1,
        "lat": -7.276079621840211,
        "lon": 112.78049921195407
    },
    "miniso": { 
        "lvl": 1,
        "lat": -7.275995255540906,
        "lon": 112.78049291186562
    },
    "carla": { 
        "lvl": 1,
        "lat": -7.275917138583381,
        "lon": 112.78054961264974
    },
    "parkiran": {
        "lvl": 1,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "dr. specs": { 
        "lvl": 1,
        "lat": -7.276713875996165,
        "lon": 112.78015313354086
    },
    "stop n go": { 
        "lvl": 1,
        "lat": -7.276716977931656,
        "lon": 112.78006212326454
    },
    "levi's": { 
        "lvl": 1,
        "lat": -7.276422201208618,
        "lon": 112.78045167404906
    },
    "watch club": { 
        "lvl": 1,
        "lat": -7.276361270040056,
        "lon": 112.78045797413552
    },
    "polo": { 
        "lvl": 1,
        "lat": -7.276211285591501,
        "lon": 112.78048002444109
    },
    "glam on": { 
        "lvl": 1,
        "lat": -7.276146802400476,
        "lon": 112.78048818680031
    },
    "fossil": { 
        "lvl": 1,
        "lat": -7.276500592181279,
        "lon": 112.78040251334335
    },
    "optik seis signature": { 
        "lvl": 1,
        "lat": -7.276570561245791,
        "lon": 112.78035928044892
    },
    "owl optical": { 
        "lvl": 1,
        "lat": -7.27668905790415,
        "lon": 112.78030580843375
    },
    "zeiss vision center": { 
        "lvl": 1,
        "lat": -7.276701912521091,
        "lon": 112.78022973036184
    },
    "lift 12": { 
        "lvl": 1,
        "lat": -7.27606243611379,
        "lon": 112.7807512154323
    },
    "eskalator 1g 2": {
        "lvl": 1,
        "lat": -7.276629602880476,
        "lon": 112.78036674841582
    },
    "eskalator 1g 1": {
        "lvl": 1,
        "lat": -7.27676952608293,
        "lon": 112.77995343637633
    },
    "eskalator 1g 3": {
        "lvl": 1,
        "lat": -7.275922284219092,
        "lon": 112.78054357264517
    },
    # Lantai 2
    "home & living": { 
        "lvl": 2,
        "lat": -7.27686304908741,
        "lon": 112.77971581434093
    },
    "malinda furniture gallery": {
        "lvl": 2,
        "lat": -7.27686304908741,
        "lon": 112.77971581434093
    },
    "vivere": {
        "lvl": 2,
        "lat": -7.27686304908741,
        "lon": 112.77971581434093
    },
    "idemu": {
        "lvl": 2,
        "lat": -7.27686304908741,
        "lon": 112.77971581434093
    },
    "payless shoes": {
        "lvl": 2,
        "lat": -7.276849722081877,
        "lon": 112.78018659780525
    },
    "padre": {
        "lvl": 2,
        "lat": -7.276831475385919,
        "lon": 112.78031268588614
    },
    "iuiga": {
        "lvl": 2,
        "lat": -7.2766531545685496,
        "lon": 112.78033060327579
    },
    "urban republic": {
        "lvl": 2,
        "lat": -7.276728581887198,
        "lon": 112.78055675557425
    },
    "vans": {
        "lvl": 2,
        "lat": -7.2765962353408895,
        "lon": 112.7805921367094
    },
    "asics": {
        "lvl": 2,
        "lat": -7.276560812400547,
        "lon": 112.78035107084827
    },
    "the athlete's foot": {
        "lvl": 2,
        "lat": -7.276501629656153,
        "lon": 112.7803957800129
    },
    "puma": {
        "lvl": 2,
        "lat": -7.276435278266959,
        "lon": 112.78043585463121
    },
    "new era": {
        "lvl": 2,
        "lat": -7.276377300060403,
        "lon": 112.78044509115921
    },
    "the north face": {
        "lvl": 2,
        "lat": -7.276538063601805,
        "lon": 112.78057310077452
    },
    "hoops": {
        "lvl": 2,
        "lat": -7.276453547076528,
        "lon": 112.78057215407802
    },
    "seek": {
        "lvl": 2,
        "lat": -7.276385934262834,
        "lon": 112.7805844600353
    },
    "kkv lantai 2": {
        "lvl": 2,
        "lat": -7.276281697174923,
        "lon": 112.78059866040945
    },
    "lao fook": {
        "lvl": 2,
        "lat": -7.276122976946809,
        "lon": 112.78062793827587
    },
    "pan & co": {
        "lvl": 2,
        "lat": -7.276052052578919,
        "lon": 112.78084782542004
    },
    "planet sports asia": {
        "lvl": 2,
        "lat": -7.276030683000869,
        "lon": 112.78067189048073
    },
    "converse": {
        "lvl": 2,
        "lat": -7.275926374273823,
        "lon": 112.78062932669417
    },
    "crocs": {
        "lvl": 2,
        "lat": -7.275917925521014,
        "lon": 112.78061051958917
    },
    "tucano's": {
        "lvl": 2,
        "lat": -7.275912415434632,
        "lon": 112.78052379564468
    },
    "adidas": {
        "lvl": 2,
        "lat": -7.27602351913221,
        "lon": 112.78048049775208
    },
    "wee nam kee": {
        "lvl": 2,
        "lat": -7.276190587163782,
        "lon": 112.78047191131486
    },
    "fila": {
        "lvl": 2,
        "lat": -7.276298731720942,
        "lon": 112.78045581594648
    },
    # Lantai 3
    "jiggle jungle": {
        "lvl": 3,
        "lat": -7.276814401852491,
        "lon": 112.77979982294897
    },
    "reformed exodus community": {
        "lvl": 3,
        "lat": -7.276931960161235,
        "lon": 112.77984669743574
    },
    "magal korean bbq": {
        "lvl": 3,
        "lat": -7.276907395741603,
        "lon": 112.7799961651383
    },
    "saga japanese restaurant": {
        "lvl": 3,
        "lat": -7.276831051529271,
        "lon": 112.78019336245194
    },
    "lincafe": {
        "lvl": 3,
        "lat": -7.276816137413817,
        "lon": 112.7803516743981
    },
    "boncafe": {
        "lvl": 3,
        "lat": -7.276788941159026,
        "lon": 112.78045161394346
    },
    "natural farm": {
        "lvl": 3,
        "lat": -7.276698499333264,
        "lon": 112.78008983249782
    },
    "shinjuku": {
        "lvl": 3,
        "lat": -7.276700140659415,
        "lon": 112.78015436394423
    },
    "mi store": {
        "lvl": 3,
        "lat": -7.276632102832224,
        "lon": 112.78032362119336
    },
    "guardian plus": {
        "lvl": 3,
        "lat": -7.276718757074988,
        "lon": 112.780545362917
    },
    "vlife medical": {
        "lvl": 3,
        "lat": -7.276657346027477,
        "lon": 112.78057366448189
    },
    "huawei": {
        "lvl": 3,
        "lat": -7.276587948550514,
        "lon": 112.78058368864305
    },
    "oppo": {
        "lvl": 3,
        "lat": -7.276521306986368,
        "lon": 112.78059319299018
    },
    "house of david": {
        "lvl": 3,
        "lat": -7.276450787084471,
        "lon": 112.78060258255806
    },
    "scoop ideas": {
        "lvl": 3,
        "lat": -7.276546753862036,
        "lon": 112.78034347702385
    },
    "maison feerie": {
        "lvl": 3,
        "lat": -7.276499155389459,
        "lon": 112.78038649798867
    },
    "pure clinic": {
        "lvl": 3,
        "lat": -7.276440067623824,
        "lon": 112.7804278643008
    },
    "puro clinic": {
        "lvl": 3,
        "lat": -7.276376055869875,
        "lon": 112.78043779221525
    },
    "justice": {
        "lvl": 3,
        "lat": -7.276384258865448,
        "lon": 112.78061465486007
    },
    "samsung": {
        "lvl": 3,
        "lat": -7.27628712764691,
        "lon": 112.78062538579496
    },
    "willio": {
        "lvl": 3,
        "lat": -7.27630219614133,
        "lon": 112.7804477201297
    },
    "gingersnaps": {
        "lvl": 3,
        "lat": -7.276213564452547,
        "lon": 112.78045930269843
    },
    "mothercare": {
        "lvl": 3,
        "lat": -7.276070225976127,
        "lon": 112.78048202671278
    },
    "watsons gm3": {
        "lvl": 3,
        "lat": -7.276164715671527,
        "lon": 112.78064282356365
    },
    "nona manis": {
        "lvl": 3,
        "lat": -7.275918541496296,
        "lon": 112.78051537392577
    },
    # Lantai 4
    "timezone gm3": {
        "lvl": 4,
        "lat": -7,
        "lon": 112
    },
    "atm bca gm3": {
        "lvl": 4,
        "lat": -7,
        "lon": 112
    },
    "bakmi gm": {
        "lvl": 4,
        "lat": -7,
        "lon": 112
    },
    "fusia": {
        "lvl": 4,
        "lat": -7,
        "lon": 112
    },
    "ichiban sushi": {
        "lvl": 4,
        "lat": -7,
        "lon": 112
    },
    "steak 21": {
        "lvl": 4,
        "lat": -7,
        "lon": 112
    },
    "food court": {
        "lvl": 4,
        "lat": -7,
        "lon": 112
    },
    "poke theory": {
        "lvl": 4,
        "lat": -7,
        "lon": 112
    },
    "burger king": {
        "lvl": 4,
        "lat": -7,
        "lon": 112
    },
    "crunchaus": {
        "lvl": 4,
        "lat": -7,
        "lon": 112
    },
    "jack & john": {
        "lvl": 4,
        "lat": -7,
        "lon": 112
    },
    "international christian assembly": {
        "lvl": 4,
        "lat": -7,
        "lon": 112
    },
    "shaburi & kintan": {
        "lvl": 4,
        "lat": -7,
        "lon": 112
    }
}
#################################################################################
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json.get('data')  # Ambil data dari permintaan POST
    # Pastikan data adalah list dengan dua elemen
    if len(data) == 2:
        rute = [[], [], []]
        goal = [[], [], []]
        data1, data2 = data
        data1 = data1.lower()
        data2 = data2.lower()
        
        dist, path = g.dijkstra(data1, data2)

        if (path is not None):
            print(path)
        
            for place in path:
                print(places[place]["lvl"])
                rute[places[place]["lvl"]].append([places[place]["lat"], places[place]["lon"]])
            
            goal[places[path[-1]]["lvl"]] = [places[path[-1]]["lat"], places[path[-1]]["lon"]]
            
        print("ini rute", rute)
        
        resp = {
            "rute": rute,
            "dur": dist[data2],
            "goal": goal,
            "path": path
        }
        return jsonify(resp)
    else:
        return "Data yang diterima tidak sesuai"
    


if __name__ == '__main__':
    app.run()
