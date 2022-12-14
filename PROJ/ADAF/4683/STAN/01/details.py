
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4683"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4683"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MPM3610 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MPM3610-PCB')
    newPart['gitName'].append('Adafruit-MPM3610-PCB')
    newPart['eagleBoard'].append('/Adafruit MPM3610.brd')
    newPart['eagleSchem'].append('/Adafruit MPM3610.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

