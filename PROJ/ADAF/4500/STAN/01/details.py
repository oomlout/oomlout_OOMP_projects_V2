
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4500"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4500"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit CLUE PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-CLUE-PCB')
    newPart['gitName'].append('Adafruit-CLUE-PCB')
    newPart['eagleBoard'].append('/Adafruit CLUE nRF52840 Express.brd')
    newPart['eagleSchem'].append('/Adafruit CLUE nRF52840 Express.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

