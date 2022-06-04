import random

#Local variables
attemptsTotal = 0
attemptsActual = 0
guess = []


#Functions
def toList(listString):
    myGuess = []
    
    for i in range(len(listString)):
        if not listString[i].isdigit() or listString[i]=='0':
            continue
        if listString[i].isdigit() and not listString[i+1].isdigit():
            myGuess.append(int(listString[i]))
        if listString[i].isdigit() and listString[i+1].isdigit():
            myGuess.append(int(listString[i]+listString[i+1]))
        
    return myGuess


#Main
print('Hola campeón. Vamos a jugar')
print('Déjame que piense ... hummm ... ya he elegido la lista de números')

for i in range(5):
    guess.append(random.randint(1,10))

attemptsTotal = int(input("Bien, ahora dime cuántos intentos quieres para adivinar: "))
print('Recuerda que has de introducir tu respuesta en el formato propuesto -> [x,x,x,x,x], donde x son tus números del 1 al 10.')


while(attemptsActual<attemptsTotal):
    result = [0,0,0,0,0]
    counter = 0
    listString = input('Adivínala: ')
    if listString=='respuestas':
        print('La solución es ', guess)
    else:
        myGuess = toList(listString)
    
        for i in range(len(guess)):
           if guess[i]==myGuess[i]:
                result[i]=1
                counter+=1

    
        attemptsActual+=1
        print('Mi respuesta es: ', result)
  
    
        if counter==5:
            print('Felicidades!! Ganaste a la IA')
            attemptsActual=attemptsTotal

if attemptsActual==attemptsTotal and not counter==5:
    print('Has gastado todos tus intentos :( Gana la IA')
