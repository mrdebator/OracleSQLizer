import csv 
from sys import argv 
import re

script, input_file, tbname = argv

print('''

╭━━━╮╱╱╱╱╱╱╱╭╮╱╱╱╭━━━┳━━━┳╮
┃╭━╮┃╱╱╱╱╱╱╱┃┃╱╱╱┃╭━╮┃╭━╮┃┃
┃┃╱┃┣━┳━━┳━━┫┃╭━━┫╰━━┫┃╱┃┃┃╱╱╭┳━━━┳━━┳━╮
┃┃╱┃┃╭┫╭╮┃╭━┫┃┃┃━╋━━╮┃┃╱┃┃┃╱╭╋╋━━┃┃┃━┫╭╯
┃╰━╯┃┃┃╭╮┃╰━┫╰┫┃━┫╰━╯┃╰━╯┃╰━╯┃┃┃━━┫┃━┫┃
╰━━━┻╯╰╯╰┻━━┻━┻━━┻━━━┻━━╮┣━━━┻┻━━━┻━━┻╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
''')

f = open(input_file)
csv_f = csv.reader(f)

print("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD';") #Note: you can change this to work with your specific dataset.

c = 1
for row in csv_f:
  if (c>1):
    query = "INSERT INTO " + tbname + " VALUES("
    for j in row:
   

      if((re.match('^[0-9]+$',j))):
        query += j + ","

    #code to handle date using the timestamp datatype. Please mention datatype DATE in CREATE statement

      elif(re.match('^(?:(?:(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00)))(\/|-|\.)(?:0?2\1(?:29)))|(?:(?:(?:1[6-9]|[2-9]\d)?\d{2})(\/|-|\.)(?:(?:(?:0?[13578]|1[02])\2(?:31))|(?:(?:0?[1,3-9]|1[0-2])\2(29|30))|(?:(?:0?[1-9])|(?:1[0-2]))\2(?:0?[1-9]|1\d|2[0-8]))))$',j)):
        query += "'" + j + "',"

      
      #this is included to work with mm-dd-yyyy

      #elif(re.match('^(((0?[1-9]|1[012])/(0?[1-9]|1\d|2[0-8])|(0?[13456789]|1[012])/(29|30)|(0?[13578]|1[02])/31)/(19|[2-9]\d)\d{2}|0?2/29/((19|[2-9]\d)(0[48]|[2468][048]|[13579][26])|(([2468][048]|[3579][26])00)))$',j)):
      
      elif(j == "null"):
        query += j + ","

      else:
        j = j.replace("'", "")
        query += "'" + j + "',"

    query = query[:-1] #pops last comma at the end
    query += ");"
    print(query)

  c += 1
