
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14495"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14495"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Adapter')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Adapter')
    newPart['gitName'].append('Qwiic_Adapter')
    newPart['eagleBoard'].append('/Hardware/SparkFun Qwiic Adapter.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun Qwiic Adapter.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

