
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14531"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14531"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Pioneer IoT Kit Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/Pioneer_IoT_Kit_Shield')
    newPart['gitName'].append('Pioneer_IoT_Kit_Shield')
    newPart['eagleBoard'].append('/Hardware/Pioneer_Kit_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/Pioneer_Kit_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

