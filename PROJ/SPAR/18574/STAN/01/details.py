
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18574"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18574"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/RFM97CW Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/RFM97CW_Breakout')
    newPart['gitName'].append('https://github.com/sparkfunX/RFM97CW_Breakout')
    newPart['eagleBoard'].append('sourceFiles/git/RFM97CW_Breakout/Hardware/SparkFun_RFM97CW_Breakout.brd')
    newPart['eagleSchem'].append('sourceFiles/git/RFM97CW_Breakout/Hardware/SparkFun_RFM97CW_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

