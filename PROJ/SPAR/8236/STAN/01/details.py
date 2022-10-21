
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "8236"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR8236"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Navigation Switch Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/Navigation_Switch_Breakout')
    newPart['gitName'].append('Navigation_Switch_Breakout')
    newPart['eagleBoard'].append('/Hardware/NavSwitch-Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/NavSwitch-Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

