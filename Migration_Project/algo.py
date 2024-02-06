from bson.json_util import dumps, loads
from queue import Queue
import colors as bcolor


# function to get order of embedding
def getOrder(tables, work) :
    n = len(work)
    adj = []
    for i in range(n) :
        adj.append([])
    indeg = [0]*n
    vis = {}
    relax = []
    zeroqueue = Queue(maxsize = n+1)
    for i in range(n) :
        for j in range(n) :
            if work[i][j] == 'e' and work[j][i] == "e" :
                work[i][j] = '-'
                work[j][i] = '-'
                relax.append([i, j, 1])
    for i in range(n) :
        for j in range(n) :
            if(work[i][j] == 'e') :
                indeg[i] = indeg[i] + 1
                adj[j].append(i)
    for t in range(n) :
        if(indeg[t] == 0) :
            zeroqueue.put(t)
        
    while zeroqueue.qsize() > 0 :
        t = zeroqueue.get()
        for c in adj[t] :
            indeg[c] = indeg[c] - 1
            if(indeg[t] == 0) :
                zeroqueue.put(c)
            relax.append([c, t])
    for pair in relax :
        print("embed " + tables[pair[1]] + " in " + tables[pair[0]])
    return relax



# dfs on access paths
def dfs1(tables,tNo,adj1,work1,currCollec,vis1,curTable):
    vis1.add(curTable)
    for nxtTable in adj1[curTable]:
        if(nxtTable not in vis1):
            dfs1(tables,tNo,adj1,work1,currCollec,vis1,nxtTable)
        if(nxtTable in currCollec):
            work1[tNo[curTable]][tNo[nxtTable]]="l"
        else:
            work1[tNo[curTable]][tNo[nxtTable]]="e"


    
# dfs on adjacency list of Relational Schema
def dfs2(tables,tNo,adj2,work2,currCollec,vis2,relations,curTable):
    vis2.add(curTable)
    if(len(relations[curTable])==0):
        if(len(adj2[curTable])==0):
            currCollec.add(curTable)
        elif(len(adj2[curTable])==1):
            nxtTable=adj2[curTable][0]
            if(curTable in currCollec):
                work2[tNo[curTable]][tNo[nxtTable]]="l"
            else:
                work2[tNo[nxtTable]][tNo[curTable]]="e"
            dfs2(tables,tNo,adj2,work2,currCollec,vis2,relations,nxtTable)
        else:
            for nxtTable in adj2[curTable]:
                if(nxtTable not in vis2):
                    dfs2(tables,tNo,adj2,work2,currCollec,vis2,relations,nxtTable)
                if(nxtTable in currCollec):
                    work2[tNo[curTable]][tNo[nxtTable]]="l"
                else:
                    work2[tNo[curTable]][tNo[nxtTable]]="e"
    else:
        for nxtTable in adj2[curTable]:
            if(nxtTable not in vis2):
                dfs2(tables,tNo,adj2,work2,currCollec,vis2,relations,nxtTable)
            if(nxtTable in currCollec):
                work2[tNo[curTable]][tNo[nxtTable]]="l"
            else:
                work2[tNo[curTable]][tNo[nxtTable]]="e"
    return



# function for main algorithm
def algo(tables,tNo,relations,paths):
    print(f"{bcolor.bcolors.OKCYAN}Running Algorithm{bcolor.bcolors.ENDC}")

    nTables=len(tables)
    currCollec = {"dummy"}

    #Part 1
    vis1 = {"dummy"}
    work1= [["-"]*nTables for _ in range(nTables)]

    # creating potential collections
    for p in paths:
        currCollec.add(p[0])
    currCollec.remove("dummy")
    vis1.remove("dummy")

    # creates adjacency from access paths
    adj1={}
    for t in tables:
        adj1[t]=[]

    for r in paths:
        for i in range(len(r)-1):
            adj1[r[i]].append(r[i+1])

    for t in currCollec:
        dfs1(tables,tNo,adj1,work1,currCollec,vis1,t)

    #Part 2
    vis2 = {"dummy"}
    work2= [["-"]*nTables for _ in range(nTables)]

    # creates adjacency from schema
    adj2={}
    for t in tables:
        adj2[t]=[]

    for r in relations:
        for r1 in relations[r]:
            adj2[r1[0]].append(r)

    for t in tables:
        dfs2(tables,tNo,adj2,work2,currCollec,vis2,relations,t)

    work = work1
    for i in range(nTables):
        for j in range(nTables):
            if(work1[i][j]=='-'):
                work[i][j]=work2[i][j]
            else:
                work[i][j]=work1[i][j]
                
    relax = getOrder(tables, work)

    print(f"{bcolor.bcolors.OKCYAN}Algorithm completed successfully{bcolor.bcolors.ENDC}")
    return [currCollec,relax, work, adj2]


