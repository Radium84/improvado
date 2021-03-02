import requests
import json

#Создаем массив имен
Names = ['Ivan','John','Petr','Serg','Helga']
file = open('Result.csv', 'w')
file.write('name,age,count'+'\n')
#Создаем гет запрос

for i in range(0,len(Names)):

    Row = requests.get('https://api.agify.io/?name='+Names[i])
    Parsed=json.loads(Row.text)
    NextStr=Parsed["name"]+',' +str(Parsed["age"])+','+str(Parsed["count"])
    print(NextStr)
    file.write(NextStr+'\n')

file.close()
