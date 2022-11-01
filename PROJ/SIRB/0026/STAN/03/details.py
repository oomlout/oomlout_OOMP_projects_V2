
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SIRB"
    oColor = "0026"
    oDesc = "STAN"
    oIndex = "03"
    hexID = "PRPR0026"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SirNanoV3 SirNano')
    newPart['gitRepo'].append('https://github.com/sirboard/SirNano')
    newPart['gitName'].append('SirNano')
    newPart['kicadBoard'].append('SirNanoV3/SirNanoV3.kicad_pcb')
    newPart['kicadSchem'].append('SirNanoV3/SirNanoV3.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

