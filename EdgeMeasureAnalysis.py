import argparse
import networkx as nx

parser = argparse.ArgumentParser('Choose which network measures to compute')

parser.add_argument('-b', action='store_true')
parser.add_argument('--custom')
parser.add_argument('-p', type=float)
args = vars(parser.parse_args())


fname = 'inFile.txt'

f = open(fname)

network = nx.Graph()

edges = {}
edgeVals = []

for line in f:
    splitLine = line.rstrip().split('\t')
    edges[(splitLine[0], splitLine[1])] = float(splitLine[2])
    edgeVals.append(float(splitLine[2]))

edgeVals.sort(reverse=True)
if args['p'] != None:
    cutoffIndex = int(float(len(edgeVals))*0.01*args['p'])
    cutoff = edgeVals[cutoffIndex]
else:
    cutoff = min(edgeVals)

for edge in edges:
    if edges[edge] >= cutoff:
        network.add_edge(edge[0], edge[1], weight=edges[edge])

edgeFunc = {'b': nx.edge_betweenness_centrality}
edgeFuncNames = {'b': 'Edge betweenness centrality'}
if(args['custom'] != None):
    edgeFunc['custom'] = getattr(nx, args['custom'])
    edgeFuncNames['custom'] = args['custom']
    

edgeRes = {}


for arg in edgeFunc:
    if args[arg]:
        edgeRes[arg] = edgeFunc[arg](network)

oline='Node 1\tNode 2\t'
for arg in edgeRes:
    if args[arg]:
        oline = oline+edgeFuncNames[arg]+'\t'
print(oline)

for edge in network.edges():
    oline = str(edge[0])+'\t'+str(edge[1])+'\t'
    for arg in edgeRes:
        if args[arg]:
            oline = oline+str(edgeRes[arg][edge])+'\t'
    oline.rstrip()
    print(oline)
        
    
