
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SIRB"
    oColor = "0027"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0027"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('CH330N SirUSB')
    newPart['gitRepo'].append('https://github.com/sirboard/SirUSB')
    newPart['gitName'].append('SirUSB')
    newPart['kicadBoard'].append('CH330N/CH330N.kicad_pcb')
    newPart['kicadSchem'].append('CH330N/CH330N.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

