def find_fib(n):
    if n<=2:
        return 1
    fibX, fibN=1,1
    i=3
    while i<=n:
        i+=1
        fibX, fibN=fibN, fibX+fibN
    return fibN
    
#for x in range(1,11):
    #print(find_fib(x))
