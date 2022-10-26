
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0659"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0659"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Flora Mainboard')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Flora-Mainboard')
    newPart['gitName'].append('Adafruit-Flora-Mainboard')
    newPart['eagleBoard'].append('/adafruit flora mainboard 2.brd')
    newPart['eagleSchem'].append('/adafruit flora mainboard 2.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

