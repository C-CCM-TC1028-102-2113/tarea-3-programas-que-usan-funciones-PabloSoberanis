
def area(b,a):
    a = (b * a)
    return a

def main():
    b = float(input("Dame la base: "))
    a = float(input("Dame la altura: "))
    res = area(b, a)
    print("El área del rectángulo es: " + str(res))
    
main()
