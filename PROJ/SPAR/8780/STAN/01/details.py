
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "8780"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR8780"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RS232 Shifter')
    newPart['gitRepo'].append('https://github.com/sparkfun/RS232_Shifter')
    newPart['gitName'].append('RS232_Shifter')
    newPart['eagleBoard'].append('/Hardware/Sparkfun_RS232.brd')
    newPart['eagleSchem'].append('/Hardware/Sparkfun_RS232.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

