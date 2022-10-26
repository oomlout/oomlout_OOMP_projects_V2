
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "19017"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR19017"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic 1.8V Adapter')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_1.8V_Adapter')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_1.8V_Adapter')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_1.8V_Adapter/Hardware/Qwiic_1.8V_Adapter.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_1.8V_Adapter/Hardware/Qwiic_1.8V_Adapter.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

