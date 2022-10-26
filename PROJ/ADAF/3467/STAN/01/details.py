
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3467"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3467"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit CharliePlex Bonnet PCBs')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-CharliePlex-Bonnet-PCBs')
    newPart['gitName'].append('Adafruit-CharliePlex-Bonnet-PCBs')
    newPart['eagleBoard'].append('/Adafruit CharliePlex Bonnet.brd')
    newPart['eagleSchem'].append('/Adafruit CharliePlex Bonnet.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

