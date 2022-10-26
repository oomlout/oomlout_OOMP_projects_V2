
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12702"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12702"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Solderable Breadboard Mini')
    newPart['gitRepo'].append('https://github.com/sparkfun/Solderable_Breadboard_Mini')
    newPart['gitName'].append('Solderable_Breadboard_Mini')
    newPart['eagleBoard'].append('/hardware/solderable_breadboard_mini.brd')
    newPart['eagleSchem'].append('/hardware/solderable_breadboard_mini.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

