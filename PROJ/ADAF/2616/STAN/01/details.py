
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2616"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2616"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PiTFT Plus 3.2 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PiTFT-Plus-3.2-PCB')
    newPart['gitName'].append('Adafruit-PiTFT-Plus-3.2-PCB')
    newPart['eagleBoard'].append('/Adafruit PiTFT+ 3.2in.brd')
    newPart['eagleSchem'].append('/Adafruit PiTFT+ 3.2in.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

