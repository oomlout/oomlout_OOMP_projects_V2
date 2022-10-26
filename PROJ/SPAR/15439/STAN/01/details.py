
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15439"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15439"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('PCA9306 Level Translator Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/PCA9306_Level_Translator_Breakout')
    newPart['gitName'].append('PCA9306_Level_Translator_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Level_Translator_PCA9306.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Level_Translator_PCA9306.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

