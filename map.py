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

    def getWeight(self, start, end):
        return self.graph[start][end]

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
g.addVertex("lift g 1") 
g.addVertex("lift g 2") 
g.addVertex("marquine")
g.addVertex("axel vinesse")
g.addVertex("kopi kenangan")
g.addVertex("pintu keluar x") 
g.addVertex("venchi")
g.addVertex("loccitane") 
g.addVertex("toilet g")
g.addVertex("x")

#---------------------- Lantai 1 ----------------------#
g.addVertex("eskalator 1g 1") 
g.addVertex("eskalator 1g 2") 
g.addVertex("eskalator 1g 3") 
g.addVertex("eskalator 12 1") 
g.addVertex("eskalator 12 2") 
g.addVertex("eskalator 12 3")
g.addVertex("lift 1 1")
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
g.addVertex("lift 1 2") 
g.addVertex("y")
g.addVertex("a")
g.addVertex("b")
g.addVertex("aa")

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
g.addVertex("eskalator 21 1") 
g.addVertex("eskalator 21 2") 
g.addVertex("eskalator 21 3") 
g.addVertex("eskalator 23 1") 
g.addVertex("eskalator 23 2") 
g.addVertex("eskalator 23 3")
g.addVertex("lift 2 1")
g.addVertex("lift 2 2")
g.addVertex("c")
g.addVertex("d")
g.addVertex("e")
g.addVertex("f")
g.addVertex("g")
g.addVertex("h")
g.addVertex("i")
g.addVertex("j")
g.addVertex("k")
g.addVertex("l")
g.addVertex("m")
g.addVertex("n")
g.addVertex("o")
g.addVertex("cc")
g.addVertex("dd")

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
g.addVertex("eskalator 32 1") 
g.addVertex("eskalator 32 2") 
g.addVertex("eskalator 32 3") 
g.addVertex("eskalator 34 1") 
g.addVertex("eskalator 34 2") 
g.addVertex("eskalator 34 3")
g.addVertex("lift 3 1")
g.addVertex("lift 3 2")
g.addVertex("p")
g.addVertex("q")
g.addVertex("r")
g.addVertex("s")
g.addVertex("t")

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
g.addEdge("eskalator 1g 3", "eskalator g1 3", 30) #eskalator
g.addEdge("eskalator g1 3", "eskalator 1g 3", 30) #eskalator
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
g.addEdge("timberland", "x", 7)
g.addEdge("x", "timberland", 7)
g.addEdge("timberland", "hyundai", 11)
g.addEdge("hyundai", "timberland", 11)
g.addEdge("hyundai", "elevatione", 7)
g.addEdge("elevatione", "hyundai", 7)
g.addEdge("max fashion", "the gourmet", 4)
g.addEdge("the gourmet", "max fashion", 4)
g.addEdge("the gourmet", "pintu keluar 9", 19)
g.addEdge("pintu keluar 9", "the gourmet", 19)
g.addEdge("eskalator g1 1", "timberland", 10)
g.addEdge("timberland", "eskalator g1 1", 10)
g.addEdge("lift g 1", "timberland", 17)
g.addEdge("timberland", "lift g 1", 17)
g.addEdge("max fashion", "lift g 1", 15)
# g.addEdge("lift g 1", "lift 1 1", 9) # lift
# g.addEdge("lift g 2", "lift 1 2", 9) # lift
g.addEdge("lift g 1", "max fashion", 15)
g.addEdge("lift g 2", "h&m lantai g", 10)
g.addEdge("h&m lantai g", "lift g 2", 10)
g.addEdge("max fashion", "eskalator g1 1", 25)
g.addEdge("eskalator g1 1", "max fashion", 25)
g.addEdge("eskalator g1 1", "eskalator 1g 1", 30) #eskalator
g.addEdge("eskalator 1g 1", "eskalator g1 1", 30) #eskalator
g.addEdge("pandora", "frank&co", 10)
g.addEdge("frank&co", "pandora", 10)
g.addEdge("elemis", "frank&co", 19)
g.addEdge("frank&co", "elemis", 19)
g.addEdge("marquine", "tumi", 7)
g.addEdge("tumi", "marquine", 7)
g.addEdge("marquine", "eskalator g1 2", 3)
g.addEdge("eskalator g1 2", "marquine", 3)
g.addEdge("eskalator g1 2", "eskalator 1g 2", 30) #eskalator
g.addEdge("eskalator 1g 2", "eskalator g1 2", 30) #eskalator
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
g.addEdge("eskalator 1g 1", "lift 1 1", 8)
g.addEdge("lift 1 1", "eskalator 1g 1", 8)
g.addEdge("stop n go", "lift 1 1", 7)
g.addEdge("lift 1 1", "stop n go", 7)
g.addEdge("uniqlo", "lift 1 1", 18)
g.addEdge("lift 1 1", "uniqlo", 18)
# g.addEdge("lift 1 1", "lift g 1", 9) #lift
# g.addEdge("lift 1 2", "lift g 2", 9) #lift
# g.addEdge("lift 1 1", "lift 2 1", 9) #lift
# g.addEdge("lift 1 2", "lift 2 2", 9) #lift
g.addEdge("uniqlo", "amarissa", 29)
g.addEdge("amarissa", "uniqlo", 29)
g.addEdge("uniqlo", "eskalator 1g 1", 12)
g.addEdge("eskalator 1g 1", "uniqlo", 12)
g.addEdge("a", "stop n go", 11)
g.addEdge("stop n go", "a", 11)
g.addEdge("a", "uniqlo", 13)
g.addEdge("uniqlo", "a", 13)
g.addEdge("eskalator 12 1", "stop n go", 6)
g.addEdge("stop n go", "eskalator 12 1", 6)
g.addEdge("a", "eskalator 1g 1", 1)
g.addEdge("eskalator 1g 1", "a", 1)
g.addEdge("b", "a", 14)
g.addEdge("a", "b", 14)
g.addEdge("b", "eskalator 12 1", 1)
g.addEdge("eskalator 12 1", "b", 1)
g.addEdge("eskalator 1g 1", "aa", 8)
g.addEdge("aa", "eskalator 1g 1", 8)
g.addEdge("aa", "amarissa", 14)
g.addEdge("amarissa", "aa", 14)
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
g.addEdge("koi the", "y", 5)
g.addEdge("y", "koi the", 5)
g.addEdge("y", "h&m lantai 1", 8)
g.addEdge("h&m lantai 1", "y", 8)
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
g.addEdge("eskalator 12 1", "dr. specs", 7)
g.addEdge("dr. specs", "eskalator 12 1", 7)
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
g.addEdge("eskalator 12 3", "eskalator 1g 3", 6)
g.addEdge("eskalator 1g 3", "eskalator 12 3", 6)
g.addEdge("h&m lantai 1", "eskalator 12 3", 3)
g.addEdge("eskalator 12 3", "h&m lantai 1", 3)
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
g.addEdge("eskalator 12 2", "owl optical", 3)
g.addEdge("owl optical", "eskalator 12 2", 3)
g.addEdge("eskalator 1g 2", "eskalator 12 2", 5)
g.addEdge("eskalator 12 2", "eskalator 1g 2", 5)
g.addEdge("dr. specs", "zeiss vision center", 5)
g.addEdge("zeiss vision center", "dr. specs", 5)
g.addEdge("y", "lift 1 2", 10)
g.addEdge("lift 1 2", "y", 10)
g.addEdge("eskalator 12 1", "eskalator 21 1", 30) #eskalator
g.addEdge("eskalator 21 1", "eskalator 12 1", 30) #eskalator
g.addEdge("eskalator 12 2", "eskalator 21 2", 30) #eskalator
g.addEdge("eskalator 21 2", "eskalator 12 2", 30) #eskalator
g.addEdge("eskalator 12 3", "eskalator 21 3", 30) #eskalator
g.addEdge("eskalator 21 3", "eskalator 12 3", 30) #eskalator

