from mergesort import *
def comeca(sequencia,entrada,entrada2,entrada3):
        div=open(entrada3,'w')
        t=open(entrada,'r')
        saida=open(entrada2,'w')
        x=t.readlines()
        if (x[-1][-1])<>'\n':
                comp=x[-1][-1]
                comp=comp+'\n'
                x.insert(-1,comp)
                comp=x[-1]
                comp=comp+'\n'
                del(x[-1])
                x.insert(-1,comp)
                del(x[-1])
        l=[]
        b=0
        t.close()
        if sequencia=='r':
                for j in range(0,len(x)):
                        k=len(x[j])
                        if x[j][0]=='>':
                                if b==1:
                                        l.append(c)
                                l.append(x[j][:k-1])
                                c=""
                                b=1
                        else:
                                y=""
                                for i in range(0,k-1):
                                        if x[j][i] == 'a' or x[j][i] == 'A' or x[j][i] == 'c' or x[j][i] == 'C' or x[j][i] == 'g' or x[j][i] == 'G' or x[j][i] == 'u' or x[j][i] == 'U' or x[j][i] == 'r' or x[j][i] == 'R' or x[j][i] == 'y' or x[j][i] == 'Y' or x[j][i] == 'k' or x[j][i] == 'K' or x[j][i] == 'm' or x[j][i] == 'M' or x[j][i] == 's' or x[j][i] == 'S' or x[j][i] == 'w' or x[j][i] == 'W' or x[j][i] == 'b' or x[j][i] == 'B' or x[j][i] == 'd' or x[j][i] == 'D' or x[j][i] == 'h' or x[j][i] == 'H' or x[j][i] == 'v' or x[j][i] == 'V' or x[j][i] == 'n' or x[j][i] == 'N':
                                                y=y+x[j][i]
                                c=c+y
                l.append(c)
        
        elif sequencia=='p':
                for j in range(0,len(x)):
                        k=len(x[j])
                        if x[j][0]=='>':
                                if b==1:
                                        l.append(c)
                                l.append(x[j][:k-1])
                                c=""
                                b=1
                        else:
                                y=""
                                for i in range(0,k-1):
                                        if x[j][i] == 'a' or x[j][i] == 'A' or x[j][i] == 'c' or x[j][i] == 'C' or x[j][i] == 'g' or x[j][i] == 'G' or x[j][i] == 'v' or x[j][i] == 'V' or x[j][i] == 'L' or x[j][i] == 'l' or x[j][i] == 'I' or x[j][i] == 'i' or x[j][i] == 'S' or x[j][i] == 's' or x[j][i] == 'T' or x[j][i] == 't' or x[j][i] == 'Y' or x[j][i] == 'y' or x[j][i] == 'M' or x[j][i] == 'm' or x[j][i] == 'd' or x[j][i] == 'D' or x[j][i] == 'n' or x[j][i] == 'N' or x[j][i] == 'E' or x[j][i] == 'e' or x[j][i] == 'Q' or x[j][i] == 'q' or x[j][i] == 'R' or x[j][i] == 'r' or x[j][i] == 'K' or x[j][i] == 'k' or x[j][i] == 'H' or x[j][i] == 'h' or x[j][i] == 'F' or x[j][i] == 'f' or x[j][i] == 'W' or x[j][i] == 'w' or x[j][i] == 'P' or x[j][i] == 'p' or x[j][i] == 'b' or x[j][i] == 'B' or x[j][i] == 'z' or x[j][i] == 'Z' or x[j][i] == 'x' or x[j][i] == 'X' or x[j][i] == 'u' or x[j][i] == 'U':
                                                y=y+x[j][i]
                                c=c+y
                l.append(c)

        else:
                for j in range(0,len(x)):
                        k=len(x[j])
                        if x[j][0]=='>':
                                if b==1:
                                        l.append(c)
                                l.append(x[j][:k-1])
                                c=""
                                b=1
                        else:
                                y=""
                                for i in range(0,k-1):
                                        if x[j][i] == 'a' or x[j][i] == 'A' or x[j][i] == 'c' or x[j][i] == 'C' or x[j][i] == 'g' or x[j][i] == 'G' or x[j][i] == 't' or x[j][i] == 'T' or x[j][i] == 'r' or x[j][i] == 'R' or x[j][i] == 'y' or x[j][i] == 'Y' or x[j][i] == 'k' or x[j][i] == 'K' or x[j][i] == 'm' or x[j][i] == 'M' or x[j][i] == 's' or x[j][i] == 'S' or x[j][i] == 'w' or x[j][i] == 'W' or x[j][i] == 'b' or x[j][i] == 'B' or x[j][i] == 'd' or x[j][i] == 'D' or x[j][i] == 'h' or x[j][i] == 'H' or x[j][i] == 'v' or x[j][i] == 'V' or x[j][i] == 'n' or x[j][i] == 'N':
                                                y=y+x[j][i]
                                c=c+y
                l.append(c)
        
        dec,dic={},{}
        for j in range(0,len(l),2):
                alta=(l[j+1]).upper()
                del(l[j+1])
                l.insert(j+1,alta)
                if (dic.has_key((l[j+1][::-1])))==True:
                        del(l[j+1])
                        l.insert((j+1),alta[::-1])
                d={l[j]:l[j+1]}
                dec.update(d)
                d={l[j+1]:l[j]}
                dic.update(d)
        vou=dic.keys()
        v=dec.values()
        diversidade=[]                
        dic={}
        for j in range(0,len(l),2):
                alta=(l[j+1])     
                divo=(len(alta))/65
                if divo > 0:
                        alta2=''
                        for h in range(1,divo+1):
                                alta2=alta2+alta[(65*(h-1)):(65*h)]+'\n'
                        alta=alta2+alta[65*divo:]
                del(l[j+1])
                l.insert(j+1,alta)
                d= {alta:l[j]}
                dic.update(d)

        key=dic.keys()
        value=dic.values()

        for j in range(len(key)):
                saida.write(value[j]+'\n'+key[j]+'\n')
                diversidade.append((v.count(vou[j])))
        saida.close()
        ordena(diversidade, value, key, div)
        div.close()
