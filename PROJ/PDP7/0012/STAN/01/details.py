
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "PDP7"
    oColor = "0012"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0012"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Sixlayer')
    newPart['gitRepo'].append('https://github.com/pdp7/art')
    newPart['gitName'].append('art')
    newPart['kicadBoard'].append('sixlayer.kicad_pcb')
    newPart['kicadSchem'].append('sixlayer.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

