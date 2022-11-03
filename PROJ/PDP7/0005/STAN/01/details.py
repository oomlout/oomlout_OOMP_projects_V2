
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "PDP7"
    oColor = "0005"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0005"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('<built-in method capitalize of str object at 0x000001DF21995D30>')
    newPart['gitRepo'].append('https://github.com/pdp7/gtb')
    newPart['gitName'].append('gtb')
    newPart['kicadBoard'].append('gtb.kicad_pcb')
    newPart['kicadSchem'].append('gtb.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

