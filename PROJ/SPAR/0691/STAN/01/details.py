
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "0691"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0691"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Transceiver Breakout nRF24L01')
    newPart['gitRepo'].append('https://github.com/sparkfun/Transceiver_Breakout-nRF24L01')
    newPart['gitName'].append('Transceiver_Breakout-nRF24L01')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Tranceiver_Breakout-nRF24L01.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Tranceiver_Breakout-nRF24L01.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

