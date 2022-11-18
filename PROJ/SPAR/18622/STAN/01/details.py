
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18622"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18622"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkX smol Power Board LiPo')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkX_smol_Power_Board_LiPo')
    newPart['gitName'].append('SparkX_smol_Power_Board_LiPo')
    newPart['eagleBoard'].append('/Hardware/SparkX_smol_LiPo_Power.brd')
    newPart['eagleSchem'].append('/Hardware/SparkX_smol_LiPo_Power.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

