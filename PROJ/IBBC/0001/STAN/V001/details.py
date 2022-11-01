
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "IBBC"
    oColor = "0001"
    oDesc = "STAN"
    oIndex = "V001"
    hexID = "PRPR0001"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ADXL345 Breakout V001')
    newPart['gitRepo'].append('https://github.com/oomlout/IBBC_0001')
    newPart['gitName'].append('IBBC_0001')
    newPart['kicadBoard'].append('IBBC_0001_V001/IBBC_0001.kicad_pcb')
    newPart['kicadSchem'].append('IBBC_0001_V001/IBBC_0001.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

