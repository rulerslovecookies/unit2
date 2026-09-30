def parking_spots(N, Y, T):
    
    N = 5
    space = 0
    for i in range(N):
        if Y[i] == "C" and T[i] == "C":
            space += 1
    print(space)
parking_spots(5, "CCCCC", ".C..C")
