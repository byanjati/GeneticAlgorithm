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
lengthVar = 20

# inisialisasi individu
kromosom = [[random.uniform(-1,1) for i in range(lengthVar)]for j in range(jumPop)]

for i in range(1000):
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
				temp  = anak[i][j] + anak[i][2]*normal_db
				anak[i][j] = anak[i][j] + anak[i][2]*normal_db
			else:
				temp  = anak[i][j]*exp(t*normal_db)
				anak[i][j] = anak[i][j]*exp(t*normal_db)
				if(anak[i][j] < 8.854*(10 ** -12)):
					anak[i][j] = 8.854*(10 ** -12)

	def convert_matrix(kromosom,neuron,pola):
		k = 0
		A1 = []
		A2 = []
		for i in range(neuron):
			A2.append(kromosom[k:k+pola])
			k += pola
		return A2


	def fungsi_fitness(wa,w2):
		w1 = convert_matrix(wa,5,3)
		TestSet = [[3,3,1],
		   [3,1,2],
		   [2,3,1],
		   [2,1,2],
		   [1,3,1],
		   [1,2,2],
		   [1,1,1],]

		TestKelas = [0,1,0,1,0,1,0]

		jumPola = 7
		jumBenar = 0
		jumNeuron = 5
		jumOutput = 1

		for i in range(jumPola):
			cp = TestSet[i][:]
			a1 = []
			for j in range(jumNeuron):
				list_v = [a*b for a,b in zip(cp,w1[:][j])]
				v = 0
				for k in list_v:
					v += k
				math_v = 1/(1+math.exp(-1*v))
				a1.append(math_v)

			a2=[]
			for m in range(jumOutput):
				list_v = [a*b for a,b in zip(a1,w2)]
				v = 0
				for l in list_v:
					v += l
				math_v = 1/(1+math.exp(-1*v))
				a2.append(math_v)

			Kelas = 0 
			for z in range(jumOutput):
				if(a2[z] < 0.5):
					Kelas = 0
				else:
					Kelas = 1

			if(Kelas==TestKelas[i]):
				jumBenar = jumBenar + 1

		return jumBenar

	fitness = {fungsi_fitness(kromosom[i],kromosom[i][15:20]):[kromosom[i][0:5],kromosom[i][15:20]] for i in range(jumPop)}

	# for i in range(jumPop/2):
	# 	print anak[i]

# 	for i in range(len(anak)):
# 		kromosom.append(anak[i])

# 	def fungsi_fitness(a,b,bilkecil):
# 		total = 100*(a**2 - b)**2 + (1-a)**2
# 		total += bilkecil
# 		return 100 - 1/total

	# fitness = {fungsi_fitness(kromosom[i][0],kromosom[i][1],0.01):[kromosom[i][0],kromosom[i][1]] for i in range(len(kromosom))}

print 100*(float(max(fitness))/7.0),fitness[max(fitness)]
