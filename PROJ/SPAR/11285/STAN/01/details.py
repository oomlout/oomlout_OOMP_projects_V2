
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11285"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11285"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad Coin Cell Battery Holder Switched')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_Coin_Cell_Battery_Holder-Switched')
    newPart['gitName'].append('LilyPad_Coin_Cell_Battery_Holder-Switched')
    newPart['eagleBoard'].append('/Hardware/Sparkfun_LilyPad-Switched-Battery.brd')
    newPart['eagleSchem'].append('/Hardware/Sparkfun_LilyPad-Switched-Battery.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

