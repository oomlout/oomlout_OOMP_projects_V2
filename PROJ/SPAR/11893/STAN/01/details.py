
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11893"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11893"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad Simple Power')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_Simple_Power')
    newPart['gitName'].append('LilyPad_Simple_Power')
    newPart['eagleBoard'].append('/Hardware/LilyPad_Simple_Power.brd')
    newPart['eagleSchem'].append('/Hardware/LilyPad_Simple_Power.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

