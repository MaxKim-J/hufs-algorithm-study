#재귀 -->시간초과
#2934 반례

X = int(input())

def n(X):
    if X == 1:
        return 0
    elif X == 2:
        return 1
    elif X == 3:
        return 1
    else:
        temp = n(X-1) + 1
        if X % 3 == 0:
            temp1 = n(X//3) + 1
            if temp1 <= temp:
                return temp1
            else:
                return temp

        elif X % 2 == 0:
            temp3 = n(X//2) + 1
            if temp3 <= temp:
                return temp3
            else:
                return temp

        else:
            return temp

print(n(X))