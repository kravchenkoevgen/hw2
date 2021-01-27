fin  = open("input.txt")
fout = open("output.txt","w")

a, b, c = map(int, fin.readline().split())
d = (max(a, b, c))
e = (min(a, b, c))
fout.write(str(d-e))

fin.close()
fout.close()