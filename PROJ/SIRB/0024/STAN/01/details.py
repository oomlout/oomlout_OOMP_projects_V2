
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SIRB"
    oColor = "0024"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0024"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ATTinyX16 SirTiny')
    newPart['gitRepo'].append('https://github.com/sirboard/SirTiny')
    newPart['gitName'].append('SirTiny')
    newPart['kicadBoard'].append('ATTinyX16/ATTinyX16.kicad_pcb')
    newPart['kicadSchem'].append('ATTinyX16/ATTinyX16.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

