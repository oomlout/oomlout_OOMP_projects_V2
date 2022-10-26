
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18575"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18575"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun MicroMod Main Board Single')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_MicroMod_Main_Board_Single')
    newPart['gitName'].append('SparkFun_MicroMod_Main_Board_Single')
    newPart['eagleBoard'].append('/Hardware/Main Board - Single.brd')
    newPart['eagleSchem'].append('/Hardware/Main Board - Single.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

