
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4319"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4319"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PyRuler PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PyRuler-PCB')
    newPart['gitName'].append('Adafruit-PyRuler-PCB')
    newPart['eagleBoard'].append('/Adafruit_PyRuler.brd')
    newPart['eagleSchem'].append('/Adafruit_PyRuler.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

