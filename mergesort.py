def ordena(lista1, lista2, lista3, opened):
       	n=len(lista1)
       	g=[]
       	h=[]
       	i=[]
	for j in range(n):
		maximo=max(lista1)
		ind= lista1.index(maximo)
		g.append(lista1[ind])
       	        h.append(lista2[ind])
       	        i.append(lista3[ind])
                del(lista1[ind])
                del(lista2[ind])
		del(lista3[ind])
       	for j in range(len(g)):
       	        opened.write((str(g[j])+' sequence(s) of:'+'\n'+h[j]+'\n'+i[j]+'\n\n'))
