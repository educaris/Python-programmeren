import random

def rollTwoDice():
    return random.randint(1,6) + random.randint(1,6)

counters=[0.]*12

nRolls = 1000
for i in range(nRolls):
    totalValue = rollTwoDice()

    counters[totalValue-1] = counters[totalValue-1] + 1.

for i in range(len(counters)):
    counters[i] = counters[i] / float(nRolls)

print("The probabilitie of rolling a total value using two dice:")
for i in range(len(counters)):
    print("P("+str(i+1)+")="+str(counters[i]))
print("where P(n) is the probability of rolling a total value of n on two dice.")
