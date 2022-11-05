
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "PDP7"
    oColor = "0010"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0010"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('<built-in method capitalize of str object at 0x00000279AD5FC230>')
    newPart['gitRepo'].append('https://github.com/pdp7/art')
    newPart['gitName'].append('art')
    newPart['kicadBoard'].append('flower-v3.kicad_pcb')
    newPart['kicadSchem'].append('flower-v3.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

