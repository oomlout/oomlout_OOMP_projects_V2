
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3787"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3787"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 1.54 inch 240x240 TFT PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-1.54-inch-240x240-TFT-PCB')
    newPart['gitName'].append('Adafruit-1.54-inch-240x240-TFT-PCB')
    newPart['eagleBoard'].append('/Adafruit 1.54inch 240x240 rev E.brd')
    newPart['eagleSchem'].append('/Adafruit 1.54inch 240x240 rev E.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

