
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15413"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15413"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic TMP117')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_TMP117')
    newPart['gitName'].append('Qwiic_TMP117')
    newPart['eagleBoard'].append('/Hardware/Qwiic_TMP117.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_TMP117.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

