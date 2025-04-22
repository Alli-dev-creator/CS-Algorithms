def nwt_raph(y):
    epsilon = 0.000001
    x = y/3
    if y< 0:
        print("Root does not exist")
    else:
        while x**2 - y >= epsilon:
            x = x - (x**2 - y)/(2*x)
    print(x)
nwt_raph(1546)