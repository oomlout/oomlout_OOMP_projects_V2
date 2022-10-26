
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9056"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9056"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Analog Digital MUX Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/Analog_Digital_MUX_Breakout')
    newPart['gitName'].append('Analog_Digital_MUX_Breakout')
    newPart['eagleBoard'].append('/Hardware/Analog-Digital-Mux-Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/Analog-Digital-Mux-Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

