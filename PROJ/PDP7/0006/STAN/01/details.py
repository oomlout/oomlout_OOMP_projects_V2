
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "PDP7"
    oColor = "0006"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0006"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Hardware/teensyi2c')
    newPart['gitRepo'].append('https://github.com/pdp7/teensy-wifi-weather-logger')
    newPart['gitName'].append('teensy-wifi-weather-logger')
    newPart['kicadBoard'].append('hardware/teensyi2c.kicad_pcb')
    newPart['kicadSchem'].append('hardware/teensyi2c.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

