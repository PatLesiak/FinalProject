


kolo=[]
kolo.append("        ----        ")
kolo.append("     -        -     ")
kolo.append("   -            -   ")
kolo.append("   -            -   ")
kolo.append("   -            -   ")
kolo.append("     -        -     ")
kolo.append("        ----        ")

krzyzyk=[]
krzyzyk.append("      \      /      ")
krzyzyk.append("       \    /       ")
krzyzyk.append("        \  /        ")
krzyzyk.append("         ||         ")
krzyzyk.append("        /  \        ")
krzyzyk.append("       /    \       ")
krzyzyk.append("      /      \      ")

puste=[]
puste.append("                    ")
puste.append("                    ")
puste.append("                    ")
puste.append("                    ")
puste.append("                    ")
puste.append("                    ")
puste.append("                    ")


# In[2]:


a1=puste
a2=puste
a3=puste
b1=puste
b2=puste
b3=puste
c1=puste
c2=puste
c3=puste


# In[3]:


j=0
kolekcja=[]
while(j<9):
    if(j%2==0):
        print('Pierwszy gracz')
        x=input('Wprowadź pierwszą współrzędną (A, B, C): ')
        y=input('Wprowadź drugą współrzędną (1, 2, 3): ')
        figura=krzyzyk
    else:
        print('Drugi gracz')
        x=input('Wprowadź pierwszą współrzędną (A, B, C): ')
        y=input('Wprowadź drugą współrzędną (1, 2, 3): ')
        figura=kolo

    element=x+y
    if(element in kolekcja):
        print("Wprowadź poprawne dane")
        continue
    kolekcja.append(element)

    if(x=='A'):
        if(y=='1'):
            a1=figura
        elif(y=='2'):
            a2=figura
        elif(y=='3'):
            a3=figura
        else:
            print("Wprowadź poprawne dane")
            continue
    elif(x=='B'):
        if(y=='1'):
            b1=figura
        elif(y=='2'):
            b2=figura
        elif(y=='3'):
            b3=figura
        else:
            print("Wprowadź poprawne dane")
            continue
    elif(x=='C'):
        if(y=='1'):
            c1=figura
        elif(y=='2'):
            c2=figura
        elif(y=='3'):
            c3=figura
        else:
            print("Wprowadź poprawne dane")
            continue
    else:
        print("Wprowadź poprawne dane")
        continue
    i=0
    a=7
    print("          A                    B                    C          ")
    while(i<a):
        if(i-3%7==0):
            print("1{}|{}|{}".format(a1[i],b1[i],c1[i]))
            pass
    print(" {}|{}|{}".format(a1[i],b1[i],c1[i]))
    i=i+1
    print(" --------------------+--------------------+--------------------")
    i=0
    while(i<a):
        if(i-3%7==0):
            print("2{}|{}|{}".format(a2[i],b2[i],c2[i]))
            pass
        print(" {}|{}|{}".format(a2[i],b2[i],c2[i]))
        i=i+1
    print(" --------------------+--------------------+--------------------")
    i=0
    while(i<a):
        if(i-3%7==0):
            print("3{}|{}|{}".format(a3[i],b3[i],c3[i]))
            pass
        print(" {}|{}|{}".format(a3[i],b3[i],c3[i]))
        i=i+1
    j=j+1
    if((a1==figura and a2==figura and a3==figura) or (b1==figura and b2==figura and b3==figura) or (c1==figura and c2==figura and c3==figura) or (a1==figura and b1==figura and c1==figura) or (a2==figura and b2==figura and c2==figura) or (a3==figura and b3==figura and c3==figura) or (a1==figura and b2==figura and c3==figura) or (a3==figura and b2==figura and c1==figura)):
        print('Wygrałeś')
        win=1
        break
if(win!=1):
    print('Remis')




