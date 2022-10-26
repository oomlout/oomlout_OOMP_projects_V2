
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14666"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14666"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Flex Glove Controller')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Flex_Glove_Controller')
    newPart['gitName'].append('Qwiic_Flex_Glove_Controller')
    newPart['eagleBoard'].append('/Hardware/Qwiic Flex Glove Controller.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic Flex Glove Controller.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

