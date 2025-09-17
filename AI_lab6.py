graph = {
'0' : ['1','2','3'],
'1' : ['0','4','5'],
'2' : ['0','6','7'],
'3' : ['0','8'],
'4' : ['1'],
'5' : ['1','9'],
'6' : ['2','7','9'],
'7' : ['2','6','10','11'],
'8' : ['3','11','12','13'],
'9' : ['5','6','14','15'],
'10' : ['7','15','16','17'],
'11' : ['7','8','18','19'],
'12' : ['8'],
'13' : ['8'],
'14' : ['9'],
'15' : ['9','10'],
'16' : ['10'],
'17' : ['10'],
'18' : ['11'],
'19' : ['11']
}

#Depth-Limited Search 
def dls(graph, S, goal, L):

    if S == goal:
        return [S]

    F = [(S, 0)]  # stack holds (node, depth)
    reached = set([S])  

    while F:
        N, depth = F.pop()
        print("Visiting:", N, "at depth", depth)

        if N == goal:
            return [N]

        if depth < L:  # only expand if within depth limit
            for neighbour in graph[N]:
                if neighbour not in reached:
                    if neighbour == goal:
                        return [N, neighbour]
                    F.append((neighbour, depth + 1))
                    reached.add(neighbour)

    return None

#Iterative Deepening Search
def ids(graph, S, goal):

    L = 0
    while True:
        print(f"\n--- Depth Limit = {L} ---")
        result = dls(graph, S, goal, L)
        if result is not None:
            return result
        L += 1


#Client Code
print("Following is the Iterative Deepening Search")
ids(graph, '13', '14')