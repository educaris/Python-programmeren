from random import choice

spelers = ['Donald', 'Kwik', 'Kwek', 'Kwak', 'Dagobert', 'Guus', 'Katrien', 'Govert', 'Gijs']
print(spelers)

teamA = []
teamB = []

while len(spelers) > 0:
    spelerA = choice(spelers)
    teamA.append(spelerA)
    spelers.remove(spelerA)

    if spelers == []:
        break

    spelerB = choice(spelers)
    teamB.append(spelerB)
    spelers.remove(spelerB)

print('Team A: ', teamA)
print('Team B: ', teamB)