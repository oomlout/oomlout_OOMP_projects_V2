
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16906"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16906"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Multi Port Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Multi_Port_Board')
    newPart['gitName'].append('Qwiic_Multi_Port_Board')
    newPart['eagleBoard'].append('/Qwiic_Multi_Port_Board/Qwiic_Multi_Port_Board.brd')
    newPart['eagleSchem'].append('/Qwiic_Multi_Port_Board/Qwiic_Multi_Port_Board.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

