calc_on = 1

def quit():
         global calc_on
         calc_on = 0

def optellen():
    eerste = float(raw_input("Wat is het eerste getal dat ik moet optellen?"))
    tweede = float(raw_input("Wat is het tweede getal dat ik moet optellen?"))
    print (eerste + tweede)

def aftrekken():
    eerste = float(raw_input("Wat is het eerste getal?"))
    tweede = float(raw_input("Wat is het tweede getal?"))
    print (eerste - tweede)

def vermenigvuldigen():
    eerste = float(raw_input("Wat is het eerste getal?"))
    tweede = float(raw_input("Wat is het tweede getal?"))
    print (eerste * tweede)

def delen():
    eerste = float(raw_input("Wat is het eerste getal?"))
    tweede = float(raw_input("Wat is het tweede getal?"))
    print (eerste / tweede)

def modulo():
    eerste = float(raw_input("Wat is het eerste getal?"))
    tweede = float(raw_input("Wat is het tweede getal?"))
    print (eerste % tweede)

def tellen_tot_10():
    for n in range (1, 10001):
        print (n)

def calc_run():
    op = raw_input("optellen, aftrekken, vermenigvuldigen, delen, modulo, tellen of stoppen? ")
    if op == "optellen":
        optellen()
    elif op == "aftrekken":
        aftrekken()
    elif op == "vermenigvuldige":
        vermenigvuldigen()
    elif op == "delen":
        delen()
    elif op == "modulo":
        modulo()
    elif op == "tellen":
        tellen_tot_10()
    else:
        print("Tot ziens")
        quit()
while calc_on == 1:
    calc_run()
