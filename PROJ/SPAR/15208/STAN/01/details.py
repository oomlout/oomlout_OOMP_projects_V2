
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15208"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15208"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Buck Boost')
    newPart['gitRepo'].append('https://github.com/sparkfun/Buck-Boost')
    newPart['gitName'].append('Buck-Boost')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Buck-Boost.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Buck-Boost.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

