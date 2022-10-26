
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1958"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1958"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Si4713 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Si4713-PCB')
    newPart['gitName'].append('Adafruit-Si4713-PCB')
    newPart['eagleBoard'].append('/Adafruit Si471x PCB.brd')
    newPart['eagleSchem'].append('/Adafruit Si471x PCB.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

