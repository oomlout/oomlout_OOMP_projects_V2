
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3709"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3709"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit SGP30 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-SGP30-PCB')
    newPart['gitName'].append('Adafruit-SGP30-PCB')
    newPart['eagleBoard'].append('/SGP30 Rev C.brd')
    newPart['eagleSchem'].append('/SGP30 Rev C.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

