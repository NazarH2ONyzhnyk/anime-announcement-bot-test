from cmath import inf


info = open('info.txt', 'w')
info.write('Hellow, World!')
info.close()

info = open('info.txt', 'r')
print(info.read())
info.close()