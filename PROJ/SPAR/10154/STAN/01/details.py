
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10154"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10154"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RF Transceiver Breakout RFM22B')
    newPart['gitRepo'].append('https://github.com/sparkfun/RF_Transceiver_Breakout-RFM22B')
    newPart['gitName'].append('RF_Transceiver_Breakout-RFM22B')
    newPart['eagleBoard'].append('/Hardware/SparkFun_RF_Transceiver-RFM22B.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_RF_Transceiver-RFM22B.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

