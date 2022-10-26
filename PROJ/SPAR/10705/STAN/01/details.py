
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10705"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10705"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MyDAQ Protoboard Kit')
    newPart['gitRepo'].append('https://github.com/sparkfun/MyDAQ_Protoboard_Kit')
    newPart['gitName'].append('MyDAQ_Protoboard_Kit')
    newPart['eagleBoard'].append('/Hardware/MyDaq Breadboard.brd')
    newPart['eagleSchem'].append('/Hardware/MyDaq Breadboard.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

