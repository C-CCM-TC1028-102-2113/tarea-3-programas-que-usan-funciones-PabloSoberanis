
def main():
    #escribe tu código abajo de esta línea
    x = int(input("Dame la cantidad de pliegos de papel albanene: "))
    y = int(input("Dame la cantidad de plumones: "))
    t = y*35
    p = x*12

    if(p > t):
      print(t)
    elif(p < t):
      print(p)  
    pass

if __name__=='__main__':
    main()
