
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SIRB"
    oColor = "0029"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0029"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('CH340G SirUSB')
    newPart['gitRepo'].append('https://github.com/sirboard/SirUSB')
    newPart['gitName'].append('SirUSB')
    newPart['kicadBoard'].append('CH340G/CH340G.kicad_pcb')
    newPart['kicadSchem'].append('CH340G/CH340G.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

