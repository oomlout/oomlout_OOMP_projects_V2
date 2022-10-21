
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15083"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15083"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Twist')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Twist')
    newPart['gitName'].append('Qwiic_Twist')
    newPart['eagleBoard'].append('/Hardware/Qwiic Twist.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic Twist.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

