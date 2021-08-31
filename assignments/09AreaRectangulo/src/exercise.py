
def area(b,a):
    ar = (b * a)
    return ar

def main():
    b = float(input("Dame la base: "))
    a = float(input("Dame la altura: "))
    res = area(b, a)
    print("El área del rectángulo es: " + str(res))
    
main()
