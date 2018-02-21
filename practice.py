l = ['a','a','a','b','b','b','c','c','c','a','a','a','d']
d ={}
l2 = []
for i in l:
	if i not in d:
		d[i] = 1
	else:
		d[i] += 1
		if d[i] == 3:
			l2.append(i) + str(d[i])
			d.clear()

print(l2)
			
	
