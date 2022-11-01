
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SIRB"
    oColor = "0031"
    oDesc = "STAN"
    oIndex = "02"
    hexID = "PRPR0031"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('FT230V2 SirUSB')
    newPart['gitRepo'].append('https://github.com/sirboard/SirUSB')
    newPart['gitName'].append('SirUSB')
    newPart['kicadBoard'].append('FT230V2/FT230V2.kicad_pcb')
    newPart['kicadSchem'].append('FT230V2/FT230V2.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

