def f(result, fuhao):
    dic = {')': '(', '}': '{', ']': '['}
    pipei = result[-1]
    if pipei == dic[fuhao]:
        return True
    else:
        return False

def isValid(s: str) -> bool:
    result = ['?']
    for ele in s:
        if ele in "({[":
            result.append(ele)
        else:
            if f(result, ele):
                result.pop()
            else:
                return False

    if len(result)==1:
        return True
    else:
        return False


a = '({}})'

m = isValid(']]')
pass
