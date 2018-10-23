import argparse
import networkx as nx

parser = argparse.ArgumentParser('Choose which network measures to compute')

parser.add_argument('-e', action='store_true')
parser.add_argument('-d', action='store_true')
parser.add_argument('-c', action='store_true')
parser.add_argument('--custom')
parser.add_argument('-p', type=float)
parser.add_argument('-f')
args = vars(parser.parse_args())

if args['f'] != None:
    fname = args['f']
else:
    fname = inFile.txt
    
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
    cutoffIndex = min(int(float(len(edgeVals))*0.01*args['p']), len(edgeVals)-1)
    cutoff = edgeVals[cutoffIndex]
else:
    cutoff = min(edgeVals)



for edge in edges:
    if edges[edge] >= cutoff:
        network.add_edge(edge[0], edge[1], weight=edges[edge])

nodeFunc = {'e': nx.eigenvector_centrality, 'd': nx.degree, 'c': nx.clustering}
nodeFuncNames = {'e': 'Eigenvector centrality', 'd': 'Degree', 'c': 'Clustering'}
if(args['custom'] != None):
    nodeFunc['custom'] = getattr(nx, args['custom'])
    nodeFuncNames['custom'] = args['custom']

nodeRes = {}


for arg in nodeFunc:
    if args[arg]:
        nodeRes[arg] = nodeFunc[arg](network)

    
oline='Node\t'
for arg in nodeRes:
    if args[arg]:
        oline = oline+nodeFuncNames[arg]+'\t'
print(oline)
        
for node in network:
    oline = str(node)+'\t'
    for arg in nodeRes:
        if args[arg]:
            oline = oline+str(nodeRes[arg][node])+'\t'
    oline.rstrip()
    print(oline)
        
    
