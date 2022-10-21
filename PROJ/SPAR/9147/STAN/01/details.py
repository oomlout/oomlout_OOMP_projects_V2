
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9147"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9147"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('AVR Stick')
    newPart['gitRepo'].append('https://github.com/sparkfun/AVR_Stick')
    newPart['gitName'].append('AVR_Stick')
    newPart['eagleBoard'].append('/Hardware/SparkFun_AVR_Stick.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_AVR_Stick.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

