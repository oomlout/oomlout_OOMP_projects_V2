
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "19017"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR19017"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic 1.8V Adapter')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_1.8V_Adapter')
    newPart['gitName'].append('Qwiic_1.8V_Adapter')
    newPart['eagleBoard'].append('/Hardware/Qwiic_1.8V_Adapter.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_1.8V_Adapter.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

