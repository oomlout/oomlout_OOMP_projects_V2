
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14642"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14642"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic RTC')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_RTC')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_RTC')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_RTC/Hardware/Qwiic-RTC.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_RTC/Hardware/Qwiic-RTC.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

