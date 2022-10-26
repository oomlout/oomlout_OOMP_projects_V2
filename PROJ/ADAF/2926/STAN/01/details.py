
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2926"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2926"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Terminal Block FeatherWing PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Terminal-Block-FeatherWing-PCB')
    newPart['gitName'].append('Adafruit-Terminal-Block-FeatherWing-PCB')
    newPart['eagleBoard'].append('/Adafruit Terminal FeatherWing.brd')
    newPart['eagleSchem'].append('/Adafruit Terminal FeatherWing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

