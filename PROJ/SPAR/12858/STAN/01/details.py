
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12858"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12858"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Vernier Interface Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/Vernier_Interface_Shield')
    newPart['gitName'].append('Vernier_Interface_Shield')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Vernier_Interface_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Vernier_Interface_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

