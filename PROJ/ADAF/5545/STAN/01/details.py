
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5545"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5545"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PCF8574 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PCF8574-PCB')
    newPart['gitName'].append('Adafruit-PCF8574-PCB')
    newPart['eagleBoard'].append('/Adafruit PCF8574 QT.brd')
    newPart['eagleSchem'].append('/Adafruit PCF8574 QT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

