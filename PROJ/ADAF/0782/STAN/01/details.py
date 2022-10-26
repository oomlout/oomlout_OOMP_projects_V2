
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0782"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0782"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit USB Serial RGB Character Backpack PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-USB-Serial-RGB-Character-Backpack-PCB')
    newPart['gitName'].append('Adafruit-USB-Serial-RGB-Character-Backpack-PCB')
    newPart['eagleBoard'].append('/Adafruit USB Serial Char LCD.brd')
    newPart['eagleSchem'].append('/Adafruit USB Serial Char LCD.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

