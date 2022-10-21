
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "0760"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0760"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LED Matrix Serial Interface RGB')
    newPart['gitRepo'].append('https://github.com/sparkfun/LED_Matrix_Serial_Interface_RGB')
    newPart['gitName'].append('LED_Matrix_Serial_Interface_RGB')
    newPart['eagleBoard'].append('/Hardware/RGB Matrix.brd')
    newPart['eagleSchem'].append('/Hardware/RGB Matrix.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

