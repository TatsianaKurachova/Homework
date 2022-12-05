from datetime import timedelta

start = timedelta (hours=9, minutes=40)
way = timedelta (hours=3, minutes=30)
finish = start + way
print (finish)