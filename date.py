#ex1
import datetime
x = datetime.datetime.now()
print(x.day - 5)

#ex2
import datetime
x = datetime.datetime.now()
print(x.day - 1)
print(x.day)
print(x.day + 1)

#ex3
import datetime
x = datetime.datetime.now()
print(x.strftime("%x"),x.strftime("%X"))

#ex4
from datetime import datetime 
 
def date_diff_in_sec(date1, date2): 
    timediff = abs(date2 - date1) 
    return timediff.total_seconds() 
date1 = datetime(2023, 1, 1, 10, 5, 5)   
date2 = datetime(2023, 1, 1, 12, 0, 0)  
difference_seconds = date_diff_in_sec(date1, date2) 
print("Difference in seconds:", difference_seconds)

