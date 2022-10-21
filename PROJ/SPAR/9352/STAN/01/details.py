
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9352"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9352"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('GraphicLCD Serial Backpack')
    newPart['gitRepo'].append('https://github.com/sparkfun/GraphicLCD_Serial_Backpack')
    newPart['gitName'].append('GraphicLCD_Serial_Backpack')
    newPart['eagleBoard'].append('/Hardware/Graphic LCD Backpack.brd')
    newPart['eagleSchem'].append('/Hardware/Graphic LCD Backpack.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

