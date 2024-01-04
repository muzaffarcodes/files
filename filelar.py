# File'lar bilan ishlash
# Problem1
try:        
    st = open("/home/muzaffar/Desktop/Homework/Straus.txt",'a')
    
    st.write("Straus nega kemading, bugun?!\n")
    
    st.close()
except:
     print("Nimadir Xato ukam!")

#%% Problem2
try: 
    with open("/home/muzaffar/Desktop/Python_Files/NeymarJR", 'a') as ny10:
        ny10.write(""" -- Neymar JR10 --
"Neymar da Silva Santos Júnior, known as Neymar,
is a Brazilian professional footballer who plays as a forward 
for Ligue 1 club Paris Saint-Germain and the Brazil national team.
He is widely regarded as one of the best players in the world."                   

Born: February 5, 1992 (age 29 years), Mogi das Cruzes, State of São Paulo, Brazil
Height: 1.75 m
Weight: 68 kg
Salary: 36.8 million EUR (2021)
Children: Davi Lucca da Silva Santos
Parents: Nadine Santos, Neymar Santos Sr.""")

except:
    print("Xato,ukajonim!")

#%% Problem3
while True:    
    choice = input("Tanlang: ")
    if(choice == '-1'):
        print("Hayr!")
        break        
    if choice == '1':
        try:
            name = input("Ismingiz: ")
            file = open("/home/muzaffar/Desktop/Python_Files/Malumotlar",'a')
            a = file.write(f"Ismingiz: {name}\n")
            file.close()
        except:
            print("Nimadir Xato!")
    if choice == '2':
        try:
            name = input("Familyangiz: ")
            file = open("/home/muzaffar/Desktop/Python_Files/Malumotlar",'a')
            a = file.write(f"Familyangiz: {name}\n")
            file.close()
        except:
            print("Nimadir Xato!")