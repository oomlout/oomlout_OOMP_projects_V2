
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2200"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2200"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LM4040 Voltage Reference PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LM4040-Voltage-Reference-PCB')
    newPart['gitName'].append('Adafruit-LM4040-Voltage-Reference-PCB')
    newPart['eagleBoard'].append('/Adafruit LM4040.brd')
    newPart['eagleSchem'].append('/Adafruit LM4040.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

