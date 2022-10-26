
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3249"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3249"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit NeoPXL8 PCBs')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-NeoPXL8-PCBs')
    newPart['gitName'].append('Adafruit-NeoPXL8-PCBs')
    newPart['eagleBoard'].append('/Adafruit NeoPXL8 Friend.brd')
    newPart['eagleSchem'].append('/Adafruit NeoPXL8 Friend.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

