
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12579"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12579"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Bluetooth Module Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/Bluetooth_Module_Breakout')
    newPart['gitName'].append('Bluetooth_Module_Breakout')
    newPart['eagleBoard'].append('/Hardware/RN41.brd')
    newPart['eagleSchem'].append('/Hardware/RN41.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

