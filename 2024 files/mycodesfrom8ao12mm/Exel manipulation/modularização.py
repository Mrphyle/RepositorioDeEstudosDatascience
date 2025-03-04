#Sum
def Sum(n1,n2):
    return n1+n2
#subtract
def sub(n1,n2):
    return n1-n2
#Division
def div(n1,n2):
    return n1/n2
#Multiplication
def mult(n1,n2):
    return n1*n2
def main():
    a= int(input("Type first number: "))
    b= int(input("Type last number: "))
    print((f"sum {Sum(a,b)}"))
    print((f"subtract {sub(a,b)}"))
    print((f"divided {div(a,b)}"))
    print((f"multiply {mult(a,b)}"))
main()