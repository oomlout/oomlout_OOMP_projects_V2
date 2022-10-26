
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15804"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15804"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic PL N823 IR Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_PL-N823_IR_Breakout')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_PL-N823_IR_Breakout')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_PL-N823_IR_Breakout/Hardware/Qwiic PL-N823 IR Breakout.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_PL-N823_IR_Breakout/Hardware/Qwiic PL-N823 IR Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

