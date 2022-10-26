
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2190"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2190"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Verter PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Verter-PCB')
    newPart['gitName'].append('Adafruit-Verter-PCB')
    newPart['eagleBoard'].append('/Adafruit Verter TPS63060 2A BoostBuck.brd')
    newPart['eagleSchem'].append('/Adafruit Verter TPS63060 2A BoostBuck.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

