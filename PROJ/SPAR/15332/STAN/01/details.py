
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15332"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15332"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Artemis')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Artemis')
    newPart['gitName'].append('SparkFun_Artemis')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Artemis.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Artemis.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

