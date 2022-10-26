
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4538"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4538"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit NAU7802 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-NAU7802-PCB')
    newPart['gitName'].append('Adafruit-NAU7802-PCB')
    newPart['eagleBoard'].append('/Adafruit NAU7802 board file.brd')
    newPart['eagleSchem'].append('/Adafruit NAU7802 board file.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

