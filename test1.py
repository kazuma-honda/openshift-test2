#import decimal
from decimal import Decimal

input_list=[]
input_list=input().split(" ")

m=int(input_list[0])
p=int(input_list[1])
q=int(input_list[2])

nokori= m*(1 - (p/100)) * (1-(q/100))
print(nokori)
