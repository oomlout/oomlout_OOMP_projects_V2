
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10730"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10730"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad Coin Cell Battery Holder 20mm')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_Coin_Cell_Battery_Holder-20mm')
    newPart['gitName'].append('LilyPad_Coin_Cell_Battery_Holder-20mm')
    newPart['eagleBoard'].append('/Hardware/SparkFun_LilyPad_Coincell-Battery.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_LilyPad_Coincell-Battery.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

