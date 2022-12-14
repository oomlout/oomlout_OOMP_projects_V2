
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4311"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4311"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 2.0 inch 240x320 TFT PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-2.0-inch-240x320-TFT-PCB')
    newPart['gitName'].append('Adafruit-2.0-inch-240x320-TFT-PCB')
    newPart['eagleBoard'].append('/Adafruit 2.0 inch 240x320 IPS TFT.brd')
    newPart['eagleSchem'].append('/Adafruit 2.0 inch 240x320 IPS TFT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

