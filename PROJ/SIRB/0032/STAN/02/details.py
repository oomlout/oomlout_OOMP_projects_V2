
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SIRB"
    oColor = "0032"
    oDesc = "STAN"
    oIndex = "02"
    hexID = "PRPR0032"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('FT231V2 SirUSB')
    newPart['gitRepo'].append('https://github.com/sirboard/SirUSB')
    newPart['gitName'].append('SirUSB')
    newPart['kicadBoard'].append('FT231V2/FT231V2.kicad_pcb')
    newPart['kicadSchem'].append('FT231V2/FT231V2.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

