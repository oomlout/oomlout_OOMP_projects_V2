
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18572"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18572"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LoRa 1W Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/LoRa_1W_Breakout')
    newPart['gitName'].append('LoRa_1W_Breakout')
    newPart['eagleBoard'].append('/Hardware/LoRa_1W_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/LoRa_1W_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

