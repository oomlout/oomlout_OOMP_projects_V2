
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "DANP"
    oColor = "0001"
    oDesc = "STAN"
    oIndex = "1A"
    hexID = "PRPR0001"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Bus Pirate Ultra 1A')
    newPart['gitRepo'].append('https://github.com/DangerousPrototypes/BusPirateUltraHardware')
    newPart['gitName'].append('BusPirateUltraHardware')
    newPart['eagleBoard'].append('BPUv1a/BusPirate-ultra.v1.0a.brd')
    newPart['eagleSchem'].append('BPUv1a/BusPirate-ultra.v1.0a.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

