p = 95189
x0 = 42
temp = (x0*x0)%p
for i in range(10):
    print(temp)
    temp = (temp*temp)%p