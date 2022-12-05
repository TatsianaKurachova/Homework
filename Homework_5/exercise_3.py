def min2time (minutes):
   h = minutes // 60 % 24
   m = minutes % 60 
   return "%02d:%02d" % (h, m)
print(min2time(1420))

