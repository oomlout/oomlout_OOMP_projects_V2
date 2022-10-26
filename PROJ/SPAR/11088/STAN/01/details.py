
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11088"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11088"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Run SPOT Run')
    newPart['gitRepo'].append('https://github.com/sparkfun/Run-SPOT-Run')
    newPart['gitName'].append('Run-SPOT-Run')
    newPart['eagleBoard'].append('/Hardware/SatUplink.brd')
    newPart['eagleSchem'].append('/Hardware/SatUplink.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

