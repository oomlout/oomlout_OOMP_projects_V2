
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5100"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5100"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MacroPad RP2040 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MacroPad-RP2040-PCB')
    newPart['gitName'].append('Adafruit-MacroPad-RP2040-PCB')
    newPart['eagleBoard'].append('/Adafruit MacroPad 2040.brd')
    newPart['eagleSchem'].append('/Adafruit MacroPad 2040.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

