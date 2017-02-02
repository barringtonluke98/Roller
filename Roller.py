from random import randint
def re_roll():
	ab_roller()
def ab_roller():
	list = [[],[],[],[],[],[],[]]
	for i in range(7):
		for s in range(4):
			list[i-1].append(randint(1,6))
	for i in range(100):
		if list[0][0] < list[0][1]:
			temp1 = list[0][0]
			temp2 = list[0][1]
			list[0][0] = temp2
			list[0][1] = temp1
		elif list[0][1] < list[0][2]:
			temp1 = list[0][1]
			temp2 = list[0][2]
			list[0][1] = temp2
			list[0][2] = temp1
		elif list[0][2] < list[0][3]:
			temp1 = list[0][2]
			temp2 = list[0][3]
			list[0][2] = temp2
			list[0][3] = temp1
	list[0][3] = 0
	for i in range(100):
		if list[1][0] < list[1][1]:
			temp1 = list[1][0]
			temp2 = list[1][1]
			list[1][0] = temp2
			list[1][1] = temp1
		elif list[1][1] < list[1][2]:
			temp1 = list[1][1]
			temp2 = list[1][2]
			list[1][1] = temp2
			list[1][2] = temp1
		elif list[1][2] < list[1][3]:
			temp1 = list[1][2]
			temp2 = list[1][3]
			list[1][2] = temp2
			list[1][3] = temp1
	list[1][3] = 0
	for i in range(100):
		if list[2][0] < list[2][1]:
			temp1 = list[2][0]
			temp2 = list[2][1]
			list[2][0] = temp2
			list[2][1] = temp1
		elif list[2][1] < list[2][2]:
			temp1 = list[2][1]
			temp2 = list[2][2]
			list[2][1] = temp2
			list[2][2] = temp1
		elif list[2][2] < list[2][3]:
			temp1 = list[2][2]
			temp2 = list[2][3]
			list[2][2] = temp2
			list[2][3] = temp1
	list[2][3] = 0
	for i in range(100):
		if list[3][0] < list[3][1]:
			temp1 = list[3][0]
			temp2 = list[3][1]
			list[3][0] = temp2
			list[3][1] = temp1
		elif list[3][1] < list[3][2]:
			temp1 = list[3][1]
			temp2 = list[3][2]
			list[3][1] = temp2
			list[3][2] = temp1
		elif list[3][2] < list[3][3]:
			temp1 = list[3][2]
			temp2 = list[3][3]
			list[3][2] = temp2
			list[3][3] = temp1
	list[3][3] = 0
	for i in range(100):
		if list[4][0] < list[4][1]:
			temp1 = list[4][0]
			temp2 = list[4][1]
			list[4][0] = temp2
			list[4][1] = temp1
		elif list[4][1] < list[4][2]:
			temp1 = list[4][1]
			temp2 = list[4][2]
			list[4][1] = temp2
			list[4][2] = temp1
		elif list[4][2] < list[4][3]:
			temp1 = list[4][2]
			temp2 = list[4][3]
			list[4][2] = temp2
			list[4][3] = temp1
	list[4][3] = 0
	for i in range(100):
		if list[5][0] < list[5][1]:
			temp1 = list[5][0]
			temp2 = list[5][1]
			list[5][0] = temp2
			list[5][1] = temp1
		elif list[5][1] < list[5][2]:
			temp1 = list[5][1]
			temp2 = list[5][2]
			list[5][1] = temp2
			list[5][2] = temp1
		elif list[5][2] < list[5][3]:
			temp1 = list[5][2]
			temp2 = list[5][3]
			list[5][2] = temp2
			list[5][3] = temp1
	list[5][3] = 0
	for i in range(100):
		if list[6][0] < list[6][1]:
			temp1 = list[6][0]
			temp2 = list[6][1]
			list[6][0] = temp2
			list[6][1] = temp1
		elif list[6][1] < list[6][2]:
			temp1 = list[6][1]
			temp2 = list[6][2]
			list[6][1] = temp2
			list[6][2] = temp1
		elif list[6][2] < list[6][3]:
			temp1 = list[6][2]
			temp2 = list[6][3]
			list[6][2] = temp2
			list[6][3] = temp1
	list[6][3] = 0
	list_rolled = [0,0,0,0,0,0,0]
	for i in range(7):
		for s in range(4):
			list_rolled[i-1] += list[i-1][s-1]
	for s in range(100):
		if list_rolled[0] < list_rolled[1]:
			temp1 = list_rolled[0]
			temp2 = list_rolled[1]
			list_rolled[0] = temp2
			list_rolled[1] = temp1
		elif list_rolled[1] < list_rolled[2]:
			temp1 = list_rolled[1]
			temp2 = list_rolled[2]
			list_rolled[1] = temp2
			list_rolled[2] = temp1
		elif list_rolled[2] < list_rolled[3]:
			temp1 = list_rolled[2]
			temp2 = list_rolled[3]
			list_rolled[2] = temp2
			list_rolled[3] = temp1
		elif list_rolled[3] < list_rolled[4]:
			temp1 = list_rolled[3]
			temp2 = list_rolled[4]
			list_rolled[3] = temp2
			list_rolled[4] = temp1
		elif list_rolled[5] < list_rolled[6]:
			temp1 = list_rolled[5]
			temp2 = list_rolled[6]
			list_rolled[5] = temp2
			list_rolled[6] = temp1
	list_rolled = sorted(list_rolled, reverse=True)
	if list_rolled[5] <= 9:
		re_roll()
	else:
		print "Your ability scores are: %s, %s, %s, %s, %s, %s" % (list_rolled[0], list_rolled[1], list_rolled[2], list_rolled[3], list_rolled[4], list_rolled[5])
	print raw_input("Press enter to go again")
	re_roll()
ab_roller()


	
	
	
	
	
	