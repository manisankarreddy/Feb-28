a ="sankar reddy"
s = ""
c = 0
b = a.split(" ")
for i in b:
	if c == 1:
		s += i + " "
		c += 1
	else:
		s = i[::-1] + " "
		c += 1
print(s)
#r = list(s)
#print(r)
