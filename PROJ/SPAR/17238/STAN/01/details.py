
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17238"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17238"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic Boost')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_Boost')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_Boost')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_Boost/Hardware/Qwiic_Boost.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_Boost/Hardware/Qwiic_Boost.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

