
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11468"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11468"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SD Sniffer')
    newPart['gitRepo'].append('https://github.com/sparkfun/SD_Sniffer')
    newPart['gitName'].append('SD_Sniffer')
    newPart['eagleBoard'].append('/hardware/SD_Sniffer.brd')
    newPart['eagleSchem'].append('/hardware/SD_Sniffer.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

