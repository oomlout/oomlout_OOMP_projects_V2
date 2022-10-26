
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15217"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15217"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LiPo Charger Plus')
    newPart['gitRepo'].append('https://github.com/sparkfun/LiPo_Charger_Plus')
    newPart['gitName'].append('LiPo_Charger_Plus')
    newPart['eagleBoard'].append('/Hardware/SparkFun_LiPo_Charger_Plus.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_LiPo_Charger_Plus.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

