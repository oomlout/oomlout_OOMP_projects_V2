
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17713"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17713"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroMod STM32 Processor')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroMod_STM32_Processor')
    newPart['gitName'].append('MicroMod_STM32_Processor')
    newPart['eagleBoard'].append('/Hardware/MicroMod_STM32_Processor.brd')
    newPart['eagleSchem'].append('/Hardware/MicroMod_STM32_Processor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

