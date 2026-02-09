import time

def execution_time(first_n):
    def wrapper(n):
        start=time.time()
        first_n(n)
        end=time.time()
        print(end-start)
    return wrapper

@execution_time
def first_n(n):
    sum=0
    for i in range(1,n+1):
        sum+=1
    print("Sum is:",sum)

first_n(1000000)