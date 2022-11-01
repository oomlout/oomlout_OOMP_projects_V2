
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ELLA"
    oColor = "0004"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0004"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('riscystick')
    newPart['gitRepo'].append('https://github.com/electrolama/riscystick')
    newPart['gitName'].append('riscystick')
    newPart['eagleBoard'].append('hardware/Revision A1/riscystick-RevA1.brd')
    newPart['eagleSchem'].append('hardware/Revision A1/riscystick-RevA1.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

