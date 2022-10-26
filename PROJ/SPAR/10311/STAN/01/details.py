
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10311"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10311"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('PicoBoard')
    newPart['gitRepo'].append('https://github.com/sparkfun/PicoBoard')
    newPart['gitName'].append('PicoBoard')
    newPart['eagleBoard'].append('/hardware/PicoBoard.brd')
    newPart['eagleSchem'].append('/hardware/PicoBoard.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

