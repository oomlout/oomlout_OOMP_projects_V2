
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "DANP"
    oColor = "0002"
    oDesc = "STAN"
    oIndex = "V4E"
    hexID = "PRPR0002"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Bus Pirate v4e')
    newPart['gitRepo'].append('https://github.com/DangerousPrototypes/Bus_Pirate')
    newPart['gitName'].append('Bus_Pirate')
    newPart['eagleBoard'].append('hardware/v4/BusPirate-v4e.brd')
    newPart['eagleSchem'].append('hardware/v4/BusPirate-v4e.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

