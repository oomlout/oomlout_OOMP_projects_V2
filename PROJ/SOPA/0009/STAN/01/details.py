
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SOPA"
    oColor = "0009"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0009"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Rp2040 stamp console')
    newPart['gitRepo'].append('https://github.com/solderparty/rp2040_stamp_console_hw')
    newPart['gitName'].append('rp2040_stamp_console_hw')
    newPart['kicadBoard'].append('rp2040_stamp_console.kicad_pcb')
    newPart['kicadSchem'].append('rp2040_stamp_console.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

