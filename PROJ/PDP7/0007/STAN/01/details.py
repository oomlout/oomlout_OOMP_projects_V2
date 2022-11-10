
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "PDP7"
    oColor = "0007"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0007"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('<built-in method capitalize of str object at 0x0000020A47D1F170>')
    newPart['gitRepo'].append('https://github.com/pdp7/art')
    newPart['gitName'].append('art')
    newPart['kicadBoard'].append('art.kicad_pcb')
    newPart['kicadSchem'].append('art.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

