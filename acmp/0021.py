fin  = open("input.txt")
fout = open("output.txt","w")

a, b, c =(str(a, b, c))
d = (max(a, b, c))
e = (min(a, b, c))
d, e = map(int, fin.readline().split())
fout.write(str(d-e))

fin.close()
fout.close()