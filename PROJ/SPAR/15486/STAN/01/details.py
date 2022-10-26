
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15486"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15486"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('gator rtc')
    newPart['gitRepo'].append('https://github.com/sparkfun/gator_rtc')
    newPart['gitName'].append('gator_rtc')
    newPart['eagleBoard'].append('/Hardware/Gator_rtc.brd')
    newPart['eagleSchem'].append('/Hardware/Gator_rtc.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

