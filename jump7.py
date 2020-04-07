for i in range(1,101):
	if i % 7 == 0 or str(i).startswith('7') or str(i).endswith('7'):
		continue
	print(i)

