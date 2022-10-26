
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11622"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11622"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RedBot with Optical Encoder')
    newPart['gitRepo'].append('https://github.com/sparkfun/RedBot_with_Optical_Encoder')
    newPart['gitName'].append('RedBot_with_Optical_Encoder')
    newPart['eagleBoard'].append('/Hardware/RedBot.brd')
    newPart['eagleSchem'].append('/Hardware/RedBot.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

