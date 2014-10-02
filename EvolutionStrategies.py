import random
import numpy as np
from math import exp
import math

#inisial menggunakan n = 2, dan 1 mutation steps
#rekombinasi menggunakan 2 orang tua tetap, dan nilainya dirata - rata, jadi n / 2 anak
#mutasi menggunakan 1 mutation step size dan 2 x
#fitness dihitung dengan x nya saja
#seleksi survivor ditambahkan anak yang n/2 tadi dengan kromosom yang existing
#sehingga pada iterasi ke sekian jumlahnya populasi = n + n/2 + (n + n/2)/2

jumPop = 20
lengthVar = 3

# inisialisasi individu
kromosom = [[random.uniform(-2,2) for i in range(lengthVar)]for j in range(jumPop)]

for i in range(150):
	anak = []

	#Recombination, intermediary lokal
	i = 0
	while i < jumPop:
		kromosom_anak = []
		for j in range(lengthVar):
			total = kromosom[i][j] + kromosom[i+1][j]
			kromosom_anak.append(total/2)
		anak.append(kromosom_anak)
		i = i+2

	# for i in range(jumPop/2):
	# 	print anak[i]

	normal_db = np.random.standard_normal(size=(1,1))[0][0]
	t = 1/(math.sqrt(2))

	#Mutation
	for i in range(jumPop/2):
		for j in range(lengthVar):
			if(j<2):
				anak[i][j] = anak[i][j] + anak[i][2]*normal_db
			else:
				anak[i][j] = anak[i][j]*exp(t*normal_db)
				if(anak[i][j] < 8.854*(10 ** -12)):
					anak[i][j] = 8.854*(10 ** -12)

	# for i in range(jumPop/2):
	# 	print anak[i]

	for i in range(len(anak)):
		kromosom.append(anak[i])

	def fungsi_fitness(x1,x2,bilkecil):
		total = x1 ** 2 + x2 ** 2;
		total += bilkecil
		return 100 - 1/total

	fitness = [fungsi_fitness(kromosom[i][0],kromosom[i][1],0.01) for i in range(len(kromosom))]

print max(fitness)

