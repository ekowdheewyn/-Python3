#THIS IS THE GHANAIAN WAY OF PLAYING CARDS
# A DECK OF 32 CARDS IS DEALT RANDOMLY BETWEEN TWO PLAYERS
# USER AND CPU.

# WITH EACH PLAYER HAVING 5 CARDS IN HAND.

#THERE ARE FIVE ROUNDS PLAYED IN EACH GAME.

# THE USER PLAYS FIRST BY SELECING A CARD FROM HIS HAND
# THE CPU THEN SELECTS A CARD WITH THE SAME HOUSE.

# FOR EXAMPLE IF A USER PLAYS "8H" WHICH IS THE EIGHT OF HEARTS
# THE THE CPU MUST PLAY A HEART FROM ITS HAND
# IF THE CPU DOESN'T HAVE A HOUSE OF HEARTS IN HIS HAND
# IT WILL THEN PLAY THE FIRST CARD IN ITS HAND.

# THE LEADING PLAYER IS SELECTED BY LOOKING AT THE HIGHEST CARD ON BOARD.

# FOR EXAMPLE IF 8H IS PLAYED BY THE USER AND THE CPU SELECTS AND PLAYS
# 6H, THEN THE LEADING PLAYER IN THIS CASE WILL BE THE USER
# SINCE 8H IS GREATER THAN 6H IN A DECK OF CARDS.

# HOWEVER IF THE CPU DOESN'T PLAY A HEART TO COUNTER THE 8H PLAYED BY THE USER
# THEN AUTOMATICALLY THE USER LEADS.

# A LEADING PLAYER IS ALLOWED TO PLAY A NEW CARD FROM HIS HAND OF CARDS.

# ANYTIME A PLAYER PLAYS A CARD FROM HIS HAND THE CARD IS REMOVED FROM THE HAND.

# WHEN THE CPU LEADS A ROUND, IT WILL HAVE TO PLAY A CARD FROM ITS HAND.
# THIS IS DONE BY SELECTING A RANDOM CARD FROM ITS HAND.

# THE USER CAN NOW DECIDE TO PLAY THE SAME HOUSE AS THE CPU PLAYED
# OR PLAY A DIFFERENT CARD IF NO HOUSE OF THE SAME TYPE OF CARD IS AVAILABLE IN HAND.

# THE WINNER OF THE GAME IS DECEIDED AT THE END OF THE 5TH ROUND.
# THE LEADER OF THE 5TH ROUND WOULD BE DECLARED AS THE WINNER OF THE GAME#

#LEGEND
# C = CLUB
# H = HEART
# S = SPADE
# D = DIAMOND
# MAGNITUDE OF CARDS: K>Q>J>10>9>8>7>6 #

###begining of code###
import random

n = 0
moves = 0

def chosewinner(cpulead):
    if (cpulead == True):
        print("CPU WON")
        exit()
    else:
        print("YOU WON")
        exit()

def cpumove(cpulead):
    global am 
    global bm
    global n
    cpun = cpu[n]
    if (cpulead == True):
        k = random.randrange(len(cpu))
        cpun = cpu[k]
        print("cpu played: ", cpun)
        cpulist=list(cpu[k])
        bm = cpulist[len(cpulist)-1]
        cpu.remove(cpu[cpu.index(cpun)])
        userchoice(cpulead, cpun)
        
    else:
        usrlist = list(usr)
        am = usrlist[len(usrlist)-1]
        cpun = cpu[n]
        cpulist=list(cpun)
        bm = cpulist[len(cpulist)-1]
        if(bm==am):
            cpun = cpu[n]
            print("cpu played: ", cpun)
            cpu.remove(cpu[cpu.index(cpun)])
            n = 0
            checklead(cpun, am, bm, cpulead)
        else:
            if(n < len(cpu)-1):
                n=n+1
                cpumove(cpulead)
            else:
                cpun = cpu[0]
                print("cpu played: ", cpun)
                cpu.remove(cpu[cpu.index(cpun)])
                n = 0
                checklead(cpun, am, bm, cpulead)
    return(cpun, am, bm)
    
