
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17870"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17870"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Soft Power Switch')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Soft_Power_Switch')
    newPart['gitName'].append('https://github.com/sparkfunX/Soft_Power_Switch')
    newPart['eagleBoard'].append('sourceFiles/git/Soft_Power_Switch/Hardware/SparkFun Soft Power Switch.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Soft_Power_Switch/Hardware/SparkFun Soft Power Switch.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

