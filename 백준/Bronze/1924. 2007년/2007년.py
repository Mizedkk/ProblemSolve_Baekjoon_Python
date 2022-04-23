from datetime import datetime
case = ['MON','TUE','WED','THU','FRI','SAT','SUN']
a, b = map(int, input().split())
n = datetime(2007,a,b)
print(case[n.weekday()])