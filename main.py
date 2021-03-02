import requests
import json

#Создаем массив имен
Names = ['Ivan','John','Petr','Serg','Helga']
#Открываем файл для записи
file = open('Result.csv', 'w')
#Создаеем заголовок
file.write('name,age,count'+'\r\n')
#Мы будем подставлять имена в get-запрос, с нулевого элемента по конечный элемент
for i in range(0,len(Names)):
    #Получаем сырой ответ
    Row = requests.get('https://api.agify.io/?name='+Names[i])
    #Используем библиотеку json для обработки текста из отвеета
    Parsed=json.loads(Row.text)
    #Используя переменные из json как разделители строки, получаем обработанную строку из значений переменных
    NextStr=Parsed["name"]+',' +str(Parsed["age"])+','+str(Parsed["count"])
    #print(NextStr) проверка результат в консоли
    #Запись в csv файл,который потом можно будет открыть в Exel
    file.write(NextStr+'\r\n')

file.close()
