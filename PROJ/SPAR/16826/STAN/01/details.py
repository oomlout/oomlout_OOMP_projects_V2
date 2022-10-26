
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16826"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16826"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Pulsed Radar Breakout A111')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Pulsed_Radar_Breakout_A111')
    newPart['gitName'].append('SparkFun_Pulsed_Radar_Breakout_A111')
    newPart['eagleBoard'].append('/Hardware/A111_Pulsed_Radar_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/A111_Pulsed_Radar_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

