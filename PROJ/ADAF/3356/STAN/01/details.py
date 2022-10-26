
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3356"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3356"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Animated Eyes Bonnet PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Animated-Eyes-Bonnet-PCB')
    newPart['gitName'].append('Adafruit-Animated-Eyes-Bonnet-PCB')
    newPart['eagleBoard'].append('/Adafruit Eyes Bonnet.brd')
    newPart['eagleSchem'].append('/Adafruit Eyes Bonnet.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

