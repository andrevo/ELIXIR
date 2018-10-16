import argparse


parser = argparse.ArgumentParser('Choose which network measures to compute')

parser.add_argument('-p', type=float)
args = vars(parser.parse_args())


fname = 'inFile.txt'
f = open(fname)

edges = {}
edgeVals = []

for line in f:
    splitLine = line.rstrip().split('\t')
    edges[(splitLine[0], splitLine[1])] = float(splitLine[2])
    edgeVals.append(float(splitLine[2]))

edgeVals.sort(reverse=True)
cutoffIndex = int(float(len(edgeVals))*0.01*args['p'])
cutoff = edgeVals[cutoffIndex]

of = 'outputNetwork.txt'
for edge in edges:
    if edges[edge] > cutoff:
        network.add_edge(edge[0], edge[1], weight=edges[edge])
        oline = edge[0]+'\t'+edge[1]+'\t'+edges[edge]
        print (oline, file=of)

of.close()
