# -*- coding: cp1252 -*-
from func import *
from Tkinter import *
import tkFileDialog
import os
import platform
root = Tk()
root.title('P.O.D.')
root.resizable(0, 0)
if platform.system() == 'Windows':
	root.iconbitmap("POD.ico")
def creditos():
        creditos=Tk()
        creditos.title('Credits')
        labe = Label(creditos,font='Arial 18',text="Produced by Diogo Munaro Vieira and Revised By Gandra \n\nSpecial thanks to my mother and father and my little brother \nthat without then I could not finish any job.\n\nSpecial thanks to Laboratory of Molecular Biology of UFRJ \nwhere Ricardo Pilz Vieira and Orlando Bonifácio Martins give me the motivation \nto continue this program. \n\n contact: diogo.mvieira@bioqmed.ufrj.br")
        labe.pack(expand=True)
def ajuda():
        ajuda=Tk()
        ajuda.title('Help')
        labe = Label(ajuda,font='Arial 18',text="Choose your wordpad with a click on the button Open a File. \nChoose your Output wordpad name and location with a click on the button Save a File. \nChoose your Output of diversity name and location with a click on the button Save a Diversity File. \nTake a look inside the location boxes on the left to see if everything is alright. \nIf everything is correct press the Start! button and wait the process. \n\n Now your sequences are without duplicates! \n\nPlease help with the bugs! \n Enjoy!!")
        labe.pack(expand=True)

def versao():
        versao=Tk()
        versao.title('About')
        labe = Label(versao,font='Arial 18',text="Version 1.0 \n\nPhylogeny Organizer of Diversity is a FREE and OpenSource software \nthat open a wordpad document (txt, fasta, aln...) and remove duplicates and impurities for \n a post-analysis with phylogeny programs like ARB software. \n This program returns a .fasta (clear wordpad) file not aligned \nand a .txt (diversity wordpad) file with a diversity analysis.")
        labe.pack(expand=True)


principal=Menu(root)
arquivo=Menu(principal)
principal.add_command(label="About",command=versao)
principal.add_command(label="Help",command=ajuda)
principal.add_command(label="Credits",command=creditos)
root.configure(menu=principal)

entrada=StringVar(root)
entrada.set('d')
entrada1=StringVar(root)
entrada2=StringVar(root)
entrada3=StringVar(root)
l = Label(font="Arial 20 bold",text= 'Phylogeny Organizer of Diversity')
l.pack()
lab=  Label ()
lab.pack(side="top",expand=True,fill="x")
label=Label()
label.pack(side='right')

ch = Radiobutton(lab,text="DNA",font='Arial 12', value='d', variable=entrada )
ch.pack(side='left')
ch = Radiobutton(lab,text="RNA",font='Arial 12', value='r', variable=entrada )
ch.pack(side='left')
ch = Radiobutton(lab,text="Protein",font='Arial 12', value='p', variable=entrada )
ch.pack(side='left')
def abre():
        global files
        global entrada1
        files=tkFileDialog.askopenfilename(parent = root, filetypes = [('TXT', '*.txt'), ('FASTA', '*.fasta'), ('CLUSTAL', '*.aln'), ('ALL TYPES', '*')], multiple = 1 )
        files = os.path.normpath(files[0])
        entrada1.set(files)
def salva():
        global files2
        global entrada2
        files2= tkFileDialog.asksaveasfilename(parent = root, filetypes = [('FASTA (Not Aligned)', '*.fasta')])
        files2 = os.path.normpath(files2)
        if '.fasta' in files2:
                entrada2.set(files2)
        else:
                entrada2.set(files2+'.fasta')
def salvadiv():
        global files3
        global entrada3
        files3= tkFileDialog.asksaveasfilename(parent = root, filetypes = [('TXT', '*.txt')])
        files3 = os.path.normpath(files3)
        if '.txt' in files3:
                entrada3.set(files3)
        else:
                entrada3.set(files3+'.txt')

diver = Entry(textvar=entrada3,borderwidth=3,font='Arial 12', width=50)
diver.pack(side='bottom')
saida = Entry(textvar=entrada2,borderwidth=3,font='Arial 12', width=50)
saida.pack(side='bottom')
nome = Entry(textvar=entrada1,borderwidth=3,font='Arial 12', width=50)
nome.pack(side='bottom')
def inicia():
        e=nome.get()
        e2=saida.get()
        e3=diver.get()
        comeca(entrada,e,e2,e3)
i=Button(lab,text="Start!",bg='navy', fg='white',bd=2, relief=RAISED,command=inicia)
i.pack(side='right')
botao=Button(label,width=16,bd=3, relief=RAISED, pady=1,text="Open a File",command=abre)
botao.pack(side='top')
botao2=Button(label,width=16,bd=3, relief=RAISED, pady=1,text="Save a File",command=salva)
botao2.pack(side='top')
botao3=Button(label,width=16,bd=3, relief=RAISED, pady=1,text="Save a Diversity File",command=salvadiv)
botao3.pack(side='top')

mainloop()
