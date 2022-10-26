
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "20107"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR20107"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Satellite Transceiver Function Board  Swarm M138')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Satellite_Transceiver_Function_Board__Swarm_M138')
    newPart['gitName'].append('https://github.com/sparkfunX/Satellite_Transceiver_Function_Board__Swarm_M138')
    newPart['eagleBoard'].append('sourceFiles/git/Satellite_Transceiver_Function_Board__Swarm_M138/Hardware/Satellite_Transceiver_Function_Board__Swarm_M138.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Satellite_Transceiver_Function_Board__Swarm_M138/Hardware/Satellite_Transceiver_Function_Board__Swarm_M138.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

