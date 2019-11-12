a = input("Input: ")
d = a.split(" ")
e = "".join(d)

if len(e) == 3:
	b = 2
elif len(e) == 6:
	b = 3
elif len(e) == 10:
	b = 4
elif len(e) == 15:
	b = 5
elif len(e) == 21:
	b = 6
elif len(e) == 28:
	b = 7
elif len(e) == 36:
	b = 8
else:
	b = 0

if b != 0:
	
	print()

	start = 0
	stop = 0
	counter = 0
	
	for i in range(1, b + 1):
		counter += 1
		stop += i
		x = list(e[start:stop])
		for h in x:
			print(h + ' ', end = '')
		print('')
		start = stop
		
	cc = counter
	stop = stop - 1
	start = 0
	
	for i in range(0, b + 1):
		x = list(e[start:start+counter])
		for h in x :
			print(h + ' ', end = '')
		print('')
		start = counter + start
		counter -= 1

else:
	print("Tidak bisa dibuat pola...")
