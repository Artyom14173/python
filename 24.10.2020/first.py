#а условие
a =10.0
for i in range(10): 
    print(i+1,"день ",round(a,2),"км")
    a=a+a/10

print("-------------")
#б условие
a=10.0
b=0.0
for i in range(7):
    b+=a
    a+=a/10   
print("Суммарный путь  за первые 7 дней тренировок: ",b)
print("-------------")

#в условие
a=10.0
b=0.0
n=int(input("Введите за какое кол-во дней вы хотите узнать суммарный путь - "))
for i in range(n):
    b+=a
    a+=a/10   
print("Суммарный путь  за n дней тренировок: ",round(b,2))
print("-------------")

#г условие
a=10.0
n=0
while a<=80:
    n+=1
    a+=a/10
    
    
print("На",n,"день он должен прекратить увеличивать пробег ") 


