import random


table = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
joueurActuel = "X"
gagnant = None
en_Jeux = True

# game table
def printtable(table):
    print(table[0] + " | " + table[1] + " | " + table[2])
    print("---------")
    print(table[3] + " | " + table[4] + " | " + table[5])
    print("---------")
    print(table[6] + " | " + table[7] + " | " + table[8])

# switch player
def switchJoueur():
    global joueurActuel
    if joueurActuel == "X":
        joueurActuel = "O"
    else:
        joueurActuel = "X"


# entree 
def playerentreeut(table):
    entree = int(input("--------choisir entre 1-9:"))
    if table[entree-1] == "-":
        table[entree-1] = joueurActuel
        switchJoueur()
    else:
        print("-------place non vide, reessayer-------")


# checker si gain ou tie
def checkHorizontal(table):
    global gagnant
    if table[0] == table[1] == table[2] and table[0] != "-":
        gagnant = table[0]
        return True
    elif table[3] == table[4] == table[5] and table[3] != "-":
        gagnant = table[3]
        return True
    elif table[6] == table[7] == table[8] and table[6] != "-":
        gagnant = table[6]
        return True


def checkRow(table):
    global gagnant
    if table[0] == table[3] == table[6] and table[0] != "-":
        gagnant = table[0]
        return True
    elif table[1] == table[4] == table[7] and table[1] != "-":
        gagnant = table[1]
        return True
    elif table[2] == table[5] == table[8] and table[2] != "-":
        gagnant = table[3]
        return True


def checkDiag(table):
    global gagnant
    if table[0] == table[4] == table[8] and table[0] != "-":
        gagnant = table[0]
        return True
    elif table[2] == table[4] == table[6] and table[4] != "-":
        gagnant = table[2]
        return True


def checkGain(table):
    global en_Jeux
    if checkHorizontal(table):
        printtable(table)
        print(f"------le gagnant est {gagnant}!--------")
        en_Jeux = False

    elif checkRow(table):
        printtable(table)
        print(f"--------le gagnant est {gagnant}!--------")
        en_Jeux = False

    elif checkDiag(table):
        printtable(table)
        print(f"--------le gagnant est {gagnant}!--------")
        en_Jeux = False


def checkTie(table):
    global en_Jeux
    if "-" not in table:
        printtable(table)
        print("--------c'est une tie!--------")
        continuer=input("---pour recommencer cliquer n'importe ou\n --- pour quitter taper 'q'")
        if continuer == 'q':
            en_Jeux = False
        else:
            table = ["-", "-", "-",
                    "-", "-", "-",
                    "-", "-", "-"]


def Bot(table):
    while joueurActuel == "O":
        position = random.randint(0, 8)
        if table[position] == "-":
            table[position] = "O"
            switchJoueur()


while en_Jeux:
    printtable(table)
    playerentreeut(table)
    checkGain(table)
    checkTie(table)
    Bot(table)
    checkGain(table)
    checkTie(table)