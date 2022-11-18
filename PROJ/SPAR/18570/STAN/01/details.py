
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18570"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18570"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic PC Fan Controller')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_PC_Fan_Controller')
    newPart['gitName'].append('Qwiic_PC_Fan_Controller')
    newPart['eagleBoard'].append('/Hardware/Qwiic_4_Pin_Fan_Controller.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_4_Pin_Fan_Controller.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

