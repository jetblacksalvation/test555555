import sys

print("what is your favorite bands/musicions?")

_list =[input(" arg num {} : ".format(x)) for x in range(3)]

print(_list[1], "is the middle one")

_list = [input("tell me ur favorite food {} : ".format(x)) for x in range(5)]
print(_list[-1])

print("give me supervillain heor first villain last")

_list = [[input() for x in range(2)] for f in range(6)]
while 1:
    temp = input("which key are you use : Q to quit")
    for elem in _list:
        if elem[0] ==temp:
            print(elem[1])
            
    if temp == 'q':
        break
    exit()
