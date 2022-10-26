
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1534"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1534"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit CC3000 Shield PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit_CC3000_Shield_PCB')
    newPart['gitName'].append('Adafruit_CC3000_Shield_PCB')
    newPart['eagleBoard'].append('/Adafruit CC3000 shield REV-B.brd')
    newPart['eagleSchem'].append('/Adafruit CC3000 shield REV-B.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

