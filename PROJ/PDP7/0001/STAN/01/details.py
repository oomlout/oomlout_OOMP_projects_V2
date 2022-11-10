
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "PDP7"
    oColor = "0001"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0001"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('<built-in method capitalize of str object at 0x000001E77154F1E0>')
    newPart['gitRepo'].append('https://github.com/pdp7/kicad-teensy-epaper')
    newPart['gitName'].append('kicad-teensy-epaper')
    newPart['kicadBoard'].append('kicad-teensy-epaper.kicad_pcb')
    newPart['kicadSchem'].append('kicad-teensy-epaper.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