#---------------------- Lantai 2 ----------------------#
g.addEdge("home & living", "h", 18)
g.addEdge("h", "home & living", 18)
g.addEdge("malinda furniture gallery", "h", 18)
g.addEdge("h", "malinda furniture gallery", 18)
g.addEdge("vivere", "h", 18)
g.addEdge("h", "vivere", 18)
g.addEdge("idemu", "h", 18)
g.addEdge("h", "idemu", 18)
g.addEdge("home & living", "c", 15)
g.addEdge("c", "home & living", 15)
g.addEdge("malinda furniture gallery", "c", 15)
g.addEdge("c", "malinda furniture gallery", 15)
g.addEdge("vivere", "c", 15)
g.addEdge("c", "vivere", 15)
g.addEdge("idemu", "c", 15)
g.addEdge("c", "idemu", 15)
g.addEdge("c", "l", 7)
g.addEdge("l", "c", 7)
g.addEdge("l", "lift 2 1", 8)
g.addEdge("lift 2 1", "l", 8)
g.addEdge("d", "lift 2 1", 8)
g.addEdge("lift 2 1", "d", 8)
g.addEdge("d", "l", 15)
g.addEdge("l", "d", 15)
g.addEdge("home & living", "eskalator 21 1", 21)
g.addEdge("eskalator 21 1", "home & living", 21)
g.addEdge("malinda furniture gallery", "eskalator 21 1", 21)
g.addEdge("eskalator 21 1", "malinda furniture gallery", 21)
g.addEdge("vivere", "eskalator 21 1", 21)
g.addEdge("eskalator 21 1", "vivere", 21)
g.addEdge("idemu", "eskalator 21 1", 21)
g.addEdge("eskalator 21 1", "idemu", 21)
g.addEdge("eskalator 21 1", "i", 13)
g.addEdge("i", "eskalator 21 1", 13)
g.addEdge("eskalator 21 1", "cc", 1)
g.addEdge("cc", "eskalator 21 1", 1)
g.addEdge("cc", "dd", 14)
g.addEdge("dd", "cc", 14)
g.addEdge("eskalator 23 1", "cc", 1)
g.addEdge("cc", "eskalator 23 1", 1)
g.addEdge("h", "i", 12)
g.addEdge("i", "h", 12)
g.addEdge("i", "j", 8)
g.addEdge("j", "i", 8)
g.addEdge("j", "payless shoes", 9)
g.addEdge("payless shoes", "j", 9)
g.addEdge("payless shoes", "padre", 12)
g.addEdge("padre", "payless shoes", 12)
g.addEdge("padre", "k", 11)
g.addEdge("k", "padre", 11)
g.addEdge("urban republic", "k", 13)
g.addEdge("k", "urban republic", 13)
g.addEdge("g", "m", 15)
g.addEdge("m", "g", 15)
g.addEdge("m", "eskalator 21 2", 3)
g.addEdge("eskalator 21 2", "m", 3)
g.addEdge("urban republic", "eskalator 21 2", 3)
g.addEdge("eskalator 21 2", "urban republic", 3)
g.addEdge("eskalator 21 2", "eskalator 23 2", 5)
g.addEdge("eskalator 23 2", "eskalator 21 2", 5)
g.addEdge("eskalator 23 2", "urban republic", 5)
g.addEdge("urban republic", "eskalator 23 2", 5)
g.addEdge("n", "eskalator 23 2", 5)
g.addEdge("eskalator 23 2", "n", 5)
g.addEdge("vans", "n", 6)
g.addEdge("n", "vans", 6)
g.addEdge("urban republic", "vans", 12)
g.addEdge("vans", "urban republic", 12)
g.addEdge("vans", "the north face", 6)
g.addEdge("the north face", "vans", 6)
g.addEdge("the north face", "hoops", 6)
g.addEdge("hoops", "the north face", 6)
g.addEdge("hoops", "seek", 8)
g.addEdge("seek", "hoops", 8)
g.addEdge("seek", "kkv lantai 2", 10)
g.addEdge("kkv lantai 2", "seek", 10)
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
g.addEdge("adidas", "eskalator 23 3", 8)
g.addEdge("eskalator 23 3", "adidas", 8)
g.addEdge("eskalator 23 3", "eskalator 21 3", 4)
g.addEdge("eskalator 21 3", "eskalator 23 3", 4)
g.addEdge("eskalator 21 3", "lao fook", 5)
g.addEdge("lao fook", "eskalator 21 3", 5)
g.addEdge("lao fook", "o", 4)
g.addEdge("o", "lao fook", 4)
g.addEdge("planet sports asia", "o", 3)
g.addEdge("o", "planet sports asia", 3)
g.addEdge("o", "lift 2 2", 10)
g.addEdge("lift 2 2", "o", 10)
g.addEdge("planet sports asia", "lift 2 2", 10)
g.addEdge("lift 2 2", "planet sports asia", 10)
g.addEdge("pan & co", "lift 2 2", 10)
g.addEdge("lift 2 2", "pan & co", 10)
# g.addEdge("lift 2 1", "lift 1 1", 9) #lift
# g.addEdge("lift 2 2", "lift 1 2", 9) #lift
# g.addEdge("lift 2 1", "lift 3 1", 9) #lift
# g.addEdge("lift 2 2", "lift 3 2", 9) #lift
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
g.addEdge("eskalator 23 1", "eskalator 32 1", 30) #eskalator
g.addEdge("eskalator 32 1", "eskalator 23 1", 30) #eskalator
g.addEdge("eskalator 23 2", "eskalator 32 2", 30) #eskalator
g.addEdge("eskalator 32 2", "eskalator 23 2", 30) #eskalator
g.addEdge("eskalator 23 3", "eskalator 32 3", 30) #eskalator
g.addEdge("eskalator 32 3", "eskalator 23 3", 30) #eskalator

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
g.addEdge("t", "boncafe", 13)
g.addEdge("boncafe", "t", 13)
g.addEdge("guardian plus", "vlife medical", 6)
g.addEdge("vlife medical", "guardian plus", 6)
g.addEdge("vlife medical", "huawei", 6)
g.addEdge("huawei", "vlife medical", 6)
g.addEdge("huawei", "oppo", 6)
g.addEdge("oppo", "huawei", 6)
g.addEdge("oppo", "house of david", 6)
g.addEdge("house of david", "oppo", 6)
g.addEdge("oppo", "pure clinic", 15)
g.addEdge("pure clinic", "oppo", 15)
g.addEdge("oppo", "maison feerie", 17)
g.addEdge("maison feerie", "oppo", 17)
g.addEdge("house of david", "justice", 6)
g.addEdge("justice", "house of david", 6)
g.addEdge("justice", "samsung", 9)
g.addEdge("samsung", "justice", 9)
g.addEdge("samsung", "watsons gm3", 12)
g.addEdge("watsons gm3", "samsung", 12)
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
g.addEdge("shinjuku", "t", 18)
g.addEdge("t", "shinjuku", 18)
g.addEdge("t", "mi store", 5)
g.addEdge("mi store", "t", 5)
g.addEdge("shinjuku", "natural farm", 7)
g.addEdge("natural farm", "shinjuku", 7)
g.addEdge("natural farm", "jiggle jungle", 28)
g.addEdge("jiggle jungle", "natural farm", 28)
g.addEdge("jiggle jungle", "eskalator 32 1", 15)
g.addEdge("eskalator 32 1", "jiggle jungle", 15)
g.addEdge("eskalator 32 1", "lift 3 1", 10)
g.addEdge("lift 3 1", "eskalator 32 1", 10)
g.addEdge("eskalator 34 1", "lift 3 1", 12)
g.addEdge("lift 3 1", "eskalator 34 1", 12)
g.addEdge("lift 3 1", "natural farm", 7)
g.addEdge("natural farm", "lift 3 1", 7)
g.addEdge("eskalator 32 1", "reformed exodus community", 18)
g.addEdge("reformed exodus community", "eskalator 32 1", 18)
g.addEdge("magal korean bbq", "eskalator 32 1", 13)
g.addEdge("eskalator 32 1", "magal korean bbq", 13)
g.addEdge("eskalator 34 2", "maison feerie", 5)
g.addEdge("maison feerie", "eskalator 34 2", 5)
g.addEdge("pure clinic", "eskalator 34 2", 6)
g.addEdge("eskalator 34 2", "pure clinic", 6)
g.addEdge("eskalator 34 2", "eskalator 32 2", 7)
g.addEdge("eskalator 32 2", "eskalator 34 2", 7)
g.addEdge("eskalator 32 2", "oppo", 6)
g.addEdge("oppo", "eskalator 32 2", 6)
g.addEdge("huawei", "eskalator 32 2", 7)
g.addEdge("eskalator 32 2", "huawei", 7)
g.addEdge("eskalator 32 2", "pure clinic", 10)
g.addEdge("pure clinic", "eskalator 32 2", 10)
g.addEdge("eskalator 32 3", "nona manis", 2)
g.addEdge("nona manis", "eskalator 32 3", 2)
g.addEdge("mothercare", "p", 10)
g.addEdge("p", "mothercare", 10)
g.addEdge("p", "eskalator 32 3", 2)
g.addEdge("eskalator 32 3", "p", 2)
g.addEdge("mothercare", "eskalator 34 3", 5)
g.addEdge("eskalator 34 3", "mothercare", 5)
g.addEdge("eskalator 34 3", "watsons gm3", 11)
g.addEdge("watsons gm3", "eskalator 34 3", 11)
g.addEdge("mi store", "boncafe", 15)
g.addEdge("boncafe", "mi store", 15)
g.addEdge("watsons gm3", "r", 7)
g.addEdge("r", "watsons gm3", 7)
g.addEdge("r", "q", 9)
g.addEdge("q", "r", 9)
g.addEdge("r", "lift 3 2", 8)
g.addEdge("lift 3 2", "r", 8)
g.addEdge("nona manis", "q", 10)
g.addEdge("q", "nona manis", 10)
g.addEdge("pure clinic", "house of david", 13)
g.addEdge("house of david", "pure clinic", 13)
g.addEdge("watsons gm3", "s", 12)
g.addEdge("s", "watsons gm3", 12)
g.addEdge("s", "mothercare", 3)
g.addEdge("mothercare", "s", 3)
# g.addEdge("lift 3 1", "lift 4 1", 9) #lift
# g.addEdge("lift 3 2", "lift 4 2", 9) #lift
# g.addEdge("lift 3 1", "lift 2 1", 9) #lift
# g.addEdge("lift 3 2", "lift 2 2", 9) #lift
# g.addEdge("eskalator 12 1", "eskalator 21 1", 30) #eskalator
# g.addEdge("eskalator 21 1", "eskalator 12 1", 30) #eskalator
# g.addEdge("eskalator 12 2", "eskalator 21 2", 30) #eskalator
# g.addEdge("eskalator 21 2", "eskalator 12 2", 30) #eskalator
# g.addEdge("eskalator 12 3", "eskalator 21 3", 30) #eskalator
# g.addEdge("eskalator 21 3", "eskalator 12 3", 30) #eskalator

