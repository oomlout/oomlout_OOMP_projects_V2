
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "0114"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0114"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Breadboard Power Supply 5V 3.3V')
    newPart['gitRepo'].append('https://github.com/sparkfun/Breadboard_Power_Supply_5V_3.3V')
    newPart['gitName'].append('Breadboard_Power_Supply_5V_3.3V')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Breadboard_Power_Supply_5_3.3V.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Breadboard_Power_Supply_5_3.3V.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

