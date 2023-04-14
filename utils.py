def is_prime(num):
    if num <2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
def prime_range(n):
    for i in range(2,n):
        if is_prime(i):
            yield i

def prime_factors(n):
    q=[]
    while n>1:
        for i in range(2,n):
            if n%i==0 and is_prime(i)==True:
                q.append(i)
                n //= i
                break
        else:
            q.append(n)
            return q



