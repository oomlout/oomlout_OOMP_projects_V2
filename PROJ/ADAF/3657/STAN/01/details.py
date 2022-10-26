
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3657"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3657"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit SAMD09 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-SAMD09-Breakout-PCB')
    newPart['gitName'].append('Adafruit-SAMD09-Breakout-PCB')
    newPart['eagleBoard'].append('/ATSAMD09D14 Breakout rev B.brd')
    newPart['eagleSchem'].append('/ATSAMD09D14 Breakout rev B.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

