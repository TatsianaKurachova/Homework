from datetime import datetime
from datetime import timedelta
start = timedelta (hours=9, minutes=40)
finish = timedelta (hours=12, minutes=50)
way = finish - start 
print (way)