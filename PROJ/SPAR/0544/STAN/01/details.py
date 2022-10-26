
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "0544"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0544"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('microSD Transflash Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/microSD_Transflash_Breakout')
    newPart['gitName'].append('microSD_Transflash_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_microSD_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_microSD_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

