
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14010"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14010"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad LED 5pcs')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_LED_5pcs')
    newPart['gitName'].append('LilyPad_LED_5pcs')
    newPart['eagleBoard'].append('/Hardware/LilyPad_LED_5pcs.brd')
    newPart['eagleSchem'].append('/Hardware/LilyPad_LED_5pcs.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

