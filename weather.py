from urllib.request import urlopen
import json

class Weather:
    def getPostalCode(TOKEN, devideId):
        URL = "https://api.amazonalexa.com/v1/devices/" + deviceId + "/settings/address/countryAndPostalCode"
        HEADER = {'Accept': 'application/json', 'Authorization': 'Bearer ' + TOKEN}
        response = urlopen(URL, headers=HEADER)
        data = json.load(response)
        return data
    
    def getCurrentWeather(self, addr):
        apiKey = "f3a83b5a8156b3dad4743bc83615b3ad"
        url = "http://api.openweathermap.org/data/2.5/weather?zip="+addr['postalCode']+","+addr['countryCode']+"&appid="+apiKey
        # response = urllib2.urlopen(url)
        # data = json.loads(response.read())
        data = {"coord":{"lon":-0.13,"lat":51.51},"weather":[{"id":300,"main":"Drizzle","description":"light intensity drizzle","icon":"09d"}],"base":"stations","main":{"temp":280.32,"pressure":1012,"humidity":81,"temp_min":279.15,"temp_max":281.15},"visibility":10000,"wind":{"speed":4.1,"deg":80},"clouds":{"all":90},"dt":1485789600,"sys":{"type":1,"id":5091,"message":0.0103,"country":"GB","sunrise":1485762037,"sunset":1485794875},"id":2643743,"name":"London","cod":200}
        return data
    
    def weatherDesc(self):
        return "It's a day with "+self.currentWeather['weather']['description']

    def tempIndex(self):
        temperature = self.currentWeather['main']['temp']
        index = temperature + -273.15 - 4
        if (index > 10):
            return 10
        elif (index < 0):
            return 0
        else:
            return int(index)
            
    def __init__(self,token,deviceId):
        # self.token = token
        # self.deviceId = deviceId
        addr = {"countryCode" : "US","postalCode" : "98109"} # getPostalCode(token, deviceId)
        self.addr = addr
        self.currentWeather = self.getCurrentWeather(addr)
        self.desc = self.weatherDesc
        self.i = self.tempIndex()
        
# HOW DO
# Weather global is always available
# access index (how hot it is out of 10) with: weather.i
# access description of weather with: weather.desc