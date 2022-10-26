
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4698"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4698"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit AS7341 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-AS7341-PCB')
    newPart['gitName'].append('Adafruit-AS7341-PCB')
    newPart['eagleBoard'].append('/Adafruit_AS7341.brd')
    newPart['eagleSchem'].append('/Adafruit_AS7341.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

