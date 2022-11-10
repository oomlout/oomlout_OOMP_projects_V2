
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SOPA"
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

    newPart['name'].append('Bbq20 keyboard')
    newPart['gitRepo'].append('https://github.com/solderparty/bbq20kbd_hw')
    newPart['gitName'].append('bbq20kbd_hw')
    newPart['kicadBoard'].append('bbq20_keyboard.kicad_pcb')
    newPart['kicadSchem'].append('bbq20_keyboard.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

