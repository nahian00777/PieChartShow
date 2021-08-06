import matplotlib.pyplot as p
n = int(input("Enter how many data you want to show in that piechart:"))
s = []
print("Enter the percentage of each data in piechart:")
for i in range(0,n):
    res = int(input())
    s.append(res)
l = []
print("Enter the name of the labels in piechart:")
for i in range(0,n):
    les = input()
    l.append(les)
p.pie(s, labels = l)
p.show()

