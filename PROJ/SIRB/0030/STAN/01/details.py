
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SIRB"
    oColor = "0030"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0030"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('CP2102N_20 SirUSB')
    newPart['gitRepo'].append('https://github.com/sirboard/SirUSB')
    newPart['gitName'].append('SirUSB')
    newPart['kicadBoard'].append('CP2102N_20/CP2102N_20.kicad_pcb')
    newPart['kicadSchem'].append('CP2102N_20/CP2102N_20.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

