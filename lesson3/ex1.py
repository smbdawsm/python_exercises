def delenie(a,b):
    try: 
      print(f"answer is: {a/b}")
    except (ZeroDivisionError, TypeError) as err:
        print(err)
try:
    delenie(int(input("a?..")), int(input("b?..")))
except ValueError as err:
    print(err)