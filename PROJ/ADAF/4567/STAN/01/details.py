
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4567"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4567"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 2.23 inch Monochrome OLED Bonnet PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-2.23-inch-Monochrome-OLED-Bonnet-PCB')
    newPart['gitName'].append('Adafruit-2.23-inch-Monochrome-OLED-Bonnet-PCB')
    newPart['eagleBoard'].append('/Adafruit 2.23-inch Monochrome OLED Bonnet.brd')
    newPart['eagleSchem'].append('/Adafruit 2.23-inch Monochrome OLED Bonnet.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

