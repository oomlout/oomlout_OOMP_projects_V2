
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3660"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3660"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit BME680 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-BME680-PCB')
    newPart['gitName'].append('Adafruit-BME680-PCB')
    newPart['eagleBoard'].append('/Adafruit BME680 Original.brd')
    newPart['eagleSchem'].append('/Adafruit BME680 Original.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

