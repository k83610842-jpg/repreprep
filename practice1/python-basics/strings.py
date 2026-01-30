#1
print("Privet")
print('Privet')
#2
print("city")
print("his name is 'John'")
print('his name is "John"')
#3
a="stars"
print(a)
#4
a="""You can assign a multiline string to a
 variable by using 
 three quotes"""
print(a)
#5
a='''You can assign a multiline string 
to a variable by using three
 quotes'''
print(a)
#6
a="Privet"
print(a[2])# output=i
#7
for a in "karbyz":
    print(a)
#8
a="alo alo"
print(len(a))
#9
a="jj ff ff dd d net"
print("ff" in a)
print("dfdf" in a)
#10
text="santa cola"
if "cola" in text:
    print("Yes")
#11
txt="lalaland and France"
print("kkk" not in txt)  #True
txt="lalaland and France"
print("and" not in txt)   #False
#12
txt="lalaland and France"
if "lalalans" not in txt:
    print("lalalans is in the txt")
#13
a="America and France"
print(a[1:7])
#14
a="Agent and Claude"
print(a[:2])
#15
a="holiday"
print(a[3:])
#16
a="America and France"
print(a[-8:-3])
#17
a="France and America"
print(a.upper()) #upper letters
#18
a="France and America"
print(a.lower())
#19
a="        France and America      "
print(a.strip())
#20
a="HHHH"
print(a.replace("H","k"))
#21
a="dhksjkd,jasdjas,slkjlkad.kaskd"
print(a.split(',')) #['dhksjkd', 'jasdjas', 'slkjlkad.kaskd']
#22
a="Privet"
b="mir"
c=a+b
print(c)
#23
a="Privet"
b="mir"
c=a+"        ///"+b
print(c)
#24 example with mistake
a=35
text="ksdladkd"+a
print(text)
#without mistake
a=35
text=f"fjkfkdf {a}"
print(text)
#25
price=10
text=f"the price is {price}"
print(a)
#26
price=434.4233
text=f"the price is {price:.3f}"
#27
text=f"the price is {823488*2}"
print(text)
#28
txt="na ulitse today \"cold\" " #output=na ulitse today "cold" 


