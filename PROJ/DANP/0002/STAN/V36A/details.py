
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "DANP"
    oColor = "0002"
    oDesc = "STAN"
    oIndex = "V36A"
    hexID = "PRPR0002"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Bus Pirate v36a')
    newPart['gitRepo'].append('https://github.com/DangerousPrototypes/Bus_Pirate')
    newPart['gitName'].append('Bus_Pirate')
    newPart['eagleBoard'].append('hardware/v3.6/BusPirate-v3.6a-SSOP.brd')
    newPart['eagleSchem'].append('hardware/v3.6/BusPirate-v3.6a-SSOP.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

