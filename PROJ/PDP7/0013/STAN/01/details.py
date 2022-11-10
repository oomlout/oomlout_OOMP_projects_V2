
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "PDP7"
    oColor = "0013"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0013"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('<built-in method capitalize of str object at 0x0000020A47D3B4B0>')
    newPart['gitRepo'].append('https://github.com/pdp7/teensy-weather-badge')
    newPart['gitName'].append('teensy-weather-badge')
    newPart['kicadBoard'].append('hardware/teensyi2c.kicad_pcb')
    newPart['kicadSchem'].append('hardware/teensyi2c.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

