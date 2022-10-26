
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16790"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16790"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Shield for Thing Plus')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Shield_for_Thing_Plus')
    newPart['gitName'].append('Qwiic_Shield_for_Thing_Plus')
    newPart['eagleBoard'].append('/Hardware/Qwiic_Shield_for_Thing_Plus.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_Shield_for_Thing_Plus.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

