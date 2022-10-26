
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17979"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17979"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic Sound Trigger')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_Sound_Trigger')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_Sound_Trigger')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_Sound_Trigger/Hardware/Qwiic Sound Trigger.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_Sound_Trigger/Hardware/Qwiic Sound Trigger.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

