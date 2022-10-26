
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16740"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16740"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic Power Switch')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_Power_Switch')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_Power_Switch')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_Power_Switch/Hardware/Qwiic Power Switch.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_Power_Switch/Hardware/Qwiic Power Switch.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

