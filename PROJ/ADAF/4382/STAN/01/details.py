
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4382"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4382"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Feather STM32F405 Express PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Feather-STM32F405-Express-PCB')
    newPart['gitName'].append('Adafruit-Feather-STM32F405-Express-PCB')
    newPart['eagleBoard'].append('/Adafruit Feather STM32F405 Express.brd')
    newPart['eagleSchem'].append('/Adafruit Feather STM32F405 Express.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

