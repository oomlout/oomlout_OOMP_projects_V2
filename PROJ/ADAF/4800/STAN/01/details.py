
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4800"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4800"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MagTag PCBs')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit_MagTag_PCBs')
    newPart['gitName'].append('Adafruit_MagTag_PCBs')
    newPart['eagleBoard'].append('/Adafruit MagTag 2.9in.brd')
    newPart['eagleSchem'].append('/Adafruit MagTag 2.9in.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

