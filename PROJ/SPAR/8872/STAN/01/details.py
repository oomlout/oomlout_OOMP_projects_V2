
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "8872"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR8872"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Mic Preamp')
    newPart['gitRepo'].append('https://github.com/sparkfun/Mic_Preamp')
    newPart['gitName'].append('Mic_Preamp')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Mic-Preamp-v12.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Mic-Preamp-v12.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

