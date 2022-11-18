
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16740"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16740"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Power Switch')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Power_Switch')
    newPart['gitName'].append('Qwiic_Power_Switch')
    newPart['eagleBoard'].append('/Hardware/Qwiic Power Switch.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic Power Switch.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

