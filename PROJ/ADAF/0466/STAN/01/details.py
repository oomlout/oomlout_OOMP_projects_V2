
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0466"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0466"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit VCNL40X0 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-VCNL40X0-PCB')
    newPart['gitName'].append('Adafruit-VCNL40X0-PCB')
    newPart['eagleBoard'].append('/Adafruit VCNL4010.brd')
    newPart['eagleSchem'].append('/Adafruit VCNL4010.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

