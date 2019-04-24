import copy

faces = [
    [
        [0,0,5],[1,2,0],[1,2,1],[1,1,3] # 9/4 = 2.25
    ],
    [
        [1,1,1],[1,1,2],[1,1,0] # 3/3 = 1
    ],
    [
        [1,2,1],[2,2,3],[1,2,1],[4,3,1] # 6/4 = 1.5
    ]
]

s = []
totals = []

for face in faces:
    t = 0
    for vert in face:
        t += vert[2]

    t /= len(face)

    totals.append(t)

minInd = 0
s = copy.deepcopy(faces)

for n in range(1,len(totals)):
    # sort
    
    if totals[n] > totals[minInd]:
        # move current to before minInd
        temp = copy.deepcopy(s[n])
        s[n] = s[minInd]
        s[n-1] = temp

        minInd = n

for face in faces:
    print(face)
#print(s)
