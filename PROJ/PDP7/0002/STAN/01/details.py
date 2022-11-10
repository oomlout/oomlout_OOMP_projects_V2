
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "PDP7"
    oColor = "0002"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0002"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('<built-in method capitalize of str object at 0x0000023941584120>')
    newPart['gitRepo'].append('https://github.com/pdp7/teensy-touch')
    newPart['gitName'].append('teensy-touch')
    newPart['kicadBoard'].append('hardware/teensy-touch.kicad_pcb')
    newPart['kicadSchem'].append('hardware/teensy-touch.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

