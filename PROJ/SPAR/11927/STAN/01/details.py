
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11927"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11927"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('BC127 Breakout Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/BC127_Breakout_Board')
    newPart['gitName'].append('BC127_Breakout_Board')
    newPart['eagleBoard'].append('/Hardware/BC127_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/BC127_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

