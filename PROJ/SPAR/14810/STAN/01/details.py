
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14810"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14810"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MP3 Breakout WT2003S')
    newPart['gitRepo'].append('https://github.com/sparkfun/MP3_Breakout_WT2003S')
    newPart['gitName'].append('MP3_Breakout_WT2003S')
    newPart['eagleBoard'].append('/Hardware/MP3 Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/MP3 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

