"""
	Dynamic Programming 

	- Mainly an optimization over plain recursion	 
	- Store the results of subproblems, 
	  so we do not have to recompute them when needed later
"""
def Fibonacci(fib, n) :
	if n not in fib :
		fib[n] = Fibonacci(fib, n - 1) + Fibonacci(fib, n - 2)
		return Fibonacci(fib, n - 1) + Fibonacci(fib, n - 2)
	else :
		return fib.get(n)

#Declare dictionary type for DP
fib = {0 : 0 , 1 : 1}

n = int(input())

print(Fibonacci(fib, n))