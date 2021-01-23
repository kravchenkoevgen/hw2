fin  = open("input.txt")
fout = open("output.txt","w")

a, b, c = map(int, fin.readline().split())
fout.write(str(max(a, b, c)))

fin.close()
fout.close()