
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SOPA"
    oColor = "0011"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0011"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('<built-in method capitalize of str object at 0x000001DF1B4058F0>')
    newPart['gitRepo'].append('https://github.com/solderparty/pmod_to_qwiic_adapter')
    newPart['gitName'].append('pmod_to_qwiic_adapter')
    newPart['kicadBoard'].append('pmod_to_qwiic.kicad_pcb')
    newPart['kicadSchem'].append('pmod_to_qwiic.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

