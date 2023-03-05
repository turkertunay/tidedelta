import datetime

tt = datetime.date(1942, 7, 22)
print(tt)


td = datetime.timedelta(30000)
ttt = (tt + td)
print(ttt)

print(tt.strftime("%A, %B %d, %Y"))

bd = "TT was born on {:%A, %B %d, %Y}."
print(bd.format(tt))

ed = "10/29/1923"
edd = datetime.datetime.strptime(ed, "%m/%d/%Y")
print(edd)

