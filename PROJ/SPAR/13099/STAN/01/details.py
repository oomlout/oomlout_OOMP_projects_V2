
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13099"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13099"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Rotary Switch Potentiometer')
    newPart['gitRepo'].append('https://github.com/sparkfun/Rotary_Switch_Potentiometer')
    newPart['gitName'].append('Rotary_Switch_Potentiometer')
    newPart['eagleBoard'].append('/Hardware/Rotary_Switch_Potentiometer.brd')
    newPart['eagleSchem'].append('/Hardware/Rotary_Switch_Potentiometer.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

