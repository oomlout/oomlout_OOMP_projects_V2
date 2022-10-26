
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4415"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4415"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PA1010D Mini GPS PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PA1010D-Mini-GPS-PCB')
    newPart['gitName'].append('Adafruit-PA1010D-Mini-GPS-PCB')
    newPart['eagleBoard'].append('/Adafruit PA1010D Mini GPS.brd')
    newPart['eagleSchem'].append('/Adafruit PA1010D Mini GPS.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

