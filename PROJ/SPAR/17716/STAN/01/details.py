
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17716"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17716"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic Time of Flight TMF8801')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_Time-of-Flight-TMF8801')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_Time-of-Flight-TMF8801')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_Time-of-Flight-TMF8801/Hardware/Qwiic_TMF8801.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_Time-of-Flight-TMF8801/Hardware/Qwiic_TMF8801.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

