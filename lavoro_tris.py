print("ciao! ora faremo una bellissima partita a tris")
print("gioco realizzato da Paola e Rebecca con molta soddisfazione!")
print(" ecco la modalità di gioco")
print(" dovrai utilizzare il tastierino numerico presente sulla tastiera del computer (si trova a destra)")
print(" infatti ogni numero corrisponde alla sua posizione nella scacchiera")
print("(es: 7= in alto a sinistra)")
print("adesso trova un compagno di gioco e divertitevi insieme :)")
print("buona fortuna e che vinca il migliore!!")
 
tavola  = { '7' : '' , '8' : '' , '9' : '' ,
            '4' : '' , '5' : '' , '6' : '' ,
            '1' : '' , '2' : '' , '3' : '' }
 
scacchiera  = []
 
for  chiavi  in  scacchiera :
    scacchiera.append (chiavi)
 
 
def  printBoard (laTavola):  
    print ( laTavola [ '7' ] +  '  |  '  +  laTavola [ '8' ]  +  ' |  '  +  laTavola [ '9' ])
    print ( '- + - + -' )
    print ( laTavola [ '4' ] +  '  |  '  +  laTavola [ '5' ]  +  ' |  '  +  laTavola [ '6' ])
    print ( '- + - + -' )
    print ( laTavola [ '1' ] +  '  |  '   +  laTavola [ '2' ] +  ' |  '  +  laTavola [ '3' ])
 
 
def  gioco ():
 
    turno  =  'X'
    punti  =  0
 
    for i  in  range ( 10 ):
        printBoard (tavola)
        print ( "Tocca a te " + str( turno ) + " , che casella scegli?" )
 
        mossa= input ()        
 
        if  tavola [ mossa ] ==  '' :
            tavola [ mossa ] =  turno
            punti  +=  1
 
        else :
            print ( "Quella casella è già occupata. in che casella vuoi spostarti?" )
            continue
 
 
        if  punti  >=  5 :
 
            if  tavola [ '7' ] ==  tavola [ '8' ] ==  tavola [ '9' ] !=  '' : # in alto
                printBoard ( tavola )             
                print ( "wow " + turno  +  " ,hai vinto!!!!" )                
                break
 
            elif  tavola [ '4' ] ==  tavola [ '5' ] ==  tavola [ '6' ] !=  '' : # al centro
                printBoard ( tavola )                
                print ( "wow " + turno  +  " ,hai vinto!!!!" )
                break
 
            elif  tavola [ '1' ] ==  tavola [ '2' ] ==  tavola [ '3' ] !=  '' : # in fondo
                printBoard ( tavola )                
                print ("wow " + turno  +  " ,hai vinto!!!!" )
                break
 
            elif  tavola [ '1' ] ==  tavola [ '4' ] ==  tavola [ '7' ] !=  '' : # sul lato sinistro
                printBoard ( tavola )                
                print ( "wow " + turno  +  " ,hai vinto!!!!")
                break
 
            elif  tavola [ '2' ] ==  tavola [ '5' ] ==  tavola [ '8' ] !=  '' : # al centro
                printBoard ( tavola )                
                print ( "wow " + turno  +  " ,hai vinto!!!!" )
                break
 
            elif  tavola [ '3' ] ==  tavola [ '6' ] ==  tavola [ '9' ] !=  '' : # sul lato destro
                printBoard ( tavola )                
                print ( "wow " + turno  +  " ,hai vinto!!!!" )
                break
 
            elif  tavola [ '7' ] ==  tavola [ '5' ] ==  tavola [ '3' ] !=  '' : # diagonale
                printBoard ( tavola )                
                print ( "wow " + turno  +  " ,hai vinto!!!!" )
                break
 
            elif  tavola [ '1' ] ==  tavola [ '5' ] ==  tavola [ '9' ] !=  '' : # diagonale
                printBoard ( tavola )       
                print ( "wow " + turno  +  " ,hai vinto!!!!")
                break 
 
      
        if  punti  ==  9 :                
            print ( "È un pareggio !!" )
            break
 
       
        if  turno  == 'X' :
            turno =  'O'
        else : 
            turno =  'X'        
    
 
 
 
if  __name__  ==  "__main__" :
    gioco ()


