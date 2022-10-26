
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11260"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11260"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad LiPower')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_LiPower')
    newPart['gitName'].append('LilyPad_LiPower')
    newPart['eagleBoard'].append('/Hardware/LilyPad_LiPower.brd')
    newPart['eagleSchem'].append('/Hardware/LilyPad_LiPower.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

