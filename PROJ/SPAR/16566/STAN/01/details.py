
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16566"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16566"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic Quad Relay')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_Quad_Relay')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_Quad_Relay')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_Quad_Relay/Hardware/Qwiic_Quad_Relay.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_Quad_Relay/Hardware/Qwiic_Quad_Relay.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

