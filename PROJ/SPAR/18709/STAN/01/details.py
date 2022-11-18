
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18709"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18709"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('PoE Power Supply')
    newPart['gitRepo'].append('https://github.com/sparkfun/PoE_Power_Supply')
    newPart['gitName'].append('PoE_Power_Supply')
    newPart['eagleBoard'].append('/Hardware/POE_Power_Supply.brd')
    newPart['eagleSchem'].append('/Hardware/POE_Power_Supply.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

