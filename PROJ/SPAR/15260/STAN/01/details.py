
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15260"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15260"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/SparkX Pi Filter Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/SparkX-Pi-Filter-Breakout')
    newPart['gitName'].append('https://github.com/sparkfunX/SparkX-Pi-Filter-Breakout')
    newPart['eagleBoard'].append('sourceFiles/git/SparkX-Pi-Filter-Breakout/Hardware/SparkX-Pi-Filter.brd')
    newPart['eagleSchem'].append('sourceFiles/git/SparkX-Pi-Filter-Breakout/Hardware/SparkX-Pi-Filter.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

