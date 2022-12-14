
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4979"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4979"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit NeoKey FeatherWing PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-NeoKey-FeatherWing-PCB')
    newPart['gitName'].append('Adafruit-NeoKey-FeatherWing-PCB')
    newPart['eagleBoard'].append('/Adafruit NeoKey FeatherWing.brd')
    newPart['eagleSchem'].append('/Adafruit NeoKey FeatherWing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

