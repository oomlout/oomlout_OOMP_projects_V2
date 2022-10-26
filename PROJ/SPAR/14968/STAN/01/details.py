
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14968"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14968"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('gator control')
    newPart['gitRepo'].append('https://github.com/sparkfun/gator_control')
    newPart['gitName'].append('gator_control')
    newPart['eagleBoard'].append('/Hardware/gatorBytes_button_board.brd')
    newPart['eagleSchem'].append('/Hardware/gatorBytes_button_board.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

