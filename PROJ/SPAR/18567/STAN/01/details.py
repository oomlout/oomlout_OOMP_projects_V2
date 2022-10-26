
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18567"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18567"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('WiFi Shield DA16200')
    newPart['gitRepo'].append('https://github.com/sparkfun/WiFi_Shield-DA16200')
    newPart['gitName'].append('WiFi_Shield-DA16200')
    newPart['eagleBoard'].append('/Hardware/SparkFun WiFi Shield - DA16200.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun WiFi Shield - DA16200.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

