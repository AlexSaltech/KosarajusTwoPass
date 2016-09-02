import sys

global s
s=None
global t
t=0

sys.setrecursionlimit(30000)

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
    t = 0
    finishing = {}
    for i in range(max(graph.keys()),0,-1):
        start = i
        q = [start]
        while q:
            v = q.pop(0)
            if v not in exploredNodes:
                exploredNodes.append(v)
                q = [v] + q
                for w in graph[v]:
                    if w not in exploredNodes: q = [w] + q
            else:
                if v not in finishing.values():
                    finishing[t] = v
                    t += 1
    return finishing
    
def dfs2ndPass(graph, i, exploredNodes, leader):
    if i in graph:
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
    print "Sorted:\n" + str(sorted(finishing.keys(), reverse=True))
    for i in sorted(finishing.keys(), reverse=True):
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
#print "Graph:\n" + str(graph)
#print "Reverse Graph:\n" + str(revGraph)

fin = dfsLoop1stPass(revGraph)
lead = dfsLoop2ndPass(graph, fin)
'''
countL = []
top = 0
for x in sorted(lead.keys(), reverse=True):
    count = 0
    for y in lead[x]:
        count += 1
    countL.append(count)
    if count > top:
        top = count
    #print count
print top
'''
#print str(sorted(countL))
print str(fin)
print str(lead)
