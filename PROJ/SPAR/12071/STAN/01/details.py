
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12071"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12071"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('CC3000 WiFi Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/CC3000_WiFi_Shield')
    newPart['gitName'].append('CC3000_WiFi_Shield')
    newPart['eagleBoard'].append('/Hardware/CC3000_WiFi_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/CC3000_WiFi_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

