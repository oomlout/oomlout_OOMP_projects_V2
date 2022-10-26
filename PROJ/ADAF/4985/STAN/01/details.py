
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4985"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4985"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit FunHouse PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-FunHouse-PCB')
    newPart['gitName'].append('Adafruit-FunHouse-PCB')
    newPart['eagleBoard'].append('/Adafruit FunHouse.brd')
    newPart['eagleSchem'].append('/Adafruit FunHouse.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

