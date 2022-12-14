
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3632"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3632"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Joy Featherwing PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Joy-Featherwing-PCB')
    newPart['gitName'].append('Adafruit-Joy-Featherwing-PCB')
    newPart['eagleBoard'].append('/Joypad FeatherWing rev C.brd')
    newPart['eagleSchem'].append('/Joypad FeatherWing rev C.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

