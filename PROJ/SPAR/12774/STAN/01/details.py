
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12774"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12774"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('BeagleBone Black Proto Cape')
    newPart['gitRepo'].append('https://github.com/sparkfun/BeagleBone_Black_Proto_Cape')
    newPart['gitName'].append('BeagleBone_Black_Proto_Cape')
    newPart['eagleBoard'].append('/Hardware/BBB_Breakout_Cape.brd')
    newPart['eagleSchem'].append('/Hardware/BBB_Breakout_Cape.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

