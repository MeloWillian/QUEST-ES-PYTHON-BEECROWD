a = int(input())

meses = ["January","February","March","April","May","June","July","August","September","October","November","December"]
l = lambda x, list: list[x-1]

print(l(a,meses))

