
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SOPA"
    oColor = "0004"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0004"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Keyboard featherwing')
    newPart['gitRepo'].append('https://github.com/solderparty/keyboard_featherwing_hw')
    newPart['gitName'].append('keyboard_featherwing_hw')
    newPart['kicadBoard'].append('keyboard_featherwing.kicad_pcb')
    newPart['kicadSchem'].append('keyboard_featherwing.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

