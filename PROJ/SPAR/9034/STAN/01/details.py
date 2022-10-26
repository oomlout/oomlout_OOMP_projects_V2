
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9034"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9034"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Transceiver Breakout nRF24LU1 RP SMA')
    newPart['gitRepo'].append('https://github.com/sparkfun/Transceiver_Breakout-nRF24LU1_RP-SMA')
    newPart['gitName'].append('Transceiver_Breakout-nRF24LU1_RP-SMA')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Transceiver_Breakout_NRF24LU1.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Transceiver_Breakout_NRF24LU1.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

