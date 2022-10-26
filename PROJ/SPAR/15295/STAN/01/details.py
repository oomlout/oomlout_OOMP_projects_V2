
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15295"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15295"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun PCB Ruler')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_PCB_Ruler')
    newPart['gitName'].append('SparkFun_PCB_Ruler')
    newPart['eagleBoard'].append('/Hardware/SparkFunRuler.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFunRuler.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

