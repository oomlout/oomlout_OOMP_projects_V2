
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2922"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2922"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Adalogger FeatherWing PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Adalogger-FeatherWing-PCB')
    newPart['gitName'].append('Adafruit-Adalogger-FeatherWing-PCB')
    newPart['eagleBoard'].append('/adalogger featherwing.brd')
    newPart['eagleSchem'].append('/adalogger featherwing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

