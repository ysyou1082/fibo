#fibonacci sequence

def fibo(num) :
    if num < = 3 :
        return 1
    else :
        return fibo(num-1)+ fibo(num-2)  

if __name__=='__main__':	print(fibo(5))





