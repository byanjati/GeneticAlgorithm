import random
import csv
import math

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def deleteRightNode(self):
    	self.key = None
    	self.rightChild = None

    def insertNode(self,node):
    	self.key = node.getRootVal()
    	self.rightChild = node.getRightChild()

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertLeftTree(self,tree):
    	self.leftChild = tree

    def insertRightTree(self,tree):
    	self.rightChild = tree

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def deleteLeftNode(self):
    	self.leftChild = None

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

def condition(x):
	if x < 0.5:
		return 'and'
	else:
		return 'or'

def op(x):
	if x < 0.5:
		return '<'
	else:
		return '>'

def init(char1,char2,val1,val2):
	a = condition(random.random())
	op1 = op(random.random())
	op2 = op(random.random())

	r = BinaryTree(a)
	r.insertLeft(op1)
	r.getLeftChild().insertLeft(char1)
	r.getLeftChild().insertRight(val1)
	r.insertRight(op2)
	r.getRightChild().insertLeft(char2)
	r.getRightChild().insertRight(val2)

	return r

def addTree(tree,char1,val1): 
	a = condition(random.random())
	op1 = op(random.random())
	root = BinaryTree(a)
	root.insertLeftTree(tree)
	root.insertRight(op1)
	root.getRightChild().insertLeft(char1)
	root.getRightChild().insertRight(val1)

	return root

def addTreeRight(root,char1,val1): 
	a = condition(random.random())
	op1 = op(random.random())
	tree = BinaryTree(condition(random.random()))
	root.insertRightTree(tree)
	root.getRightChild().insertLeft(op1)
	root.getRightChild().getLeftChild().insertLeft(char1)
	root.getRightChild().getLeftChild().insertRight(val1)

def buildTree(char1,val1):
	root = BinaryTree(condition(random.random()))
	a = condition(random.random())
	op1 = op(random.random())
	root.insertLeft(op1)
	root.getLeftChild().insertLeft(char1)
	root.getRightChild().insertRight(val1)

	return root

def createTree():
	tree = init('komunikasi','kepemimpinan',random.uniform(90,160),random.uniform(400,668))
	sec_tree = addTree(tree,'integritas',random.uniform(114,190))
	third_tree = BinaryTree(condition(random.random()))
	third_tree.insertLeftTree(sec_tree)
	addTreeRight(third_tree,'kerjasama',random.uniform(199,300))
	last_tree = init('loyalitas','disiplin',random.uniform(99,100),random.uniform(53,130))
	third_tree.getRightChild().insertRightTree(last_tree)

	return third_tree

def getPartTree(tree):
	x = []
	e = inorder(tree,x)
	t = ' '.join(e)
	return t

def inorder(tree,s):
	if tree != None:
		inorder(tree.getLeftChild(),s)
		# print(tree.getRootVal(),end=' ')
		s.append(str(tree.getRootVal()))
		inorder(tree.getRightChild(),s)

	return s

def fungsiMasukan(komunikasi,kepemimpinan,integritas,kerjasama,loyalitas,disiplin,f):
	t = f %(komunikasi,kepemimpinan,integritas,kerjasama,loyalitas,disiplin)
	if(eval(t)):
		return 'Ya'
	else:
		return 'Tidak'

def size(tree):
	x = []

	inorder(tree,x)
	count = 0
	for i in x:
		if i=='and' or i=='or':
			count+=1

	return count

def getTree(tree,count):
	if size(tree)>count:
		i = 0
		while(i<count):
			tree = tree.getLeftChild()
			i+=1

		return tree

def merge(tree,count,tree_b):
	if size(tree) > count:
		i = 0
		while(i<count):
			tree = tree.getLeftChild()
			i+=1

		tree.deleteRightNode()
		tree.insertNode(tree_b)

# 2 kromosom dalam 1 pool menukarkan secuplik bagian tree
def recombination(tree_a,tree_b):
	if size(tree_a) > 1 and size(tree_b)>1:
		p1 = math.floor(random.uniform(1,size(tree_a)))
		p2 = math.floor(random.uniform(1,size(tree_b)))

		if size(tree_a)-2 > p1 and size(tree_b)-2 > p2:
			part_a = getTree(tree_a,p1)
			part_b = getTree(tree_b,p1)

			merge(tree_a,p1,part_b)
			merge(tree_b,p1,part_a)

# mutasi untuk varisi dengan memotong tree, mutasi hanya untuk bagian tengah tree 1<x<4
def mutation(tree,count):
	if size(tree)>1 and size(tree)-3 >count:
		a = getTree(tree,count-1)
		b = getTree(tree,count)
		c = getTree(tree,count+1)

		a.deleteLeftNode()
		b.deleteLeftNode()
		a.insertLeftTree(c)

def sizeOp(tree):
	x = []
	a = []
	count_ya = 0
	count_tidak = 0
	f = open('DataPromosi.csv')
	csv_f = csv.reader(f)

	inorder(tree,x)

	for row in csv_f:
		a = list(x)
		for n,i in enumerate(a):
			if(i=='komunikasi'):
				a[n] = row[2:9][0]
			elif(i=='kepemimpinan'):
				a[n] = row[2:9][1]
			elif(i=='integritas'):
				a[n] = row[2:9][2]
			elif(i=='kerjasama'):
				a[n] = row[2:9][3]
			elif(i=='loyalitas'):
				a[n] = row[2:9][4]
			elif(i=='disiplin'):
				a[n] = row[2:9][5]

		evaluasi = ' '.join(a)

		if(eval(evaluasi)):
			if(row[2:9][6]=='Ya'):
				count_ya += 1
		else:
			if(row[2:9][6]=='Tidak'):
				count_tidak += 1

	result = [count_ya,count_tidak]
	return result

def printKromosom(tree):
	x = []

	inorder(tree,x)

	return ' '.join(x)
	
banyak_kromosom = 100
kromosom = [createTree() for i in range(banyak_kromosom)]

# print(printKromosom(kromosom[0]))

list_p = [1,2,3,4]

list_result = {}

perulangan = 100
for percobaan in range(perulangan):
	print percobaan
	if(math.floor(random.uniform(1,11)) in list_p):
		a = int(math.floor(random.uniform(0,banyak_kromosom)))
		b = int(math.floor(random.uniform(2,5)))
		mutation(kromosom[a],b)
	else:
		p1 = int(math.floor(random.uniform(0,banyak_kromosom)))
		p2 = int(math.floor(random.uniform(0,banyak_kromosom)))
		recombination(kromosom[p1],kromosom[p2])

	for i in range(banyak_kromosom):
		list_result[kromosom[i]]=sizeOp(kromosom[i])

for i in range(banyak_kromosom):
	if(list_result[kromosom[i]][0]>5 and 69 < (float(list_result[kromosom[i]][0]+list_result[kromosom[i]][1])/50)*100):
		print(list_result[kromosom[i]][0],(float(list_result[kromosom[i]][0]+list_result[kromosom[i]][1])/50)*100,printKromosom(kromosom[i]))

AND(OR(AND(AND(AND(C1>103.664873222,D1>584.970688681),E1>144.15631416),F1>208.534137947),G1>99.9638585221),H1>83.5863425297)
