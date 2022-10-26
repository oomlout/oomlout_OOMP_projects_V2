
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3444"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3444"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('DotStar 2020 8x8 Matrix PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/DotStar-2020-8x8-Matrix-PCB')
    newPart['gitName'].append('DotStar-2020-8x8-Matrix-PCB')
    newPart['eagleBoard'].append('/Adafruit DotStar 2020 8x8 Matrix .brd')
    newPart['eagleSchem'].append('/Adafruit DotStar 2020 8x8 Matrix .sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

