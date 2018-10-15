import argparse
import networkx as nx

parser = argparse.ArgumentParser('Choose which network measures to compute')

parser.add_argument('-e', action='store_true')
parser.add_argument('-d', action='store_true')
parser.add_argument('-c', action='store_true')
parser.add_argument('-p', type=float)
parser.add_argument('-f')
args = vars(parser.parse_args())

print(args)


fname = 'inFile.txt'
pVal = 0.1


f = open(fname)

network = nx.Graph()

edges = {}

for line in f:
    splitLine = line.rstrip().split('\t')
    edges[(splitLine[0], splitLine[1])] = float(splitLine[2])

edgeVals = edges.values()
edgeVals.sort(reverse=True)
cutoffIndex = int(float(len(edgeVals))*0.01*args['p'])
cutoff = edgeVals[cutoffIndex]


for edge in edges:
    if edges[edge] > cutoff:
        network.add_edge(edge[0], edge[1], weight=edges[edge])

if args['e']:
    evc = nx.eigenvector_centrality(network)
if args['d']:
    degs = nx.degree(network)
if args['c']:
    clus = nx.clustering(network)

for node in network:
    oline = str(node)+'\t'
    if args['e']:
        oline = oline+str(evc[node])+'\t'
    if args['d']:
        oline = oline+str(degs[node])+'\t'
    if args['c']:
        oline = oline+str(clus[node])+'\t'
    oline = oline.rstrip()
    print oline
        
    
