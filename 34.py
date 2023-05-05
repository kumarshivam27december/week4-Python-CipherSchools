import math
list_a=[3,10,18,22,36,40]
print("list:",list_a)
power_list=list(map(lambda x: int(math.pow(x,2)),list_a))
print("Resultant list: ",power_list)