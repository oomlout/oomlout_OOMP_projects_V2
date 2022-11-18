
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14241"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14241"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Air Quality Combo Board CCS811 BME280')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Air_Quality_Combo_Board-CCS811-BME280')
    newPart['gitName'].append('Qwiic_Air_Quality_Combo_Board-CCS811-BME280')
    newPart['eagleBoard'].append('/Hardware/Qwiic_Air_Quality_Combo_Board-CCS811-BME280.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_Air_Quality_Combo_Board-CCS811-BME280.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

