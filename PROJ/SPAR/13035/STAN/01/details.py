
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13035"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13035"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Edison OLED Block')
    newPart['gitRepo'].append('https://github.com/sparkfun/Edison_OLED_Block')
    newPart['gitName'].append('Edison_OLED_Block')
    newPart['eagleBoard'].append('/Hardware/oled_block.brd')
    newPart['eagleSchem'].append('/Hardware/oled_block.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

