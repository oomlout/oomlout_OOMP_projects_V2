
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14349"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14349"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Human Presence Sensor Breakout AK9753')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Human_Presence_Sensor_Breakout_AK9753')
    newPart['gitName'].append('Qwiic_Human_Presence_Sensor_Breakout_AK9753')
    newPart['eagleBoard'].append('/Hardware/AK9753 Human Movement Sensor.brd')
    newPart['eagleSchem'].append('/Hardware/AK9753 Human Movement Sensor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

