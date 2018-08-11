f = open('hello.txt', 'w')
try:
    f.write('hoiii!')
finally:
    f.close()
