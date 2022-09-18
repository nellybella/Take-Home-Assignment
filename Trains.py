
class Graph:
    def __init__(self, edges):
 
        self.adjList = {}
 
        for (src, dest, weight) in edges:
            if src in self.adjList:
                self.adjList[src].append((dest, weight))
            else:
                self.adjList[src] = [(dest, weight)]
 
        # print("Graph:", self.adjList)

    def distanceOfRoute(self, routes):
        if(self.isRouteExists(routes) == False):
            return 'NO SUCH ROUTE'

        distance = 0
        routes = list(routes)
        length = len(routes)
        for vertex in range(length-1):
            src = routes[vertex]
            end = routes[vertex+1]
            edge = self.adjList.get(src)
            for e in edge:
                if(e[0] == end):
                    distance += e[1]

        return distance

    def numberOfRoutesWithDistanceLess(self, src, end, maxDistance=30):
        noOfRoutes = 0
        
        nodes = self.adjList.get(src)
        newPaths = []
        for node in nodes:
            paths = self.getPaths(node[0], end)
            for path in paths:
                path = [src] + path
                newPaths.append(path)
                
        distances = []
        for paths in newPaths:
            distances.append(self.distanceOfRoute("".join(paths)))

        noOfRoutes = 0
        for d1 in distances:
            if(d1 < maxDistance):
                noOfRoutes += 1
            for d2 in distances:
                if(d1+d2 < maxDistance):
                    noOfRoutes += 1


        for d1 in distances:
            sum = d1 + d1 + d1
            while(sum < maxDistance):
                noOfRoutes += 1
                sum += d1

        return noOfRoutes

    def isRouteExists(self, routes):
        routes = list(routes)
        length = len(routes)
        for vertex in range(length-1):
            src = routes[vertex]
            end = routes[vertex+1]
            edge = self.adjList.get(src)
            valid = False
            for e in edge:
                if(e[0] == end):
                    valid = True
            if(valid == False):
                return False

        return True

    def getPaths(self, src, end, path=[]):
        path = path + [src]

        if src == end:
            return [path]

        if src not in self.adjList:
            return []

        paths = []

        for node in self.adjList[src]:
            if node[0] not in path:
                newPaths = self.getPaths(node[0], end, path)
                for p in newPaths:
                    paths.append(p)

        return paths
        
    def getPathsExactLength(self, src, end, path=[], steps=0):
        path = path + [src]

        if (src == end and steps == 4):
            return [path]

        if(steps > 4):
            return []

        if src not in self.adjList:
            return []

        paths = []

        for node in self.adjList[src]:
            newPaths = self.getPathsExactLength(node[0], end, path, steps+1)
            for p in newPaths:
                paths.append(p)

        return paths
        
        

    def numberOfTripsWithMaximumSteps(self, src, end, maxSteps):
        noOfTrips = 0
        nodes = self.adjList.get(src)
        trips = []

        for n in nodes:
            trips.append(self.getPaths(n[0], end))

        for trip in trips:
            for t in trip:
                if(len(t) <= maxSteps):
                    noOfTrips += 1

        return noOfTrips

    def numberOfTripsWithExactlySteps(self, src, end, exactSteps):

        paths = self.getPathsExactLength(src, end)

        return len(paths)

    def shortestRouteLength(self, src, end):
        
        path = self.BFS_SP(src, end)
        distance = 0
        length = len(path)
        for vertex in range(length-1):
            src = path[vertex]
            end = path[vertex+1]
            edge = self.adjList.get(src)
            for e in edge:
                if(e[0] == end):
                    distance += e[1]

        return distance

    def BFS_SP(self, start, end):
        explored = []
        queue = [[start]]
        
        while queue:
            path = queue.pop(0)
            node = path[-1]
            
            if node not in explored:
                neighbours = self.adjList[node]
                
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour[0])
                    queue.append(new_path)
                    
                    if neighbour[0] == end:
                        return new_path

                explored.append(node)
    
        return
    
 
if __name__ == '__main__':
 
    # Graph: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
    edges = [
            ('A', 'B', 5),
            ('B', 'C', 4),
            ('C', 'D', 8),
            ('D', 'C', 8),
            ('D', 'E', 6),
            ('A', 'D', 5),
            ('C', 'E', 2),
            ('E', 'B', 3),
            ('A', 'E', 7)
        ]
 
    graph = Graph(edges)

 
    distance = graph.distanceOfRoute('ABC')
    print(f"Output #1: {distance}")

    distance = graph.distanceOfRoute('AD')
    print(f"Output #2: {distance}")

    distance = graph.distanceOfRoute('ADC')
    print(f"Output #3: {distance}")

    distance = graph.distanceOfRoute('AEBCD')
    print(f"Output #4: {distance}")

    distance = graph.distanceOfRoute('AED')
    print(f"Output #5: {distance}")

    numOfTrips = graph.numberOfTripsWithMaximumSteps('C', 'C', 3)
    print(f"Output #6: {numOfTrips}")

    numOfTrips = graph.numberOfTripsWithExactlySteps('A', 'C', 4)
    print(f"Output #7: {numOfTrips}")

    distance = graph.shortestRouteLength('A','C')
    print(f"Output #8: {distance}")

    distance = graph.shortestRouteLength('B','B')
    print(f"Output #9: {distance}")

    routes = graph.numberOfRoutesWithDistanceLess('C','C', 30)
    print(f"Output #10: {routes}")
