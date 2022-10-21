
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "8554"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR8554"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('IR Receiver Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/IR_Receiver_Breakout')
    newPart['gitName'].append('IR_Receiver_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_IR_Receiver.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_IR_Receiver.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

