
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16984"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16984"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroMod Processor Board nRF52840')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroMod_Processor_Board-nRF52840')
    newPart['gitName'].append('MicroMod_Processor_Board-nRF52840')
    newPart['eagleBoard'].append('/Hardware/MicroMod_Processor_Board-nRF52840.brd')
    newPart['eagleSchem'].append('/Hardware/MicroMod_Processor_Board-nRF52840.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

