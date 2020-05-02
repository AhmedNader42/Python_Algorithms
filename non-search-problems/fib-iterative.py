def fib(n: int) -> int:
	if n == 0 : return n
	last = 0
	next = 1
	for _ in range(1, n):
		last, next = next, last + next
	return next

if __name__ == "__main__":
	print(fib(1000))