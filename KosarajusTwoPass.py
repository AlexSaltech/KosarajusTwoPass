import sys
import copy
import time

global s
s=None
global t
t=0
exploredNodes = {}

def loadFile():
    with open('/home/alejandro/Documents/Stanford Algorithms 1/Week 4/SCC.txt') as f:
        graph = {}
        revGraph = {}
        numberOfNodes = 875714
        for x in range(1,numberOfNodes+1):
            graph[x] = []
            exploredNodes[x] = [False,False]
            #revGraph[x] = []
        revGraph = copy.deepcopy(graph)
        for line in f:
            if line:
                line = line.split()
                node = int(line[0])
                connection = int(line[1])
                #if node in graph:
                graph[node].append(connection)
                #else:
                #graph[node] = [connection]
                #if connection in revGraph:
                revGraph[connection].append(node)
                #else:
                #revGraph[connection] = [node]
    return (graph,revGraph)
            
def dfsLoop1stPass(graph):
    t = 0
    finishing = {}
    finishingP = {}
    for i in sorted(graph.keys(), reverse=True):
        start = i
        q = [start,]
        while q:
            #if i == 874931: print "while q"
            v = q.pop()
            if not exploredNodes[v][0]:
                exploredNodes[v][0] = True
                q.append(v)
                for w in graph[v]:
                    #print "for" + str(w)
                    if not exploredNodes[w][0]: q.append(w)
            else:
                if v not in finishingP:
                    finishingP[v] = True
                    finishing[t] = v
                    t += 1
    return finishing
    
def dfs2ndPass(graph, i, exploredNodes, leader):
    exploredNodes[i][1] = True
    global s
    if s in leader:
        leader[s].append(i)
    else:
        leader[s] = [i]
    for j in graph[i]:
        if not exploredNodes[j][1]:
            dfs2ndPass(graph, j, exploredNodes, leader)

            
def dfsLoop2ndPass(graph, finishing):
    leader = {}
    s = None
    for i in sorted(finishing.keys(), reverse=True):
        start = finishing[i]
        q = [start,]
        while q:
            v = q.pop()
            if not exploredNodes[v][1]:
                s = i
                if s in leader:
                    leader[s].append(i)
                else:
                    leader[s] = [i]
                exploredNodes[v][1] = True
                q.append(v)
                for w in graph[v]:
                    if not exploredNodes[w][1]: q.append(w)
    return leader
    '''
    leader = {}
    global s
    s = None
    for f in sorted(finishing.keys(), reverse=True):
        i = finishing[f]
        if not exploredNodes[i][1]:
            s = i
            dfs2ndPass(graph, i, exploredNodes, leader)
    return leader
    '''            
                                    
def reverseGraph(graph):
    revGraph = {}
    for key, value in graph.iteritems():
        for x in value:
            if x in revGraph:
                revGraph[x].append(key)
            else:
                revGraph[x] = [key]
    return revGraph

t0 = time.time()
graphTuple = loadFile()
print "File loaded"
graph = graphTuple[0]
revGraph = graphTuple[1]
#print "Graph:\n" + str(graph)
#print "Reverse Graph:\n" + str(revGraph)

fin = dfsLoop1stPass(revGraph)
print "First pass"
lead = dfsLoop2ndPass(graph, fin)
print "Second pass"
countL = []
#top = 0
for x in sorted(lead.keys(), reverse=True):
    count = 0
    for y in lead[x]:
        count += 1
    countL.append(count)
    #if count > top:
        #top = count
    #print count
#print top

print str(sorted(countL, reverse=True)[:5])
print "Time taken: " + str(time.time()-t0)
#print str(fin)
#print str(lead)
