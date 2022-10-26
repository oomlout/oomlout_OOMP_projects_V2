
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2298"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2298"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PiTFT Plus 2.8 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PiTFT-Plus-2.8-PCB')
    newPart['gitName'].append('Adafruit-PiTFT-Plus-2.8-PCB')
    newPart['eagleBoard'].append('/Adafruit PiTFT+ 2.8in.brd')
    newPart['eagleSchem'].append('/Adafruit PiTFT+ 2.8in.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

