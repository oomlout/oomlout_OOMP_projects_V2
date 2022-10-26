
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10936"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10936"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Bar Graph Breakout Kit')
    newPart['gitRepo'].append('https://github.com/sparkfun/Bar_Graph_Breakout_Kit')
    newPart['gitName'].append('Bar_Graph_Breakout_Kit')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Bar_Graph_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Bar_Graph_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

