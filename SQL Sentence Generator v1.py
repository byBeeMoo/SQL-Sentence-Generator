import random
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter.ttk import Progressbar


def readColumnNames():
    listOfColumns = "Starter value"
    finished = False

    while (not finished):
       
        listOfColumns = input("Give your columns names separated by commas, to finish type -> end <- [word,word,end]: ").split(",") 
        for i in listOfColumns:
            if (i == "end"):
                listOfColumns.pop(len(listOfColumns))
                finished = not finished
    return listOfColumns

def readDataTypes():
    listOfDataTypes = "Starter value"
    finished = False

    while (not finished):
       
        listOfDataTypes = input("Give your columns names separated by commas, to finish type -> end <- [word,word,end]: ").split(",") 
        for i in listOfDataTypes:
            if (i == "end"):
                listOfDataTypes.pop(len(listOfDataTypes))
                finished = not finished
    return listOfDataTypes


## idFactura    int(6) not null
def createListOfIdsFactura(desideredRange):
    vectorOfIntegers = []
    
    for i in range(0, desideredRange):
        vectorOfIntegers.append(i)
        
    return vectorOfIntegers

## Guardem la llista generada
def chooseIdFactura(vectorOfIntegers):
## Escollim un id Random dins de la llista de ID's
    idFactura = random.choice(vectorOfIntegers)

## Esborrem l'element de la llista que ens ha retornat la funcio anterior per a tal de que no es repeteixi en una altra tupla
    for i in range((len(vectorOfIntegers) - 1)):
        if (vectorOfIntegers[i] == idFactura):
            del vectorOfIntegers[i]
    return idFactura

## dataFactura date YYYY MM DD
def createDate():
    dataFactura = str(random.randint(1900,2020))
    dataFactura += "-"
    dataFactura += str(random.randint(1,12))
    dataFactura += "-"
    dataFactura += str(random.randint(0,28))
    
    return dataFactura

## IVAFactura int(2) choice(21%,10%,4%) null
def chooseIvaFactura():
    return random.choice([21, 10, 4])

## dteFactura int(2) choice (10%, 20%, 30%, 40%, 50%) null
def chooseDteFactura():
    return random.choice([10, 20, 30, 40, 50])

## idVenedor int(5) not null
def chooseIdVenedor():
    return random.randint(0,99999)

## idClient int(5) not null
def chooseIdClient():
    return random.randint(0,99999)












## Demanem a l'usuari per a quina taula vol generar sentencies SQL
def insertTableName(posicioNomTaula):
    opcions = ['article', 'client', 'factura',
                     'liniafactura', 'poble', 'provincia', 'venedor']
    nomDeLaTaula = opcions[posicioNomTaula - 1]
##    index = 0
##
##    while nomDeLaTaula != opcions[index]:
##       nomDeLaTaula = input('Introdueix el nom de la taula: ').casefold()
##    
##        for i in range((len(opcions) - 1)):
##            if(nomDeLaTaula == opcions[i]):
##                index = i
##               
    return nomDeLaTaula




## El usuari introdueix el numero de tuples que voldra generar, el bucle acaba quan s'introdueix un numero (el iterador es modifica)
##def insertNumberOfColumns():
##    iterator = 1
##    while iterator == 1:
##        try:
##            numberOfLines = int(input('Introdueix el nombre de tuples a generar: '))
##            iterator = 0
##        except ValueError:
##            print("Not a number")
##        
##    return numberOfLines




    
## Creem i insertem al fitxer la primera linea que defineix que estem fent
def createFileAndChooseSqlSentence(nomDeLaTaula, opcioGUI):
    file = open("dades.sql", "w+")
   
   
    if(opcioGUI == 1):
        file.write("CREATE TABLE " + nomDeLaTaula + "(\n")
        
    elif(opcioGUI == 2):
        file.write("ALTER TABLE " + nomDeLaTaula + "\n")
        
    elif(opcioGUI == 3):
        file.write("INSERT INTO " + nomDeLaTaula + "\n"
            + "\t VALUES")
        
    elif(opcioGUI == 4):
        file.write("UPDATE " + nomDeLaTaula + "\n")
    
    return file

## Funcio de creació de tuples
def createSqlTuple(idFactura, dataFactura, IVAFactura, dteFactura, idVenedor, idClient):
    tupla = (idFactura, dataFactura, IVAFactura, dteFactura, idVenedor, idClient);
    
    return tupla
    

