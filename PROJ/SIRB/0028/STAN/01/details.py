
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SIRB"
    oColor = "0028"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0028"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('CH340E SirUSB')
    newPart['gitRepo'].append('https://github.com/sirboard/SirUSB')
    newPart['gitName'].append('SirUSB')
    newPart['kicadBoard'].append('CH340E/CH340E.kicad_pcb')
    newPart['kicadSchem'].append('CH340E/CH340E.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

