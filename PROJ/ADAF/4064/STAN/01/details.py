
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4064"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4064"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Grand Central PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Grand-Central-PCB')
    newPart['gitName'].append('Adafruit-Grand-Central-PCB')
    newPart['eagleBoard'].append('/Adafruit Grand Central M4 Express rev B.brd')
    newPart['eagleSchem'].append('/Adafruit Grand Central M4 Express rev B.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

