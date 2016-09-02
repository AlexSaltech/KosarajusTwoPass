global s
global t

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

def dfsLoop1stPass(graph):
    exploredNodes = []
    finishing = {}
    global t
    t = 0
    for i in sorted(graph.keys(), reverse=True):
        if i not in exploredNodes:
            dfs1stPass(graph, i, exploredNodes, finishing)
    return finishing

def dfs1stPass(graph, i, exploredNodes, finishing):
    exploredNodes.append(i)
    global t
    if i in graph:
        for j in graph[i]:
            if j not in exploredNodes:
                dfs1stPass(graph, j, exploredNodes, finishing)
        t += 1
        if t in finishing:
            finishing[t].append(i)
        else:
            finishing[t] = [i]
    
def dfs2ndPass(graph, i, exploredNodes, leader):
    exploredNodes.append(i)
    global s
    if s in leader:
        leader[s].append(i)
    else:
        leader[s] = [i]
        for j in graph[i]:
            if j not in exploredNodes:
                dfs2ndPass(graph, j, exploredNodes, leader)

            
def dfsLoop2ndPass(graph, finishing):
    exploredNodes = []
    leader = {}
    global s
    s = None
    for f in sorted(finishing.keys(), reverse=True):
        for i in finishing[f]:
            if i not in exploredNodes:
                s = i
                dfs2ndPass(graph, i, exploredNodes, leader)
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
print str(fin)
print str(lead)
