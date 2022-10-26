
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3900"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3900"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Hallowing M0 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Hallowing-M0-PCB')
    newPart['gitName'].append('Adafruit-Hallowing-M0-PCB')
    newPart['eagleBoard'].append('/Adafruit Hallowing M0 Express.brd')
    newPart['eagleSchem'].append('/Adafruit Hallowing M0 Express.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

