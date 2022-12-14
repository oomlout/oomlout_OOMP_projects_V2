
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4282"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4282"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PiRTC DS3231 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PiRTC-DS3231-PCB')
    newPart['gitName'].append('Adafruit-PiRTC-DS3231-PCB')
    newPart['eagleBoard'].append('/Adafruit DS3231 PiRTC.brd')
    newPart['eagleSchem'].append('/Adafruit DS3231 PiRTC.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

