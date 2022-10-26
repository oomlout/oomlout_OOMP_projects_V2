
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "8619"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR8619"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ProtoBoard Wombat PTH')
    newPart['gitRepo'].append('https://github.com/sparkfun/ProtoBoard_Wombat-PTH')
    newPart['gitName'].append('ProtoBoard_Wombat-PTH')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Protoboard-PTH-v14.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Protoboard-PTH-v14.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

