
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3000"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3000"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Circuit Playground PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Circuit-Playground-PCB')
    newPart['gitName'].append('Adafruit-Circuit-Playground-PCB')
    newPart['eagleBoard'].append('/Adafruit Circuit Playground.brd')
    newPart['eagleSchem'].append('/Adafruit Circuit Playground.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

