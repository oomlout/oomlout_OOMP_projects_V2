
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16832"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16832"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('OpenLog Artemis')
    newPart['gitRepo'].append('https://github.com/sparkfun/OpenLog_Artemis')
    newPart['gitName'].append('OpenLog_Artemis')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Artemis_OpenLog.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Artemis_OpenLog.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

