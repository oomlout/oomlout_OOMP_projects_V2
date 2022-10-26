
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17722"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17722"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroMod GNSS F9P Carrier Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroMod_GNSS_F9P_Carrier_Board')
    newPart['gitName'].append('MicroMod_GNSS_F9P_Carrier_Board')
    newPart['eagleBoard'].append('/Hardware/F9P_Carrier_Board.brd')
    newPart['eagleSchem'].append('/Hardware/F9P_Carrier_Board.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

