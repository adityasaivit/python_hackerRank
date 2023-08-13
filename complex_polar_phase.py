# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
import math

n=complex(input())
print(abs(n))
print(cmath.phase(complex(n.real,n.imag)))