def checklead(cpun, am, bm, cpulead):
    global moves
    bb=cpun
    usrlist = list(usr)
    cpulist = list(bb)
    a = usrlist[len(usrlist)-2]
    b = cpulist[len(cpulist)-2]
    
    if (am != bm):
        if(cpulead == False):
            print("user leads")
            cpulead = False
            moves = moves + 1
            if (moves == 5):
                chosewinner(cpulead)
            else:
                userchoice(cpulead, cpun)
        else:
            print("cpuleads")
            cpulead = True
            moves = moves + 1
            if (moves == 5):
                chosewinner(cpulead)
            else:
                cpumove(cpulead)
    else:
        aind=her.index(a)
        bind=her.index(b)
        if(aind > bind):
            print("user leads")
            cpulead = False
            moves = moves + 1
            if (moves == 5):
                chosewinner(cpulead)
            else:
                userchoice(cpulead, cpun)
        else:
            print("cpu leads")
            cpulead = True
            moves = moves + 1
            if (moves == 5):
                chosewinner(cpulead)
            else:
                cpumove(cpulead)
    return(cpulead, cpun)

def userchoice(cpulead, cpun):
    global usr
    if (cpulead == True):
        print("Select a Card from your hand to Play:")
        usr = input()
        while usr in user:
                usrlist = list(usr)
                am = usrlist[len(usrlist)-1]
                user.remove(user[user.index(usr)])
                print("New Cards in hand:", user)
                checklead(cpun, am, bm, cpulead)  
        print("played card not in hand")
        userchoice(cpulead)
    else:
        print("Select a Card from your hand to Play:")
        usr = input()
        while usr in user:
            print("user played: ", usr)
            user.remove(user[user.index(usr)])
            print("New Cards in hand:", user)
            cpumove(cpulead)   
        print("played card not in hand")
        userchoice(cpulead, cpun)
    return(cpun)

def spit():
    print("Your hand: ",user)
    cpun = ""
    cpulead = False
    userchoice(cpulead, cpun)
    return(cpulead)

her = ["6","7","8","9","0","j","q","k"]
cards = ["6h","7h","8h","9h","10h","jh","qh","kh"
            ,"6d","7d","8d","9d","10d","jd","qd","kd"
            ,"6s","7s","8s","9s","10s","js","qs","ks"
            ,"6c","7c","8c","9c","10c","jc","qc","kc"]

a = cards[random.randrange(32)]
b = cards[random.randrange(32)]
c = cards[random.randrange(32)]
d = cards[random.randrange(32)]
e = cards[random.randrange(32)]
a1 = cards[random.randrange(32)]
b1 = cards[random.randrange(32)]
c1 = cards[random.randrange(32)]
d1 = cards[random.randrange(32)]
e1 = cards[random.randrange(32)]
user=[]
cpu=[]

while (a==b or a==c or a==d or a==e or b==c or b==d or b==e or c==d or c==e or d==e
        or a1==b1 or a1==c1 or a1==d1 or a1==e1 or b1==c1 or b1==d1 or b1==e1 or c1==d1 or c1==e1 or d1==e1
        or a1==b or a1==c or a1==d or a1==e or b1==c or b1==d or b1==e or c1==d or c1==e or d1==e
        or a==b1 or a==c1 or a==d1 or a==e1 or b==c1 or b==d1 or b==e1 or c==d1 or c==e1 or d==e1
        or a1==a or b1==b or c1==c or d1==d or e1==e):
    a = cards[random.randrange(32)]
    b = cards[random.randrange(32)]
    c = cards[random.randrange(32)]
    d = cards[random.randrange(32)]
    e = cards[random.randrange(32)]
    a1 = cards[random.randrange(32)]
    b1 = cards[random.randrange(32)]
    c1 = cards[random.randrange(32)]
    d1 = cards[random.randrange(32)]
    e1 = cards[random.randrange(32)]

user = [a,b,c,d,e]
cpu = [a1,b1,c1,d1,e1]
spit()
