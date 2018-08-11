def foo():
    try:
        f = open('hola.txt', 'r')
        print(f.read())
    except:
        f = open('hola.txt', 'w')
        f.write('Holaaaa!')
    finally:
        f.close()
        
foo()

        
