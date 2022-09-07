from token import NUMBER
from PySide2 import QtWidgets
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from ui_mainwindow import Ui_MainWindow
import numpy as np
from tabulate import tabulate
from colorama import init, Fore, Back, Style

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        header = self.ui.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        self.ui.pushButton.clicked.connect(self.Automata)
        

    @Slot()
    def Automata(self): 
        #Nuevas variables
        pila = []
        pila.append('2')
        pila.append('0')

        entrada = []
                    
        matrizLR = [['d2','','','1'], #0
                    ['','','r0(acept)',''], #1
                    ['','d3','r2',''], #2
                    ['d2','','','4'], #3
                    ['','','r1',''] #4
                    ]

        #Variables iniciales
        elementos=[]
        estado = 0
        indice = 0
        cadena = self.ui.textEdit.toPlainText().strip() + '$'
        while(indice<=(len(cadena)-1)  and estado==0):  
                #Se inicializan las siguientes variables
                lexema=''
                token='error'
                num=-1
                #Mientras el indice sea menor a la longitud de la cadena y NO se encuentre en el estado 20
                while(indice<=(len(cadena)-1) and estado!=20):
                    if estado==0:#Si está en el estado inicial
                        #Si en la posición cadena[indice] hay espacio en blanco
                        if(cadena[indice].isspace()):
                            estado=0 #El estado se establece como el inicial
                        #Si en la posición cadena[indice] hay una letra o un guión bajo
                        elif cadena[indice].isalpha() or cadena[indice]=='_':
                            estado=4 #La variable estado se establece con el número 4
                            lexema+=cadena[indice] #Al lexema se le agrega el contenido de cadena[indice]
                            token='identificador' #El token se define como un identificador
                            num=0 #La variable num se establece con el número 0
                            entrada.append(num)
                        #Si en la posición cadena[indice] hay un $ (fin de cadena)
                        elif cadena[indice]=='$':
                            estado=20 #Se establece el estado como el final
                            lexema+=cadena[indice] #Al lexema se le agrega el contenido de cadena[indice]
                            token='$'  #El token se define como un signo de pesos o final de cadena
                            #num=23 #La variable num se establece con el número 23
                            num=2
                            entrada.append(num)
                        elif cadena[indice].isdigit():
                            lexema+=cadena[indice]
                            token='entero'
                            estado=6 
                            num=1
                            entrada.append(num)
                        elif cadena[indice]=='"':
                            lexema+=cadena[indice]
                            estado=11
                            indice+=1
                        elif cadena[indice]=='=':
                            lexema+=cadena[indice]
                            token='='
                            estado=5  
                            num=18  
                            entrada.append(num)
                        elif cadena[indice]=='+' or cadena[indice]=='-':
                            lexema+=cadena[indice]
                            token='opSuma'
                            estado=20
                            #num=5 
                            num=1
                            entrada.append(num)
                        elif cadena[indice]=='*' or cadena[indice]=='/':
                            lexema+=cadena[indice]
                            token='opMul'
                            estado=20 
                            num=6
                            entrada.append(num)
                        elif cadena[indice]=='<' or cadena[indice]=='<=' or cadena[indice]=='>' or cadena[indice]=='>=':
                            lexema+=cadena[indice]
                            token='opRelac'
                            estado=20 
                            num=7 
                            entrada.append(num)
                        elif cadena[indice]=='||':
                            lexema+=cadena[indice]
                            token='opOr'
                            estado=20 
                            num=8
                            entrada.append(num)  
                        elif cadena[indice]=='&&':
                            lexema+=cadena[indice]
                            token='opAnd'
                            estado=20 
                            num=9
                            entrada.append(num)
                        elif cadena[indice]=='!':
                            lexema+=cadena[indice]
                            token='opNot'
                            estado=10 
                            num=10   
                            entrada.append(num)
                        elif cadena[indice]==';':
                            lexema+=cadena[indice]
                            token=';'
                            estado=20 
                            num=12 
                            entrada.append(num)
                        elif cadena[indice]==',':
                            lexema+=cadena[indice]
                            token=','
                            estado=20 
                            num=13 
                            entrada.append(num)
                        elif cadena[indice]=='(':
                            lexema+=cadena[indice]
                            token='('
                            estado=20 
                            num=14
                            entrada.append(num) 
                        elif cadena[indice]==')':
                            lexema+=cadena[indice]
                            token=')'
                            estado=20 
                            num=15
                            entrada.append(num)
                        elif cadena[indice]=='{':
                            lexema+=cadena[indice]
                            token='{'
                            estado=20 
                            num=16
                            entrada.append(num) 
                        elif cadena[indice]=='}':
                            lexema+=cadena[indice]
                            token='}'
                            estado=20 
                            num=17
                            entrada.append(num)
                        #Si NO hay un espacio en blanco o alguno de los tokens válidos       
                        else:
                            estado=20 #Se establece el estado como el final
                            token='error' #El token se define como un error
                            lexema=cadena[indice] #Al lexema se le agrega el contenido de cadena[indice]
                            num=-1 #La variable num se establece con el número -1
                        indice+=1 #Se le suma 1 a la variable indice (se pasa a la siguiente posición)
                    elif estado==4:
                        #Si en la posición cadena[indice] hay un digito, una letra o un guión bajo
                        if cadena[indice].isdigit() or cadena[indice].isalpha() or cadena[indice]=='_':
                            estado=4 #Se establece el estado como el 4
                            lexema+=cadena[indice] #Al lexema se le agrega el contenido de cadena[indice]
                            token='identificador' #El token se define como un identificador
                            indice+=1 #Se le suma 1 a la variable indice (se pasa a la siguiente posición)
                            num=0 #La variable num se establece con el número 1
                            entrada.append(num)
                        #Si en la posición cadena[indice] NO hay un digito, una letra o un guión bajo
                        else:
                            estado=20 #Se establece el estado como el final
                    elif estado==5:
                        #Si en la posición cadena[indice] NO hay un "="
                        if cadena[indice]!='=':
                            estado=20 #Se establece el estado como el final
                        #Si en la posición cadena[indice] NO hay un "="
                        else:
                            estado=20 #Se establece el estado como el final
                            lexema+=cadena[indice] #Al lexema se le agrega el contenido de cadena[indice]
                            token='opIgualdad' #El token se define como un operador de igualdad
                            indice+=1 #Se le suma 1 a la variable indice (se pasa a la siguiente posición)
                            num=11 #La variable num se establece con el número 11
                            entrada.append(num)
                    elif estado==6:
                        if cadena[indice].isdigit():
                            estado=7 
                            lexema+=cadena[indice] 
                            token='entero' 
                            indice+=1 
                            num=1 
                            entrada.append(num)
                        if cadena[indice]=='.':
                            estado=7
                            lexema+=cadena[indice]
                            indice+=1
                        else:
                            estado=20  
                    elif estado==7:
                        if cadena[indice].isdigit():
                            estado=8
                            lexema+=cadena[indice]
                            token='real'
                            indice+=1
                            num=2
                            entrada.append(num)
                        if cadena[indice]=='.':
                            estado=8
                            lexema+=cadena[indice]
                            indice+=1
                        else:
                            estado=20
                    elif estado==8:
                        if cadena[indice].isdigit():
                            estado=9
                            lexema+=cadena[indice]
                            token='real'
                            indice+=1
                            num=2
                            entrada.append(num)
                        else:
                            estado=20
                    elif estado==9:
                        if cadena[indice].isdigit():
                            estado=20
                            lexema+=cadena[indice]
                            token='real'
                            indice+=1
                            num=2
                            entrada.append(num)
                        else:
                            estado=20
                    elif estado==10:
                        if cadena[indice]!='=':
                            estado=20
                        else:
                            estado=20
                            lexema+=cadena[indice]
                            token='opIgualdad'
                            indice+=1
                            num=11
                            entrada.append(num)
                    elif estado==11:
                        if cadena[indice]=='"':
                            estado=20
                            lexema+=cadena[indice]
                            token='cadena'
                            num=3
                            entrada.append(num)
                        else:
                            while(indice<=(len(cadena)-1) and cadena[indice]!='"'): 
                                lexema+=cadena[indice]
                                token='cadena'
                                num=3
                                indice+=1
                                entrada.append(num)
                estado = 0
                elementos.append({'token':token,'num':num,'lexema':lexema})

        init(autoreset=True) 
        r1 = 'r1 = E -> id + E'
        r2 = 'r2 = E -> id'
        print("{:^85}".format(Fore.YELLOW+'Tabla LR(1)'))
        print("{:^51} {:^12}".format(Fore.GREEN+r1,Fore.GREEN+r2))
        print ("{:^15} {:^15} {:^15} {:^15} {:^15}".format('','0','1','2','3','4'))
        print ("{:^16} {:^18} {:^23} {:^17} {:^22}".format('',Fore.CYAN+'id',Fore.CYAN+'+',Fore.CYAN+'$',Fore.CYAN+'E'))
        num=0
        for v in matrizLR:
            id, mas, pesos, E = v
            print ("{:^15} {:^15} {:^15} {:^15} {:^15}".format(num, id, mas, pesos, E))
            num+=1
         
        print('\n')      
        print("{:^130}".format(Fore.YELLOW+'Análisis LR(1)'))
        print('{:^50}{:^40}{:^18}'.format(Fore.CYAN+'Pila',Fore.CYAN+'Entrada',Fore.CYAN+'Salida'))
        
        #print('{:^45}{:^35}{:^13}'.format('Pila','Entrada','Salida'))
        
        while(True):
            x = int(entrada[0])
            y = int(pila[len(pila)-1])
            
            salida = matrizLR[y][x]

            print('{:^50}{:^40}{:^18}'.format(Fore.YELLOW+str(pila),Fore.GREEN+str(entrada),Fore.MAGENTA+salida))
        
            if(salida == ''):
                print('ERROR!')
                QMessageBox.information(self,'Mensaje','Cadena rechazada!')
                break
            if(salida == 'r0(acept)'):
                QMessageBox.information(self,'Mensaje','Cadena aceptada!')
                break
            
            if(salida[0] == 'd'):
                entrada.pop(0)
                pila.append(x)
                pila.append(salida[1])
            elif(salida[0] == 'r'):
                if(salida[1] == '1'): 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][3])
                    
                    pila.append('3')
                    pila.append(aux)
                    
                    if(aux == ''):
                        print('ERROR!')
                        QMessageBox.information(self,'Mensaje','Cadena rechazada!')
                        break   
                else:
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][3])
                    
                    pila.append('3')
                    pila.append(aux)
                    
                    if(aux == ''):
                        print('ERROR!')
                        QMessageBox.information(self,'Mensaje','Cadena rechazada!')
                        break
                               
        self.ui.tableWidget.clearContents()

        row = 0
        self.ui.tableWidget.setRowCount(len(elementos))

        for elemento in elementos:
            if elemento['lexema']=="if":
                elemento['token']="if"
                elemento['num'] = 19
            elif elemento['lexema']=="else":
                elemento['token']="else"
                elemento['num'] = 22
            elif elemento['lexema']=="while":
                elemento['token']="while"
                elemento['num']=20
            elif elemento['lexema']=="return":
                elemento['token']="return"
                elemento['num']=21
            elif elemento['lexema']=="int":
                elemento['token']="tipo de dato"
                elemento['num']=4
            elif elemento['lexema']=="float":
                elemento['token']="tipo de dato"
                elemento['num']=4
            elif elemento['lexema']=="void":
                elemento['token']="tipo de dato"
                elemento['num']=4
            
            self.ui.tableWidget.setItem(row,0,QTableWidgetItem(elemento['token']))
            self.ui.tableWidget.setItem(row,1,QTableWidgetItem(str(elemento['num'])))
            self.ui.tableWidget.setItem(row,2,QTableWidgetItem(elemento['lexema']))
            row +=1  