#---------------------- Lantai 4 ----------------------#
g.addEdge("timezone gm3", "atm bca gm3", 19)
g.addEdge("atm bca gm3", "timezone gm3", 19)
g.addEdge("atm bca gm3", "bakmi gm", 11)
g.addEdge("bakmi gm", "atm bca gm3", 11)
g.addEdge("timezone gm3", "bakmi gm", 20)
g.addEdge("bakmi gm", "timezone gm3", 20)
g.addEdge("ichiban sushi", "bakmi gm", 11)
g.addEdge("bakmi gm", "ichiban sushi", 11)
g.addEdge("steak 21", "fusia", 9)
g.addEdge("fusia", "steak 21", 9)
g.addEdge("ichiban sushi", "steak 21", 11)
g.addEdge("steak 21", "ichiban sushi", 11)
g.addEdge("bakmi gm", "fusia", 20)
g.addEdge("fusia", "bakmi gm", 20)
g.addEdge("fusia", "food court", 67)
g.addEdge("food court", "fusia", 67)
g.addEdge("steak 21", "food court", 51)
g.addEdge("food court", "steak 21", 51)
g.addEdge("food court", "poke theory", 29)
g.addEdge("poke theory", "food court", 29)
g.addEdge("poke theory", "burger king", 11)
g.addEdge("burger king", "poke theory", 11)
g.addEdge("burger king", "crunchaus", 10)
g.addEdge("crunchaus", "burger king", 10)
g.addEdge("crunchaus", "jack & john", 8)
g.addEdge("jack & john", "crunchaus", 8)
g.addEdge("jack & john", "international christian assembly", 7)
g.addEdge("international christian assembly", "jack & john", 7)
g.addEdge("shaburi & kintan", "international christian assembly", 5)
g.addEdge("international christian assembly", "shaburi & kintan", 5)
g.addEdge("food court", "shaburi & kintan", 43)
g.addEdge("shaburi & kintan", "food court", 43)


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
    "lift g 1": {
        "lvl": 0,
        "lat": -7.276694348726551,
        "lon": 112.78000031309045
    },
    "lift g 2": {
        "lvl": 0,
        "lat": -7.276068503898244,
        "lon": 112.78072156282406
    },
    "x": {
        "lvl": 0,
        "lat": -7.276738194892914,
        "lon": 112.7800860111762
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
    "lift 1 1": { 
        "lvl": 1,
        "lat": -7.276685322893826,
        "lon": 112.77998835796643
    },
    "lift 1 2": {
        "lvl": 1,
        "lat": -7.276067130444247,
        "lon": 112.78075380185732
    },
    "y": {
        "lvl": 1,
        "lat": -7.276034574423221,
        "lon": 112.78064743897329
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
    "eskalator 12 1": {
        "lvl": 1,
        "lat": -7.276749303483015,
        "lon": 112.7800890392362
    },
    "eskalator 12 2": {
        "lvl": 1,
        "lat": -7.276683838969902,
        "lon": 112.78037130659726
    },
    "eskalator 12 3": {
        "lvl": 1,
        "lat": -7.275932819942739,
        "lon": 112.78061942343106
    },
    "a": {
        "lvl": 1,
        "lat": -7.276743431982581,
        "lon": 112.77995228926716
    },
    "b": {
        "lvl": 1,
        "lat": -7.276730899799716,
        "lon": 112.78008115541769
    },
    "aa": {
        "lvl": 1,
        "lat": -7.27683835376088,
        "lon": 112.77993627772213
    },
    # Lantai 2
    "home & living": { 
        "lvl": 2,
        "lat": -7.276860724638212,
        "lon": 112.77973573259476
    },
    "malinda furniture gallery": {
        "lvl": 2,
        "lat": -7.276860724638212,
        "lon": 112.77973573259476
    },
    "vivere": {
        "lvl": 2,
        "lat": -7.276860724638212,
        "lon": 112.77973573259476
    },
    "idemu": {
        "lvl": 2,
        "lat": -7.276860724638212,
        "lon": 112.77973573259476
    },
    "payless shoes": {
        "lvl": 2,
        "lat": -7.276836937605751,
        "lon": 112.78018308281861
    },
    "padre": {
        "lvl": 2,
        "lat": -7.276818690908215,
        "lon": 112.78031268588614
    },
    "iuiga": {
        "lvl": 2,
        "lat": -7.276640370086881,
        "lon": 112.78034231989534
    },
    "urban republic": {
        "lvl": 2,
        "lat": -7.2767204463104065,
        "lon": 112.78054386729116
    },
    "vans": {
        "lvl": 2,
        "lat": -7.2765962353408895,
        "lon": 112.78057924842744
    },
    "asics": {
        "lvl": 2,
        "lat": -7.276565461303477,
        "lon": 112.78036161580701
    },
    "the athlete's foot": {
        "lvl": 2,
        "lat": -7.2765097652382025,
        "lon": 112.78040749663381
    },
    "puma": {
        "lvl": 2,
        "lat": -7.276435278266959,
        "lon": 112.78044874291436
    },
    "new era": {
        "lvl": 2,
        "lat": -7.276379624512131,
        "lon": 112.78045446445572
    },
    "the north face": {
        "lvl": 2,
        "lat": -7.276542712505048,
        "lon": 112.78056372747807
    },
    "hoops": {
        "lvl": 2,
        "lat": -7.276451222625141,
        "lon": 112.78056278078157
    },
    "seek": {
        "lvl": 2,
        "lat": -7.276381285357999,
        "lon": 112.78057391507662
    },
    "kkv lantai 2": {
        "lvl": 2,
        "lat": -7.276278210494553,
        "lon": 112.78058694378853
    },
    "lao fook": {
        "lvl": 2,
        "lat": -7.276106705768356,
        "lon": 112.78061739331844
    },
    "pan & co": {
        "lvl": 2,
        "lat": -7.2760648370785646,
        "lon": 112.78084431043465
    },
    "planet sports asia": {
        "lvl": 2,
        "lat": -7.276034169681878,
        "lon": 112.78065314388778
    },
    "converse": {
        "lvl": 2,
        "lat": -7.2759379965479525,
        "lon": 112.7806246400466
    },
    "crocs": {
        "lvl": 2,
        "lat": -7.275926061113751,
        "lon": 112.78060466127937
    },
    "tucano's": {
        "lvl": 2,
        "lat": -7.275921713255016,
        "lon": 112.78052965395449
    },
    "adidas": {
        "lvl": 2,
        "lat": -7.27601887022368,
        "lon": 112.78049104271071
    },
    "wee nam kee": {
        "lvl": 2,
        "lat": -7.27618942493676,
        "lon": 112.78048245627355
    },
    "fila": {
        "lvl": 2,
        "lat": -7.2763010561743755,
        "lon": 112.78046753256609
    },
    "eskalator 21 1": {
        "lvl": 2,
        "lat": -7.276768553333966,
        "lon": 112.77993624210023
    },
    "eskalator 21 2": {
        "lvl": 2,
        "lat": -7.276717892957947,
        "lon": 112.78051579498236
    },
    "eskalator 21 3": {
        "lvl": 2,
        "lat": -7.276081333843109,
        "lon": 112.78058241025713
    },
    "eskalator 23 1": {
        "lvl": 2,
        "lat": -7.276750932334124,
        "lon": 112.78010500079404
    },
    "eskalator 23 2": {
        "lvl": 2,
        "lat": -7.276671588805115,
        "lon": 112.78052526834352
    },
    "eskalator 23 3": {
        "lvl": 2,
        "lat": -7.276070320701251,
        "lon": 112.7805357795653
    },
    "lift 2 1": {
        "lvl": 2,
        "lat": -7.2766848535805195,
        "lon": 112.78000285737369
    },
    "lift 2 2": {
        "lvl": 2,
        "lat": -7.276068335734408,
        "lon": 112.78074158628732
    },
    "c": {
        "lvl": 2,
        "lat": -7.2767354940717155,
        "lon": 112.77984858382945
    },
    "d": {
        "lvl": 2,
        "lat": -7.276705726973944,
        "lon": 112.78008643126907
    },
    "e": {
        "lvl": 2,
        "lat": -7.27671234188486,
        "lon": 112.78015867464944
    },
    "f": {
        "lvl": 2,
        "lat": -7.276706829458405,
        "lon": 112.78022758372055
    },
    "g": {
        "lvl": 2,
        "lat": -7.276690034557035,
        "lon": 112.78034071688091
    },
    "h": {
        "lvl": 2,
        "lat": -7.276924370984631,
        "lon": 112.77989501641031
    },
    "i": {
        "lvl": 2,
        "lat": -7.276880316109455,
        "lon": 112.78000922022068
    },
    "j": {
        "lvl": 2,
        "lat": -7.276856190818805,
        "lon": 112.78009698796382
    },
    "k": {
        "lvl": 2,
        "lat": -7.276784977442944,
        "lon": 112.78042857503351
    },
    "l": {
        "lvl": 2,
        "lat": -7.276724607564603,
        "lon": 112.77992220943213
    },
    "m": {
        "lvl": 2,
        "lat": -7.2767392846176335,
        "lon": 112.78049941692763
    },
    "n": {
        "lvl": 2,
        "lat": -7.2766484734403605,
        "lon": 112.78056892597806
    },
    "o": {
        "lvl": 2,
        "lat": -7.276056842374558,
        "lon": 112.78063890103869
    },
    "cc": {
        "lvl": 2,
        "lat": -7.276748074104617,
        "lon": 112.77993411470248
    },
    "dd": {
        "lvl": 2,
        "lat": -7.27673170334748,
        "lon": 112.78010290232993
    },
    # Lantai 3
    "jiggle jungle": {
        "lvl": 3,
        "lat": -7.2768155807522135,
        "lon": 112.77981203274476
    },
    "reformed exodus community": {
        "lvl": 3,
        "lat": -7.276920670469963,
        "lon": 112.77985119964342
    },
    "magal korean bbq": {
        "lvl": 3,
        "lat": -7.276902572657988,
        "lon": 112.77998229847361
    },
    "saga japanese restaurant": {
        "lvl": 3,
        "lat": -7.276819262534914,
        "lon": 112.78019573939446
    },
    "lincafe": {
        "lvl": 3,
        "lat": -7.2768067062172435,
        "lon": 112.78034097815214
    },
    "boncafe": {
        "lvl": 3,
        "lat": -7.276774794363888,
        "lon": 112.78045280241543
    },
    "natural farm": {
        "lvl": 3,
        "lat": -7.276704393831949,
        "lon": 112.78008507861017
    },
    "shinjuku": {
        "lvl": 3,
        "lat": -7.276710750756692,
        "lon": 112.78015911783064
    },
    "mi store": {
        "lvl": 3,
        "lat": -7.276632102832224,
        "lon": 112.7803355059113
    },
    "guardian plus": {
        "lvl": 3,
        "lat": -7.276709325876453,
        "lon": 112.78053466667228
    },
    "vlife medical": {
        "lvl": 3,
        "lat": -7.276650272627975,
        "lon": 112.78056177976526
    },
    "huawei": {
        "lvl": 3,
        "lat": -7.276585590749917,
        "lon": 112.7805706154532
    },
    "oppo": {
        "lvl": 3,
        "lat": -7.276517770284954,
        "lon": 112.78058249674416
    },
    "house of david": {
        "lvl": 3,
        "lat": -7.276450787084471,
        "lon": 112.7805918863121
    },
    "scoop ideas": {
        "lvl": 3,
        "lat": -7.276557363961814,
        "lon": 112.78035773868555
    },
    "maison feerie": {
        "lvl": 3,
        "lat": -7.2765074076917955,
        "lon": 112.78039719423464
    },
    "pure clinic": {
        "lvl": 3,
        "lat": -7.276441246523206,
        "lon": 112.78044212596126
    },
    "puro clinic": {
        "lvl": 3,
        "lat": -7.276379592572368,
        "lon": 112.78044967693313
    },
    "justice": {
        "lvl": 3,
        "lat": -7.27638543776763,
        "lon": 112.78060039319831
    },
    "samsung": {
        "lvl": 3,
        "lat": -7.276280054241553,
        "lon": 112.78061587802091
    },
    "willio": {
        "lvl": 3,
        "lat": -7.2762974805384175,
        "lon": 112.78045960484764
    },
    "gingersnaps": {
        "lvl": 3,
        "lat": -7.276218280056312,
        "lon": 112.78047118741506
    },
    "mothercare": {
        "lvl": 3,
        "lat": -7.276072583778202,
        "lon": 112.78049628837323
    },
    "watsons gm3": {
        "lvl": 3,
        "lat": -7.276158821164358,
        "lon": 112.78063212731763
    },
    "nona manis": {
        "lvl": 3,
        "lat": -7.2759244360052975,
        "lon": 112.78052488169988
    },
    "eskalator 32 1": {
        "lvl": 3,
        "lat": -7.276764447523618,
        "lon": 112.7799571083359
    },
    "eskalator 32 2": {
        "lvl": 3,
        "lat": -7.276528777251087,
        "lon": 112.78052305072418
    },
    "eskalator 32 3": {
        "lvl": 3,
        "lat": -7.27593611346289,
        "lon": 112.78053035672269
    },
    "eskalator 34 1": {
        "lvl": 3,
        "lat": -7.276746661091991,
        "lon": 112.78011624461203
    },
    "eskalator 34 2": {
        "lvl": 3,
        "lat": -7.2765032092432875,
        "lon": 112.7804546893666
    },
    "eskalator 34 3": {
        "lvl": 3,
        "lat": -7.276093968300472,
        "lon": 112.7805269946881
    },
    "lift 3 1": {
        "lvl": 3,
        "lat": -7.276683296924531,
        "lon": 112.78000978020265
    },
    "lift 3 2": {
        "lvl": 3,
        "lat": -7.276080470184809,
        "lon": 112.7807317850224
    },
    "p": {
        "lvl": 3,
        "lat": -7.275943539344524,
        "lon": 112.78050295489646
    },
    "q": {
        "lvl": 3,
        "lat": -7.275968394003243,
        "lon": 112.78063783383567
    },
    "r": {
        "lvl": 3,
        "lat": -7.276067713553303,
        "lon": 112.78064511852881
    },
    "s": {
        "lvl": 3,
        "lat": -7.276094932115541,
        "lon": 112.7805122393861
    },
    "t": {
        "lvl": 3,
        "lat": -7.276688034426414,
        "lon": 112.78034095702168
    },
    # Lantai 4
    "timezone gm3": {
        "lvl": 4,
        "lat": -7.276838666980666,
        "lon": 112.77990906241973
    },
    "atm bca gm3": {
        "lvl": 4,
        "lat": -7.276904404240923,
        "lon": 112.7801001416234
    },
    "bakmi gm": {
        "lvl": 4,
        "lat": -7.276857047555168,
        "lon": 112.7801318503428
    },
    "fusia": {
        "lvl": 4,
        "lat": -7.2768056696691445,
        "lon": 112.78033114871192
    },
    "ichiban sushi": {
        "lvl": 4,
        "lat": -7.276734269195828,
        "lon": 112.78012774452685
    },
    "steak 21": {
        "lvl": 4,
        "lat": -7.2767300686801235,
        "lon": 112.78025337164075
    },
    "food court": {
        "lvl": 4,
        "lat": -7.276336506793498,
        "lon": 112.78053275973247
    },
    "poke theory": {
        "lvl": 4,
        "lat": -7.27610589443195,
        "lon": 112.78040224987262
    },
    "burger king": {
        "lvl": 4,
        "lat": -7.2759870766181365,
        "lon": 112.78042351963882
    },
    "crunchaus": {
        "lvl": 4,
        "lat": -7.275884916204745,
        "lon": 112.78049068661892
    },
    "jack & john": {
        "lvl": 4,
        "lat": -7.27587381173241,
        "lon": 112.7805925576011
    },
    "international christian assembly": {
        "lvl": 4,
        "lat": -7.275927113198733,
        "lon": 112.78065300851301
    },
    "shaburi & kintan": {
        "lvl": 4,
        "lat": -7.275981525105394,
        "lon": 112.78067875612476
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
        rute_eska = [[], [], [], [], []]
        rute_lift = [[], [], [], [], []]
        goal = [[], [], [], [], []]
        selantai = 0
        data1, data2 = data
        data1 = data1.lower()
        data2 = data2.lower()
        
        ################## ESKALATOR ##################
        g.removeEdge("lift g 1", "lift 1 1")
        g.removeEdge("lift g 2", "lift 1 2")
        g.removeEdge("lift 1 1", "lift g 1")
        g.removeEdge("lift 1 2", "lift g 2")
        g.removeEdge("lift 1 1", "lift 2 1")
        g.removeEdge("lift 1 2", "lift 2 2") 
        g.removeEdge("lift 2 1", "lift 1 1")
        g.removeEdge("lift 2 2", "lift 1 2")
        g.removeEdge("lift 2 1", "lift 3 1")
        g.removeEdge("lift 2 2", "lift 3 2")
        g.removeEdge("lift 3 1", "lift 2 1") 
        g.removeEdge("lift 3 2", "lift 2 2") 

        g.addEdge("eskalator 1g 3", "eskalator g1 3", 30) 
        g.addEdge("eskalator g1 3", "eskalator 1g 3", 30) 
        g.addEdge("eskalator g1 1", "eskalator 1g 1", 30) 
        g.addEdge("eskalator 1g 1", "eskalator g1 1", 30) 
        g.addEdge("eskalator g1 2", "eskalator 1g 2", 30) 
        g.addEdge("eskalator 1g 2", "eskalator g1 2", 30) 
        g.addEdge("eskalator 12 1", "eskalator 21 1", 30) 
        g.addEdge("eskalator 21 1", "eskalator 12 1", 30) 
        g.addEdge("eskalator 12 2", "eskalator 21 2", 30) 
        g.addEdge("eskalator 21 2", "eskalator 12 2", 30) 
        g.addEdge("eskalator 12 3", "eskalator 21 3", 30) 
        g.addEdge("eskalator 21 3", "eskalator 12 3", 30) 
        g.addEdge("eskalator 23 1", "eskalator 32 1", 30) 
        g.addEdge("eskalator 32 1", "eskalator 23 1", 30) 
        g.addEdge("eskalator 23 2", "eskalator 32 2", 30) 
        g.addEdge("eskalator 32 2", "eskalator 23 2", 30) 
        g.addEdge("eskalator 23 3", "eskalator 32 3", 30) 
        g.addEdge("eskalator 32 3", "eskalator 23 3", 30) 
        # g.addEdge("eskalator 34 1", "eskalator 43 1", 30) 
        # g.addEdge("eskalator 43 1", "eskalator 34 1", 30) 
        # g.addEdge("eskalator 34 2", "eskalator 43 2", 30) 
        # g.addEdge("eskalator 43 2", "eskalator 34 2", 30) 
        # g.addEdge("eskalator 34 3", "eskalator 43 3", 30) 
        # g.addEdge("eskalator 43 3", "eskalator 34 3", 30) 

        dist_eska, path = g.dijkstra(data1, data2)
        path_eska = []
        before = after = data1
        if (path is not None):
            if (places[data1]["lvl"] == places[data2]["lvl"]):
                selantai = 1
            print(path)
        
            for place in path:
                after = place

                if (place == before):
                    path_eska.append([place, 0])
                else:
                    path_eska.append([place, g.getWeight(before, after)])
                
                before = place

                print(places[place]["lvl"])
                print(place)
                rute_eska[places[place]["lvl"]].append([places[place]["lat"], places[place]["lon"]])
            
            goal[places[path[-1]]["lvl"]] = [places[path[-1]]["lat"], places[path[-1]]["lon"]]
            
        print("ini rute_eska", rute_eska)
        print(dist_eska[data2])
        
        eskalator = {
            "rute": rute_eska,
            "dur": dist_eska[data2],
            "path": path_eska
        }

        ################## LIFT ##################
        g.removeEdge("eskalator 1g 3", "eskalator g1 3") 
        g.removeEdge("eskalator g1 3", "eskalator 1g 3") 
        g.removeEdge("eskalator g1 1", "eskalator 1g 1") 
        g.removeEdge("eskalator 1g 1", "eskalator g1 1") 
        g.removeEdge("eskalator g1 2", "eskalator 1g 2") 
        g.removeEdge("eskalator 1g 2", "eskalator g1 2") 
        g.removeEdge("eskalator 12 1", "eskalator 21 1") 
        g.removeEdge("eskalator 21 1", "eskalator 12 1") 
        g.removeEdge("eskalator 12 2", "eskalator 21 2") 
        g.removeEdge("eskalator 21 2", "eskalator 12 2") 
        g.removeEdge("eskalator 12 3", "eskalator 21 3") 
        g.removeEdge("eskalator 21 3", "eskalator 12 3") 
        g.removeEdge("eskalator 23 1", "eskalator 32 1") 
        g.removeEdge("eskalator 32 1", "eskalator 23 1") 
        g.removeEdge("eskalator 23 2", "eskalator 32 2") 
        g.removeEdge("eskalator 32 2", "eskalator 23 2") 
        g.removeEdge("eskalator 23 3", "eskalator 32 3") 
        g.removeEdge("eskalator 32 3", "eskalator 23 3") 
        # g.removeEdge("eskalator 34 1", "eskalator 43 1") 
        # g.removeEdge("eskalator 43 1", "eskalator 34 1") 
        # g.removeEdge("eskalator 34 2", "eskalator 43 2") 
        # g.removeEdge("eskalator 43 2", "eskalator 34 2") 
        # g.removeEdge("eskalator 34 3", "eskalator 43 3") 
        # g.removeEdge("eskalator 43 3", "eskalator 34 3") 

        g.addEdge("lift g 1", "lift 1 1", 9)
        g.addEdge("lift g 2", "lift 1 2", 9)
        g.addEdge("lift 1 1", "lift g 1", 9)
        g.addEdge("lift 1 2", "lift g 2", 9)
        g.addEdge("lift 1 1", "lift 2 1", 9)
        g.addEdge("lift 1 2", "lift 2 2", 9) 
        g.addEdge("lift 2 1", "lift 1 1", 9)
        g.addEdge("lift 2 2", "lift 1 2", 9)
        g.addEdge("lift 2 1", "lift 3 1", 9)
        g.addEdge("lift 2 2", "lift 3 2", 9)
        g.addEdge("lift 3 1", "lift 2 1", 9) 
        g.addEdge("lift 3 2", "lift 2 2", 9) 

        dist_lift, path = g.dijkstra(data1, data2)

        before = after = data1
        path_lift = []
        if (path is not None):
            print(path)

            for place in path:
                after = place

                if (place == before):
                    path_lift.append([place, 0])
                else:
                    path_lift.append([place, g.getWeight(before, after)])
                
                before = place
                print(places[place]["lvl"])
                print(place)
                rute_lift[places[place]["lvl"]].append([places[place]["lat"], places[place]["lon"]])
            
        print("ini rute_lift", rute_lift)
        print(dist_lift[data2])
        
        lift = {
            "rute": rute_lift,
            "dur": dist_lift[data2],
            "path": path_lift
        }

        resp = {
            "eskalator": eskalator,
            "lift": lift,
            "goal": goal,
            "level": selantai
        }
        return jsonify(resp)
    else:
        return "Data yang diterima tidak sesuai"
    


if __name__ == '__main__':
    app.run()
