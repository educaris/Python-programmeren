# Hier hebben we een klassiek "steen, papier, schaar" spel. Je kent dat vast wel. Nu maken we het op de computer
# We hebben de random bibliotheek nodig om de computer een willekeurige keuze te laten maken. Deze moeten we importeren
# We hebben alleen het commando randint nodig:

from random import randint

# We laten de speler input geven in het spel. De speler mag kiezen tussen r, p of s. Het commando input zorgt er voor
# dat het programma wacht totdat de speler die input geeft:

player = input('rock (r), paper (p), of scissors (s)?')

# Hier kiest de computer. Hij paket een willekeurig getal 1, 2 of 3. Daaronder staat wat de verschillende getallen zijn

gekozen = randint(1,3)

if gekozen == 1:
    computer = 'r'                # De 1 staat dus voor 'r' oftewel rock

elif gekozen == 2:
    computer = 'p'                # De 2 staat voor 'p' oftewel paper

else:
    computer = 's'                # Dit is de 3, omdat dat de laatste keuze is kunnen we dat zo weergeven

print(player, 'vs', computer)     # Hier printen we de twee gekozen inputs, dus die van de speler en die van de computer

# Hier onder krijgen we de verschillende combinaties van de drie keuzes. In sommige gevallen wint de speler, en in
# sommige gevallen wint de computer. In 1 geval is het gelijk.

if player == computer:
    print('GELIJK!')

elif player == 'r' and computer == 's':
    print('Speler wint!')

elif player == 'r' and computer == 'p':
    print('computer wint!')

elif player == 'p' and computer == 'r':
    print('Speler wint!')

elif player == 'p' and computer == 's':
    print('computer wint!')

elif player == 's' and computer == 'p':
    print('Speler wint!')

elif player == 's' and computer == 'r':
    print('computer wint!')