
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13033"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13033"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Edison 9DOF Block')
    newPart['gitRepo'].append('https://github.com/sparkfun/Edison_9DOF_Block')
    newPart['gitName'].append('Edison_9DOF_Block')
    newPart['eagleBoard'].append('/Hardware/9dof_block.brd')
    newPart['eagleSchem'].append('/Hardware/9dof_block.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

