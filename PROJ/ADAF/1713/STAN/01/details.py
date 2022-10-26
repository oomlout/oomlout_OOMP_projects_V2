
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1713"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1713"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MAX9814 AGC Microphone PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MAX9814-AGC-Microphone-PCB')
    newPart['gitName'].append('Adafruit-MAX9814-AGC-Microphone-PCB')
    newPart['eagleBoard'].append('/Adafruit MAX9814.brd')
    newPart['eagleSchem'].append('/Adafruit MAX9814.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