## El loop que procedirà a la creació de les senténcies SQL
def createSqlSentences(file, tupla, i, numberOfLines):
    if(i != 0):
        file.write("\t\t")
    if (i != (numberOfLines - 1)):
        file.write(str(tupla) + ",\n")
    else:
        file.write(str(tupla) + "\n")
    ## file.close()



## ------------------------  PROGRAMA MAIN  ---------------------------------- ##
def run(opcioGUI, posicioNomTaula, numberOfLines):
    ## Creem el fitxer sql
    
    nomDeLaTaula = insertTableName(posicioNomTaula)

    file = createFileAndChooseSqlSentence(nomDeLaTaula, opcioGUI)
    defaultMaxRangeForIdsFactura = 2501
    vectorOfIntegers = createListOfIdsFactura(defaultMaxRangeForIdsFactura)


    for i in range(numberOfLines):
        idFactura = chooseIdFactura(vectorOfIntegers)
        dataFactura = createDate()
        ivaFactura = chooseIvaFactura()
        dteFactura = chooseDteFactura()
        idVenedor = chooseIdVenedor()
        idClient = chooseIdClient()
        tupla = createSqlTuple(idFactura, dataFactura, ivaFactura, dteFactura, idVenedor, idClient)
        createSqlSentences(file, tupla, i, numberOfLines)
    
    file.close()
    
        
        
        
        
        
        
def clicked():
    opcioGUI = int(selected.get())
    posicioNomTaula = int(taula.get())
    try:
        numberOfLines = int(txtTuples.get())
        run(opcioGUI, posicioNomTaula, numberOfLines)
        while bar['value'] != 100:
            bar['value'] +=1
        if(opcioGUI != 0 and posicioNomTaula != 0 and numberOfLines != 0):
            messagebox.showinfo('Enhorabona!','El fixer ha estat creat i desat en el mateix directori del programa amb el nom \'dades.sql\'')
            tk.destroy()
    except ValueError:
        messagebox.showerror('Error de tipus','El valor introduit en \'numero de tuples a crear\' es incorrecte.')
        
tk = tkinter.Tk()
tk.title("SQL Tuple Generator")
tk.geometry('550x550')

## mainFrame = Frame(tk, borderwidth = 2)
## mainFrame.pack(side=LEFT, expand=1, fill=BOTH)

lblSqlSentence = Label(tk, text="Escull una opció: ", font=("Times New Roman", 14))
lblSqlSentence.grid(column=0, row=0)


selected = IntVar()

radCreate = Radiobutton(tk, text='CREATE TABLE', value=1, var=selected)
radCreate.grid(column=0, row=1)

radAlter = Radiobutton(tk, text='ALTER TABLE', value=2, var=selected)
radAlter.grid(column=1, row=1)

radInsert = Radiobutton(tk, text='INSERT INTO', value=3, var=selected)
radInsert.grid(column=0, row=2)

radUpdate = Radiobutton(tk, text='UPDATE TABLE', value=4, var=selected)
radUpdate.grid(column=1, row=2)




lablTaula= Label(tk, text="Escull per quina taula vols generar dades: ", font=("Times New Roman", 14))
lablTaula.grid(column=0, row=3)


taula = IntVar()

radArticle = Radiobutton(tk, text='Article', value=1, var=taula)
radArticle.grid(column=0, row=4)

radClient = Radiobutton(tk, text='Client', value=2, var=taula)
radClient.grid(column=1, row=4)

radFactura = Radiobutton(tk, text='Factura', value=3, var=taula)
radFactura.grid(column=0, row=5)

radLiniaFactura = Radiobutton(tk, text='LiniaFactura', value=4, var=taula)
radLiniaFactura.grid(column=1, row=5)

radUpdate = Radiobutton(tk, text='Poble', value=5, var=taula)
radUpdate.grid(column=0, row=6)

radUpdate = Radiobutton(tk, text='Provincia', value=6, var=taula)
radUpdate.grid(column=1, row=6)

radUpdate = Radiobutton(tk, text='Venedor', value=7, var=taula)
radUpdate.grid(column=0, row=7)



lablColumnes = Label(tk, text="Escull quantes tuples vols crear (MAX 2500): ", font=("Times New Roman", 14))
lablColumnes.grid(column=0, row=8)



txtTuples = Entry(tk,width=20, font=("Times New Roman", 14))
txtTuples.grid(column=0, row=9)



btn = Button(tk, text="Continua", command=clicked)
btn.grid(column=1, row=9)


bar = Progressbar(tk, length=200)
bar['value'] = 0

bar.grid(column=0, row=10)

if bar['value'] == 101:
    tk.destroy()
tk.mainloop()











