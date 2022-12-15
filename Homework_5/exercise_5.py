from datetime import datetime
from datetime import datetime, timedelta

start = timedelta (hours=12, minutes=10)
finish =timedelta (hours=14, minutes=40)
way = finish - start
print (way)