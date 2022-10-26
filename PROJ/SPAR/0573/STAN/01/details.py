
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "0573"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0573"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SIM Card Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/SIM_Card_Breakout')
    newPart['gitName'].append('SIM_Card_Breakout')
    newPart['eagleBoard'].append('/Hardware/Sim_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/Sim_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

