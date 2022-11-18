
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14783"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14783"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic LED Stick')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_LED_Stick')
    newPart['gitName'].append('Qwiic_LED_Stick')
    newPart['eagleBoard'].append('/Hardware/Qwiic LED Stick.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic LED Stick.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

