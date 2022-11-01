
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "DANP"
    oColor = "0001"
    oDesc = "STAN"
    oIndex = "2A"
    hexID = "PRPR0001"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Bus Pirate Ultra 2A')
    newPart['gitRepo'].append('https://github.com/DangerousPrototypes/BusPirateUltraHardware')
    newPart['gitName'].append('BusPirateUltraHardware')
    newPart['kicadBoard'].append('BPUv2a/BPUv2a.kicad_pcb')
    newPart['kicadSchem'].append('BPUv2a/BPUv2a.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

