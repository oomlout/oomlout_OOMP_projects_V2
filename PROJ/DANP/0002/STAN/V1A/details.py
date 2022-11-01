
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "DANP"
    oColor = "0002"
    oDesc = "STAN"
    oIndex = "V1A"
    hexID = "PRPR0002"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Bus Pirate v1a')
    newPart['gitRepo'].append('https://github.com/DangerousPrototypes/Bus_Pirate')
    newPart['gitName'].append('Bus_Pirate')
    newPart['eagleBoard'].append('hardware/v1a/BusPirate-24Fv1a.final.brd')
    newPart['eagleSchem'].append('hardware/v1a/BusPirate-24Fv1a.final.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

