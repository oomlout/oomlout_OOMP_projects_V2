
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15093"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15093"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Relay')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Relay')
    newPart['gitName'].append('Qwiic_Relay')
    newPart['eagleBoard'].append('/Hardware/Qwiic_Relay.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_Relay.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

