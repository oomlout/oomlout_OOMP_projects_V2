
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15334"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15334"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Qwiic 12 Bit ADC   4 Channel ADS1015')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Qwiic_12_Bit_ADC_-_4_Channel_ADS1015')
    newPart['gitName'].append('SparkFun_Qwiic_12_Bit_ADC_-_4_Channel_ADS1015')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Qwiic_12_Bit_ADC_-_4_Channel_ADS1015.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Qwiic_12_Bit_ADC_-_4_Channel_ADS1015.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

