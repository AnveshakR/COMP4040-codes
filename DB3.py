p = 95189
x0 = 42
X = (x0*x0)%p
for i in range(10):
    print(X)
    X = (X*X)%p