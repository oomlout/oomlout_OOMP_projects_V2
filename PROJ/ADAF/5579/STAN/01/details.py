
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5579"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5579"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MMC5603 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MMC5603-PCB')
    newPart['gitName'].append('Adafruit-MMC5603-PCB')
    newPart['eagleBoard'].append('/MMC56x3 rev A.brd')
    newPart['eagleSchem'].append('/MMC56x3 rev A.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

