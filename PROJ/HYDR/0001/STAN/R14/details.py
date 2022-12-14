
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "HYDR"
    oColor = "0001"
    oDesc = "STAN"
    oIndex = "R14"
    hexID = "PRPR0001"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Hydrabus 1.0 r1.4')
    newPart['gitRepo'].append('https://github.com/hydrabus/hydrabus')
    newPart['gitName'].append('hydrabus')
    newPart['kicadBoard'].append('hardware/HydraBus.kicad_pcb')
    newPart['kicadSchem'].append('hardware/HydraBus.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

