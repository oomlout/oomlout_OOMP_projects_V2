
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4369"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4369"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PCT2075 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PCT2075-PCB')
    newPart['gitName'].append('Adafruit-PCT2075-PCB')
    newPart['eagleBoard'].append('/Adafruit_PCT2075.brd')
    newPart['eagleSchem'].append('/Adafruit_PCT2075.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

