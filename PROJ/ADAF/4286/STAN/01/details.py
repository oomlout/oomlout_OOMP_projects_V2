
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4286"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4286"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit DS3502 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-DS3502-PCB')
    newPart['gitName'].append('Adafruit-DS3502-PCB')
    newPart['eagleBoard'].append('/Adafruit DS3502.brd')
    newPart['eagleSchem'].append('/Adafruit DS3502.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

