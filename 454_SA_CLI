# Produced by Diogo Munaro Vieira
print ''
print 'Welcome to 454 Simple Analysis CLI'
print ''
entrada = raw_input('Input Name (inDNA.txt): ')
saida = raw_input('Output Name (outDNA.txt): ')
diversi = raw_input('Output Diversity (outdiversity.txt): ')
div=open("Output/"+diversi,'w')
t=open("Input/"+entrada,'r')
saida=open("Output/"+saida,'w')
x=t.readlines()
dic={}
print "Removing duplicates..."
for j in range(0,len(x),2):
	d={x[j+1]:x[j]}
	dic.update(d)
key=dic.keys()
value=dic.values()
print "Looking for diversity..."
for j in range(0,len(x),2):
	d={x[j]:x[j+1]}
	dic.update(d)
v=dic.values()
print "Checking the results..."
for j in range(len(key)):
	saida.write(value[j])
	saida.write(key[j])
	diversidade= v.count(key[j])
	div.write(str(diversidade)+'\n'+key[j]+'\n')

saida.close()
t.close()
div.close()

print ''
print 'Finish! Press Enter to Quit.'
print ''
raw_input()
