
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13815"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13815"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Beefcake Relay Control Kit')
    newPart['gitRepo'].append('https://github.com/sparkfun/Beefcake_Relay_Control_Kit')
    newPart['gitName'].append('Beefcake_Relay_Control_Kit')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Beefcake_Relay_Control_Kit.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Beefcake_Relay_Control_Kit.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

