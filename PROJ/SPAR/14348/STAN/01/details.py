
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14348"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14348"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic BME280 CCS811 Combo')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_BME280_CCS811_Combo')
    newPart['gitName'].append('Qwiic_BME280_CCS811_Combo')
    newPart['eagleBoard'].append('/Hardware/CSS811_BME280_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/CSS811_BME280_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

