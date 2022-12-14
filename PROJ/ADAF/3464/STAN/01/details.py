
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3464"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3464"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Joy Bonnet PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Joy-Bonnet-PCB')
    newPart['gitName'].append('Adafruit-Joy-Bonnet-PCB')
    newPart['eagleBoard'].append('/Adafruit Joy Bonnet.brd')
    newPart['eagleSchem'].append('/Adafruit Joy Bonnet.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

