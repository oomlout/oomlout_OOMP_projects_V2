
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ELLA"
    oColor = "0002"
    oDesc = "STAN"
    oIndex = "0A"
    hexID = "PRPR0002"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Zoe Rev A')
    newPart['gitRepo'].append('https://github.com/electrolama/zoe')
    newPart['gitName'].append('zoe')
    newPart['eagleBoard'].append('/Revision A/pi-zigbee-poe-rtc.brd')
    newPart['eagleSchem'].append('/Revision A/pi-zigbee-poe-rtc.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

