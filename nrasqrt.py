def nwt_raph(y):
    epsilon = 0.000001
    x = y/3
    global steps
    steps = 1
    if y< 0:
        print("Root does not exist")
    else:
        while x**2 - y >= epsilon:
            x = x - (x**2 - y)/(2*x)
            steps += 1
    print(x)
def bisect(value):
    low = 0
    high = value
    global times
    times = 1 
    ans = (high + low)/2
    limiter = 0.000001
    while abs(ans**2 - value) >= limiter:
        if ans**2 < value:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
        times += 1
    print(ans)
def compare(number):
    print("Newton-Raphson method:")
    nwt_raph(number)
    print("Bisection method:")
    bisect(number)
    print("Newton-Raphson steps:", steps)
    print("Bisection steps:", times) 
compare(56789)       