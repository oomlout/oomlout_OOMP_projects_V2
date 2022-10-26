
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11447"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11447"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Wake on shake')
    newPart['gitRepo'].append('https://github.com/sparkfun/Wake_on_shake')
    newPart['gitName'].append('Wake_on_shake')
    newPart['eagleBoard'].append('/Hardware/ADXL362WakeOnShake.brd')
    newPart['eagleSchem'].append('/Hardware/ADXL362WakeOnShake.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

