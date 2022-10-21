
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11083"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11083"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('FM Tuner Basic Breakout Si4703')
    newPart['gitRepo'].append('https://github.com/sparkfun/FM_Tuner_Basic_Breakout-Si4703')
    newPart['gitName'].append('FM_Tuner_Basic_Breakout-Si4703')
    newPart['eagleBoard'].append('/Hardware/SparkFun_FM_Tuner_Basic_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_FM_Tuner_Basic_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

