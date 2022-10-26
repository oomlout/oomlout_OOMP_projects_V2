
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11736"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11736"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('FT231X Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/FT231X_Breakout')
    newPart['gitName'].append('FT231X_Breakout')
    newPart['eagleBoard'].append('/hardware/ft231x-breakout.brd')
    newPart['eagleSchem'].append('/hardware/ft231x-breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

