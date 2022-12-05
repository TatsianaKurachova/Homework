def year (n): 
    if (n % 4 == 0 and n % 100 !=0) or n % 400 == 0:
        print ('Yes')
        return n
    else:
        print ('No')
        return n

print (year(2030))        