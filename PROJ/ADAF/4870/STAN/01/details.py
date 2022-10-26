
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4870"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4870"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Neo Trinkey PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Neo-Trinkey-PCB')
    newPart['gitName'].append('Adafruit-Neo-Trinkey-PCB')
    newPart['eagleBoard'].append('/Adafruit Neo Trinkey.brd')
    newPart['eagleSchem'].append('/Adafruit Neo Trinkey.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

