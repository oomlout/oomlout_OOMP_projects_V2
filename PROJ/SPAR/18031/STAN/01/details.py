
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18031"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18031"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun LTE GNSS Breakout SARA R510M8S')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_LTE_GNSS_Breakout_SARA-R510M8S')
    newPart['gitName'].append('SparkFun_LTE_GNSS_Breakout_SARA-R510M8S')
    newPart['eagleBoard'].append('/Hardware/SparkFun_LTE_GNSS_Breakout_SARA-R510M8S.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_LTE_GNSS_Breakout_SARA-R510M8S.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

