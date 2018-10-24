from sys import argv
from contextlib import redirect_stdout

def fatorial(n):
	fat = 1
	while (n > 1):
		fat = n * fat
		n = n - 1
	return (fat)

def bin_coeff(i , j): 
	fat1 = fatorial(i)
	fat2 = fatorial(j)
	fat3 = fatorial(i - j)
	return ((fat1)//(fat2 * fat3))

if __name__ == "__main__":
	n = int(argv[1])
	k = int(argv[2])
	
	with open("triangle.out", "w", encoding="utf-8") as out:
		with redirect_stdout(out):
			for i in range(n+1):
				k = n + 1 if (k > n + 1) else k
				limit = i + 1 if i != n else k
				for j in range(limit):
					print(bin_coeff(i , j), end=" ")
				print()