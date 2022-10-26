
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5374"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5374"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit ADXL375 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit_ADXL375_PCB')
    newPart['gitName'].append('Adafruit_ADXL375_PCB')
    newPart['eagleBoard'].append('/Adafruit ADXL375.brd')
    newPart['eagleSchem'].append('/Adafruit ADXL375.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

