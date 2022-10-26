
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17114"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17114"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic Cellular Notecarrier')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_Cellular-Notecarrier')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_Cellular-Notecarrier')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_Cellular-Notecarrier/Hardware/Qwiic-Cellular-Notepad.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_Cellular-Notecarrier/Hardware/Qwiic-Cellular-Notepad.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

