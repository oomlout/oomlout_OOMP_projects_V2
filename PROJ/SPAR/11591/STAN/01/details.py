
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11591"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11591"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ISP Pogo Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/ISP_Pogo_Board')
    newPart['gitName'].append('ISP_Pogo_Board')
    newPart['eagleBoard'].append('/Hardware/ISP_Pogo_Board.brd')
    newPart['eagleSchem'].append('/Hardware/ISP_Pogo_Board.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

