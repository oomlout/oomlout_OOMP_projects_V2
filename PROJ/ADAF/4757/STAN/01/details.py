
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4757"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4757"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Voice Bonnet PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Voice-Bonnet-PCB')
    newPart['gitName'].append('Adafruit-Voice-Bonnet-PCB')
    newPart['eagleBoard'].append('/Adafruit Voice Bonnet.brd')
    newPart['eagleSchem'].append('/Adafruit Voice Bonnet.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

