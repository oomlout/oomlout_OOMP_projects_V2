
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14030"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14030"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Mini GPS Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/Mini_GPS_Shield')
    newPart['gitName'].append('Mini_GPS_Shield')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Mini_GPS_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Mini_GPS_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

