import csv
from sys import argv
import re

script, input_file, tbname = argv

f = open(input_file)
csv_f = csv.reader(f)

c = 1
for row in csv_f:
  if (c>1):
    query = "INSERT INTO " + tbname + " VALUES("
    for j in row:
      
      if(not(re.match('^[0-9]+$',j))):
        j = j.replace("'", "")
        query += "'" + j + "',"
      else:
        query += j + ","
        
    query = query[:-1]
    query += ");"
    print(query)
    
  c += 1

