
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "0258"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0258"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Serial Enabled LCD Backpack')
    newPart['gitRepo'].append('https://github.com/sparkfun/Serial_Enabled_LCD_Backpack')
    newPart['gitName'].append('Serial_Enabled_LCD_Backpack')
    newPart['eagleBoard'].append('/Hardware/Serial LCD Backpack v28.brd')
    newPart['eagleSchem'].append('/Hardware/Serial LCD Backpack v28.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

