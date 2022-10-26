
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11509"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11509"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Papilio Button LED Wing')
    newPart['gitRepo'].append('https://github.com/sparkfun/Papilio_Button_LED_Wing')
    newPart['gitName'].append('Papilio_Button_LED_Wing')
    newPart['eagleBoard'].append('/Hardware/Papilio-Button_LED_Wing.brd')
    newPart['eagleSchem'].append('/Hardware/Papilio-Button_LED_Wing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

