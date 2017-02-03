from random import randint
def re_roll():
	ab_roller()
def ab_roller():
	list = [[],[],[],[],[],[],[]]
	for i in range(7):
		for s in range(4):
			list[i-1].append(randint(1,6))
	list = sorted(list, reverse=True)
	list_rolled = [0,0,0,0,0,0,0]
	for i in range(7):
		for s in range(3):
			list_rolled[i-1] += list[i-1][s-1]
	list_rolled = sorted(list_rolled, reverse=True)
	if list_rolled[5] <= 9:
		re_roll()
	else:
		print "Your ability scores are: %s, %s, %s, %s, %s, %s" % (list_rolled[0], list_rolled[1], list_rolled[2], list_rolled[3], list_rolled[4], list_rolled[5])
	os()
def os():
	for i in range(20):
		pc_in = raw_input("'A'bility score roller or 'D'ice roller: ").lower()
		if pc_in == "d":
			roller()
		elif pc_in == "a":
			ab_roller()
		else:
			print "I'm sorry that isn't an accepted input"
def roller():
	idx = input("How many dice? ")
	xdi = input("How many sides per dice? ")
	total = 0
	for i in range(idx):
		x = randint(1,xdi)
		print x
		total += x
	print "The total is %s" % (total)
	os()
print "Welcome to my table top dice roller"
print "At this point the system has been programmed to roll"
print "the ability scores of Pathfinder and DnD based"
print "characters along with a dice roller"
os()
