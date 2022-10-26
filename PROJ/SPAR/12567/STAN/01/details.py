
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12567"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12567"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RedBot Buzzer')
    newPart['gitRepo'].append('https://github.com/sparkfun/RedBot_Buzzer')
    newPart['gitName'].append('RedBot_Buzzer')
    newPart['eagleBoard'].append('/Hardware/RedBot_Buzzer.brd')
    newPart['eagleSchem'].append('/Hardware/RedBot_Buzzer.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

