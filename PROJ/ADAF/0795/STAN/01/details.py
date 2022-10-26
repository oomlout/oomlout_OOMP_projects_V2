
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0795"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0795"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Menta PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Menta-PCB')
    newPart['gitName'].append('Adafruit-Menta-PCB')
    newPart['eagleBoard'].append('/menta.brd')
    newPart['eagleSchem'].append('/menta.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

