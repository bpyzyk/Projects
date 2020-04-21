import requests
page = requests.get ('http://api.openweathermap.org/data/2.5/weather?q=Krakow&appid=99a24a78addf4a2c41947189fcff67f7&&lang=p&format=jsonl')
json = page.json() 
temp = json['main']['temp']
print ('Aktualna temperatura w Krakowie: [st. C]', temp-273,15)