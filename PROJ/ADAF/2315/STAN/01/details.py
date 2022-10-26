
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2315"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2315"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PiTFT 2.2 Inch HAT PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PiTFT-2.2-Inch-HAT-PCB')
    newPart['gitName'].append('Adafruit-PiTFT-2.2-Inch-HAT-PCB')
    newPart['eagleBoard'].append('/Adafruit 2.2in TFT HAT rev A.brd')
    newPart['eagleSchem'].append('/Adafruit 2.2in TFT HAT rev A.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

