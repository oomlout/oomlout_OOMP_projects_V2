
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "DANP"
    oColor = "0002"
    oDesc = "STAN"
    oIndex = "V25"
    hexID = "PRPR0002"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Bus Pirate v25')
    newPart['gitRepo'].append('https://github.com/DangerousPrototypes/Bus_Pirate')
    newPart['gitName'].append('Bus_Pirate')
    newPart['eagleBoard'].append('hardware/v2go/BusPirate-v25.brd')
    newPart['eagleSchem'].append('hardware/v2go/BusPirate-v25.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

