
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "20000"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR20000"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun RTK Facet')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_RTK_Facet')
    newPart['gitName'].append('SparkFun_RTK_Facet')
    newPart['eagleBoard'].append('/Hardware/Connector/SparkFun RTK Facet - External Connector.brd')
    newPart['eagleSchem'].append('/Hardware/Connector/SparkFun RTK Facet - External Connector.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

