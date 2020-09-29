import numpy as np
w=5
matrix = [[0 for x in range(w)] for y in range(w)] 
distance=[0 for x in range(w)] 
visited=[0 for x in range(w)]
pre=[0 for x in range(w)]
min=0
nextnode=0
for i in range(5):
    for j in range(5):
        matrix[i][j]=input()
        matrix[i][j]=int(matrix[i][j])
        if(matrix[i][j]==0):
            matrix[i][j]=1000
distance=matrix[0]
distance[0]=0
visited[0]=1
for i in range(5):
    min=1000
    for j in range(5):
        if((min>distance[j])and(visited[j]!=1)):
            min=distance[j]
            nextnode=j
    visited[nextnode]=1
    for c in range(5):
        if(visited[c]!=1):
            if((min+matrix[nextnode][c]<distance[c])):
                distance[c]=min+(matrix[nextnode][c])
                pre[c]=nextnode

for u in range(5):
    print(distance[u])
