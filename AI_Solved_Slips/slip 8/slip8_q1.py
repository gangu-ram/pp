user_input= "i ama pranav PP"

lower=0
upper=0

for i in user_input:
    if i.islower():
        lower += 1
    elif i.isupper():
        upper+= 1
print("lower string is:", lower)
print("upper String :", upper )
