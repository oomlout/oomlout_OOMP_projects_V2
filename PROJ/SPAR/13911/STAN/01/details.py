
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13911"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13911"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Serial Controlled Motor Driver')
    newPart['gitRepo'].append('https://github.com/sparkfun/Serial_Controlled_Motor_Driver')
    newPart['gitName'].append('Serial_Controlled_Motor_Driver')
    newPart['eagleBoard'].append('/Hardware/Serial Controlled Motor Driver.brd')
    newPart['eagleSchem'].append('/Hardware/Serial Controlled Motor Driver.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

