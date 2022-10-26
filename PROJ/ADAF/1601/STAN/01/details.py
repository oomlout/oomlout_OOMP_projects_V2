
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1601"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1601"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PiTFT 2.8 inch Display PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PiTFT-2.8-inch-Display-PCB')
    newPart['gitName'].append('Adafruit-PiTFT-2.8-inch-Display-PCB')
    newPart['eagleBoard'].append('/Adafruit PiTFT 2.8inch Resistive PCB.brd')
    newPart['eagleSchem'].append('/Adafruit PiTFT 2.8inch Resistive PCB.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

