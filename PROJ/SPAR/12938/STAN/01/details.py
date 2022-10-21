
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12938"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12938"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Si4703 FM Tuner Evaluation Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/Si4703_FM_Tuner_Evaluation_Board')
    newPart['gitName'].append('Si4703_FM_Tuner_Evaluation_Board')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Si4703_Eval.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Si4703_Eval.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

