#Ainult positiivsed arvud korrutamine



# a=float(input("A:"))
# b=float(input("B:"))
# if a>0 and b>0:
#    print(f"Korutis võrdub: {a*b}")

#a paaris või paaritu

# if a%2==0 and a!=0:
#     print(f"{a} on paaris")
# elif a==0:
#     print("arv on tundmatu")
# else:
#     print(f"{a} on paaritu")

# #Ema-robot 5/4/3/2/1

# try:
#     grade=int(input("Whats your grade"))
#     if grade in range (1,6):
#         if grade==5:
#             print("Well done!")
#         elif grade==4:
#             print("Good!")
#         elif grade==3:
#             print("Ok")
#         elif grade==2:
#             print("Better luck next time!")
#         elif grade==1:
#             print("Pull up!")
#     else:
#         print("Can't be real!")
# except Exception as e:
#     print("Error:", e)

#ül1

name=str(input("Mis on su nimi"))
if name.isupper():
    age=int(input("Kui vana sa oled"))
    if age<6:
        print("tasuta")
    elif age in range (6,14):
        print("lastepilet")
    elif age in range (15,65):
        print("täispilet")
    elif age>65:
        print("sooduspilet")
    elif age>100 or age<0:
        print ("niimodi ei käi")
else:
    print("error")

#ül2
try:
    naaber1=str(input("esimine nimi"))
    naaber2=str(input("teine nimi"))
    naaber3=str(input("kolmas nimi"))
    nimed=["Ilja","Aleksei","Marina"]
    if (naaber1 in nimed) and (naaber2 in nimed) and (naaber3 in nimed)and naaber1!=naaber2 and naaber2!=3:
        if naaber1.isalpha() and naaber2.isalpha and naaber3.isalpha:
                print("jah nad on naabrid")
        else:
            print("siseta ainult tähed")
    else:
        print("nad ei ole naabrid")
except:
    print("viga")

#ül3
side1=float(input("siseta 1 pool"))
side2=float(input("siseta 2 pool"))
if side1>0 and side2>0:
    perim=side1*side2
    print(f"perimeeter on {perim}")
    hind1=float(input("mitu maksab üks meeter?"))
    jah=str(input("Kas soovite remondi teha?"))
    if jah.lower()=="jah":
        hindkokku=hind1*perim
        print(f"väga jää hind on {hindkokku}")
    else:
            print("ok, siis teine kord")
else:("vale numbrid")

#ül4

try:
    alghind=float("sisesta hind")
    if alghind>700:
        soodus=alghind*0.7
        print(f"soodus on {soodus}")
    else:
        print("kahjuks hind ei ole piisav et saada soodustusi")
except:
    print("error")

#ül5

temp = float(input("Mis on toatemperatuur? : "))

if temp > 18:
    print(f" {temp} on üle 18 kraadi, kõik on korras!")
else:
    print(f" {temp} on madalam kui 18 kraadi.")

#ül6

kasv = float(input("Mis on sinu kasv? "))
if kasv<=160:
    print("lühike kasv")
elif kasv<180:
    print("keskmine kasv")
elif kasv>180:
    print("kõrg kasv")

#ül7


sugu = str(input("Mis on sinu sugu? M/N "))
if sugu.upper()=="M":
    print("Tere mees")
elif sugu.upper()=="N":
    print("Tere naine")

kasv= float(input("Mis on sinu kasv? "))
if kasv<=160:
    print("lühike kasv")
elif kasv<180:
    print("keskmine kasv")
elif kasv>180:
    print("kõrg kasv")


#ül12

hind = float(input("sisesta hind: "))
if hind>=10:
    hind=hind-(hind * 0.1)
    print(f"soodus on 10% ja hind on {hind}")
elif hind<=10:
     hind = hind-(hind*0.2)
     print(f"soodus on 20% ja hind on {hind}")
else:
    print("soodustusi pole")