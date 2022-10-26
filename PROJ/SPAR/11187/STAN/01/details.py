
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11187"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11187"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('5 Way Tactile Switch Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/5-Way_Tactile_Switch_Breakout')
    newPart['gitName'].append('5-Way_Tactile_Switch_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_5-Way_Tactile_Switch_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_5-Way_Tactile_Switch_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

