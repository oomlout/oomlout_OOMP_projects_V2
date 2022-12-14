
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11168"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11168"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('AVR ISP Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/AVR_ISP_Shield')
    newPart['gitName'].append('AVR_ISP_Shield')
    newPart['eagleBoard'].append('/Hardware/AVR_ISP-Shield-v11.brd')
    newPart['eagleSchem'].append('/Hardware/AVR_ISP-Shield-v11.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

