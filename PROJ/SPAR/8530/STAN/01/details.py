
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "8530"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR8530"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Speed Trap')
    newPart['gitRepo'].append('https://github.com/sparkfun/Speed_Trap')
    newPart['gitName'].append('Speed_Trap')
    newPart['eagleBoard'].append('/hardware/Large Digit Shield.brd')
    newPart['eagleSchem'].append('/hardware/Large Digit Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

