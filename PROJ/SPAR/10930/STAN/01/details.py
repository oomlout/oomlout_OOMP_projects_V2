
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10930"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10930"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ClockIt')
    newPart['gitRepo'].append('https://github.com/sparkfun/ClockIt')
    newPart['gitName'].append('ClockIt')
    newPart['eagleBoard'].append('/Hardware/Clock-v16.brd')
    newPart['eagleSchem'].append('/Hardware/Clock-v16.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

