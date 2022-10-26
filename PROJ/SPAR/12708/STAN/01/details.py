
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12708"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12708"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RTC Module')
    newPart['gitRepo'].append('https://github.com/sparkfun/RTC-Module')
    newPart['gitName'].append('RTC-Module')
    newPart['eagleBoard'].append('/hardware/RTC-Module.brd')
    newPart['eagleSchem'].append('/hardware/RTC-Module.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

