def es_bisiesto(a):
    if a % 4 != 0: 
	    return False
    elif a % 4 == 0 and a % 100 != 0:
	    return True
    elif a % 4 == 0 and a % 100 == 0 and a % 400 != 0: 
	    return False
    elif a % 4 == 0 and a % 100 == 0 and a % 400 == 0: 
	     return True

def main():
  
  añoU = int(input())#el año que queremos comprobar
  res = es_bisiesto(añoU)
  print(str(res))

if __name__ == '__main__':
    main()
