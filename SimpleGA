import random 

ba = 15
bb = 1
jumPop = 20
inLength = 4
length = '{0:0' + str(inLength) + 'b}'
bilkecil = 0.001
pc = 0.8
pm = 0.1
maxGen = 150

def fungsi_fitness(lists,bilkecil):
	total = 1
	for i in range(len(lists)):
		total *= lists[i]

	total += bilkecil
	return 100 - 1/total

# inisialisasi populasi
kromosom = [[random.randint(bb,ba),random.randint(bb,ba)] for i in range(jumPop)]

for gen in range(maxGen):
	fitness = [fungsi_fitness(kromosom[i],bilkecil) for i in range(jumPop)]

	print fitness[0]

	# dekode kromosom int -> biner
	for i in range(jumPop):
		for j in range(2):
			kromosom[i][j] = length.format(kromosom[i][j])

	matingPool = []
	halfPop = jumPop / 2
	for i in range(halfPop):
		matingPool.append([kromosom[random.randint(0,jumPop-1)],kromosom[random.randint(0,jumPop-1)]])

	# rekombinasi 
	resPop = []
	for i in range(halfPop):
		if random.random() < pc: 
			temp = matingPool[i][0][1]
			matingPool[i][0][1].replace(matingPool[i][0][1],matingPool[i][1][1]) 
			matingPool[i][1][1].replace(matingPool[i][1][1],temp)
			
			str_mating_pool   = matingPool[i][0][0] + matingPool[i][0][1]
			str_mating_pool_2 = matingPool[i][1][0] + matingPool[i][1][1]
			resPop.append(str_mating_pool)
			resPop.append(str_mating_pool_2)
		else:
			str_mating_pool   = matingPool[i][0][0] + matingPool[i][0][1]
			str_mating_pool_2 = matingPool[i][1][0] + matingPool[i][1][1]
			resPop.append(str_mating_pool)
			resPop.append(str_mating_pool_2)

	def mutation(kromosom,pm):
		for i in range(len(kromosom)-1):
			if random.random() < pm:
				if kromosom[i] == "0" : 
					kromosom[i].replace("0","1")
				else:
					kromosom[i].replace("1","0")
		return kromosom

	for i in range(20):
		resPop[i].replace(resPop[i],mutation(resPop[i],pm))	

	# print resPop[0][:4:]
	# print resPop[0][4::]

	def convert_to_int(string):
		total = 0
		i = len(string)-1
		j = 0
		while i>-1:
			if(string[i] == "1"):
				total += (2 ** j) * 1  

			i = i - 1
			j = j + 1

		return total

	kromosom = []
	# balikin lagi dari biner ke desimal
	for i in range(jumPop):
		kromosom.append([convert_to_int(resPop[i][:4:]),convert_to_int(resPop[i][4::])])

	# for i in range(jumPop):
	# 	print kromosom[i]
