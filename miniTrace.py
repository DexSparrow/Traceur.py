from tkinter import*
from math import*
# By Hilarion Alias Li Li
# Je peux pas encore differencier un nombre et un char
# Je ne sais pas encore gerer l'entree de l'utilisateur qui peut Amener de l'erreur 
# Je ne pais encore mis de grandeur sur les axes
# J'ai devellope ce miniAppli pendant un cours de math ca fait a peu pres 2h la duree dont j'ai fait tout cela
# Meme si c'est un projet Noob j'en suis quand meme fiere de ce que j'ai accompli
# Je viens d'ajouter quelque code "traduire" pour corriger l'entree utilisateur comme 
# 2x + 2 => 2*x+2


def inserer(text,intrus,balise):
	i = 0
	res = ""
	y = len(text)
	while (i < y):
		if (i == balise):
			res += (intrus)
			res += (text[i])
		else :
			res += (text[i])
		i += 1
	res =  str(res)							
	return res

def isNaN(s):
	try :
		int(s)
	except :
		verite = 1
	else :
		verite = 0

	return verite			

def traduire(g):
	i = 0
	x = len(g)
	while (g[i] != ''):
		if (g[i] == 'x'):
			if (g[i - 1] == g[len(g) - 1]):
				pass
			elif(g[i - 1] =='/') :
				pass
			elif(g[i - 1] =='*') :
				pass	
			elif(g[i - 1] =='+') :
				pass	
			elif(g[i - 1] =='-') :
				pass	
			elif(g[i - 1] =='(') :
				pass	
			else :
				g = inserer(g,'*',i)
		i += 1	
		if (i >= len(g)):
				break	
	return g



canWi = 500
canHei = 500


# Il y a une certaine limite qu'ue je sais pas encore comment regler // en fait les boucles limite le truc 
#  	---->J'ai regle le probleme en utilisant la recursivite :)

ray = 0.1
lineWi = 0.1

echelle = 3


def Tracer() :
	global x,y,axeX,axeY
	if (x >= limi):
		pass
	else :
		y = eval(traduire(aa.get()))
		axeX.append(x*echelle)
		axeY.append(y*echelle)
		if (len(axeX) == 2):
			canvas.create_oval(((canWi/2)+axeX[0]) - ray,(canHei/2 - axeY[0]) - ray,((canWi/2)+axeX[0]) + ray,(canHei/2 - axeY[0]) + ray,fill = "black")
			canvas.create_oval(((canWi/2)+axeX[1]) - ray,(canHei/2 - axeY[1]) - ray,((canWi/2)+axeX[1]) + ray,(canHei/2 - axeY[1]) + ray,fill = "black")
			canvas.create_line(((canWi/2)+axeX[0]),(canHei/2 - axeY[0]),((canWi/2)+axeX[1]),(canHei/2 - axeY[1]),width = lineWi)
			del(axeX[0]) 
			del(axeY[0])	
		x += 1	
		ctx.after(30,Tracer)		

def letTrace() :
	global x,axeX,axeY,limi
	canvas.create_rectangle(0,0,canWi,canHei,fill = "white")
	canvas.create_line(canWi/2,1,canWi/2,canHei)
	canvas.create_line(0,canHei/2,canWi,canHei/2)
	x = int(bb.get())
	limi = int(cc.get()) 
	axeX = [] 
	axeY = []
	Tracer()
# def Tracer(limi = 100) :
# 	canvas.create_rectangle(0,0,canWi,canHei,fill = "white")
# 	axeX = [] 
# 	axeY = []
# 	x = 0	
# 	while (x < limi ):
# 		y = eval(aa.get())
# 		axeX.append(x*echelle)
# 		axeY.append(y*echelle)
# 		if (len(axeX) == 2):
# 			canvas.create_oval((axeX[0]) - ray,(canHei/2 - axeY[0]) - ray,(axeX[0]) + ray,(canHei/2 - axeY[0]) + ray,fill = "black")
# 			canvas.create_oval((axeX[1]) - ray,(canHei/2 - axeY[1]) - ray,(axeX[1]) + ray,(canHei/2 - axeY[1]) + ray,fill = "black")
# 			canvas.create_line((axeX[0]),(canHei/2 - axeY[0]),(axeX[1]),(canHei/2 - axeY[1]),width = lineWi)
# 			del(axeX[0]) 
# 			del(axeY[0])	
# 		x += 1	




ctx = Tk()
a = Label(text = "Equation:")
aa = Entry()
a.grid(row = 0,column = 0)
aa.grid(row = 0,column = 1)

b = Label(text = "Debut:")
bb = Entry()
b.grid(row = 2,column = 0)
bb.grid(row = 2,column = 1)

c = Label(text = "Limite:")
cc = Entry()
c.grid(row = 4,column = 0)
cc.grid(row = 4,column = 1)

# Pas besoin pur le moment

# d = Label(text = "D:")
# dd = Entry()
# d.grid(row = 6,column = 0)
# dd.grid(row = 6,column = 1)

# e = Label(text = "E:")
# ee = Entry()
# e.grid(row = 8,column = 0)
# ee.grid(row = 8,column = 1)

manuel = Label(text = "Entrez un equation comme : 2*x + 2 ")
manuel.grid(row = 4,column = 1,rowspan = 5)

buttonTrace = Button(text = "Tracer",command = letTrace)
button999 = Button(text = "Quittez",command = ctx.quit)

buttonTrace.grid(row = 12,column =1)
button999.grid(row = 14,column =1)






canvas = Canvas(width = canWi, height = canHei,bg = "#ffffff")
canvas.create_line(canWi/2,1,canWi/2,canHei)
canvas.create_line(0,canHei/2,canWi,canHei/2)
canvas.grid(row = 0,rowspan = 20,column = 4)

ctx.mainloop()











