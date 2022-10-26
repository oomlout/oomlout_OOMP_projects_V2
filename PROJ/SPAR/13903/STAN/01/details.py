
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13903"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13903"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad LED Rainbow')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_LED_Rainbow')
    newPart['gitName'].append('LilyPad_LED_Rainbow')
    newPart['eagleBoard'].append('/Hardware/LilyPad_Rainbow_LED_v02.brd')
    newPart['eagleSchem'].append('/Hardware/LilyPad_Rainbow_LED_v02.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

