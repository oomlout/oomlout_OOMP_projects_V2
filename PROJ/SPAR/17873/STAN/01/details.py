
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17873"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17873"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic Power Meter ACS37800')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_Power_Meter-ACS37800')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_Power_Meter-ACS37800')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_Power_Meter-ACS37800/Hardware/Qwiic_Power_Meter-ACS37800.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_Power_Meter-ACS37800/Hardware/Qwiic_Power_Meter-ACS37800.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

