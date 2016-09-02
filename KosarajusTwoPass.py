def loadFile():
    with open('/home/alejandro/Documents/Stanford Algorithms 1/Week 4/Test1.txt') as f:
        graph = {}
        for line in f:
            if line:
                line = line.split()
                node = int(line[0])
                if node in graph:
                    graph[node].append(int(line[1]))
                else:
                    graph[node] = [int(line[1])]
    return graph

def dfs(graph, i, exploredNodes, finishing, leader, t, s):
    exploredNodes.append(i)
    if s in leader:
        leader[s].append(i)
    else:
        leader[s] = [i]
    for j in graph[i]:
        if j not in exploredNodes:
            dfs(graph, j, exploredNodes, finishing, leader, t, s)
    t += 1
    if t in finishing:
        finishing[t].append(i)
    else:
        finishing[t] = [i]

def dfsLoop1stPass(graph):
    exploredNodes = []
    finishing = {}
    leader = {}
    t = 0
    s = None
    for i in sorted(graph.keys(), reverse=True):
        if i not in exploredNodes:
            s = i
            dfs(graph, i, exploredNodes, finishing, leader, t, s)
    return finishing
            
def dfsLoop2ndPass(graph, finishing):
    exploredNodes = []
    leader = {}
    t = 0
    s = None
    for f in sorted(finishing.keys(), reverse=True):
        for i in finishing[f]:
            if i not in exploredNodes:
                s = i
                dfs(graph, i, exploredNodes, finishing, leader, t, s)
    return leader           
            
def reverseGraph(graph):
    revGraph = {}
    for key, value in graph.iteritems():
        for x in value:
            if x in revGraph:
                revGraph[x].append(key)
            else:
                revGraph[x] = [key]
    return revGraph

graph = loadFile()
revGraph = reverseGraph(graph)
print "Graph:\n" + str(graph) + "\nReverse Graph:\n" + str(revGraph)

fin = dfsLoop1stPass(revGraph)
lead = dfsLoop2ndPass(graph, fin)

for x in sorted(lead.keys(), reverse=True):
    count = 0
    for y in lead[x]:
        count += 1
    print count

print str(lead)
