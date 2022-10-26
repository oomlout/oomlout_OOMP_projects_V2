
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4226"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4226"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit INA260 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-INA260-PCB')
    newPart['gitName'].append('Adafruit-INA260-PCB')
    newPart['eagleBoard'].append('/Adafruit INA260.brd')
    newPart['eagleSchem'].append('/Adafruit INA260.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

