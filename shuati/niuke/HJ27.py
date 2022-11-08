# inputlst = '4 abc bca cab cba abc 1'#input()
inputlst = input()
inputlst = inputlst.split()
total, lst, target, k = inputlst[0], inputlst[1:-2], inputlst[-2], int(inputlst[-1])

target_paixu = sorted(target)
res = []
for ele in lst:
    if ele == target:
        pass
    else:
        ele_paixu = sorted(ele)
        if target_paixu == ele_paixu:
            res.append(ele)

res2 = sorted(res)
print(len(res2))
print(res2[k-1])
