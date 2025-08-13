def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print('Value  of ','index', i, 'is',l[i])
    return 1
  except ValueError:
    print('ValueError')
  
  except IndexError:
    print('IndexError')
  
  except:
    print('Some Error Occured')
    return 0

  finally:
    print("I am always executed")
    return 1

x = func1()
print(x)