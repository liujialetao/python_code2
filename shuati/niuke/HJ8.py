# n = input()
# n = int(n)
# a = []
# while n:
#     input_pair = [int(ele) for ele in input('zu:').split()]
#     a.append(input_pair)
#     n -= 1
a = [[0,1],[-1,2],[0,3]]
dic = dict()
for key,value in a:
    if key in dic.keys():
        dic[key] +=value
    else:
        dic[key] =value
keys = sorted(dic)
for key in keys:
    print(key,dic[key])
#dict[(key,dic[key]) for key in sorted(dic)]