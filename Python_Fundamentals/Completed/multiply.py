a = [2,4,10,16]
def multiply(a,factor):
        for i in range(0,len(a)):
                a[i] *= factor
        return a
b = multiply(a,5)
print b
