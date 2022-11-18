
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "19236"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR19236"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Satellite Transceiver Breakout  Swarm M138')
    newPart['gitRepo'].append('https://github.com/sparkfun/Satellite_Transceiver_Breakout__Swarm_M138')
    newPart['gitName'].append('Satellite_Transceiver_Breakout__Swarm_M138')
    newPart['eagleBoard'].append('/Hardware/Satellite_Transceiver_Breakout__Swarm_M138.brd')
    newPart['eagleSchem'].append('/Hardware/Satellite_Transceiver_Breakout__Swarm_M138.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

