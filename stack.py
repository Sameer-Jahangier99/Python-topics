def push(num, n):
    num.append(n);
    return n

def pop(num):
    if isEmpty(num):
       return False
    else:
        num.pop()
        return num

def isEmpty(num):
    if not num:
        return True
    else:
        return False


num = []

push(num, 2);
print(num);
print(num.pop())
print(num);
       
     