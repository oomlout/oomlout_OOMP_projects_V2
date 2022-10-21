
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10495"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10495"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Coin Cell Battery Holder Breakout 24.5mm')
    newPart['gitRepo'].append('https://github.com/sparkfun/Coin_Cell_Battery_Holder_Breakout-24.5mm')
    newPart['gitName'].append('Coin_Cell_Battery_Holder_Breakout-24.5mm')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Coin_Cell_Battery_Holder-24.5mm.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Coin_Cell_Battery_Holder-24.5mm.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

