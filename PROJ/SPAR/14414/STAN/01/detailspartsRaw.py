def load(newPart,it):
    it['PROJ-SPAR-14414-STAN-01']['rawParts'] = [{'kicadBom': [], 'eagleBom': [{'Part': 'B1', 'Value': '6.8MM_COIN_CELL', 'Device': 'BATTERY-6.8MM_SMD', 'Package': 'BATTCON-6.8MM', 'Description': 'Battery - Single Cell', 'BOM': 'BATT-13734'}, {'Part': 'C1', 'Value': '0.1uF', 'Device': '0.1UF-0603-25V-(+80/-20%)', 'Package': '0603', 'Description': '0.1µF ceramic capacitors', 'BOM': 'CAP-00810'}, {'Part': 'C2', 'Value': '1.0uF', 'Device': '1.0UF-0603-16V-10%', 'Package': '0603', 'Description': '1µF ceramic capacitors', 'BOM': 'CAP-00868'}, {'Part': 'C3', 'Value': '1.0uF', 'Device': '1.0UF-0603-16V-10%', 'Package': '0603', 'Description': '1µF ceramic capacitors', 'BOM': 'CAP-00868'}, {'Part': 'C4', 'Value': '1.0uF', 'Device': '1.0UF-0603-16V-10%', 'Package': '0603', 'Description': '1µF ceramic capacitors', 'BOM': 'CAP-00868'}, {'Part': 'D1', 'Value': 'BLUE', 'Device': 'LED-BLUE0603', 'Package': 'LED-0603', 'Description': 'Blue SMD LED', 'BOM': 'DIO-08575'}, {'Part': 'D2', 'Value': '0.5A/40V/420mV', 'Device': 'DIODE-SCHOTTKY-PMEG4005EJ', 'Package': 'SOD-323', 'Description': 'Schottky diode', 'BOM': 'DIO-10955'}, {'Part': 'FB1', 'Value': '600Ohm/100MHz', 'Device': 'FERRITE_BEAD-0603', 'Package': '0603', 'Description': 'Ferrite Bead (blocks, cores, rings, chokes, etc.)', 'BOM': 'NDUC-07859'}, {'Part': 'FRAME1', 'Value': 'FRAME-LETTER', 'Device': 'FRAME-LETTER', 'Package': 'CREATIVE_COMMONS', 'Description': 'Schematic Frame - Letter', 'BOM': ''}, {'Part': 'J1', 'Value': 'U.FL', 'Device': 'U.FL2PIN', 'Package': 'U.FL', 'Description': 'SMD Antenna Connector - U.FL', 'BOM': 'CONN-09193'}, {'Part': 'J2', 'Value': 'Qwiic Right Angle', 'Device': 'I2C_STANDARDQWIIC', 'Package': '1X04_1MM_RA', 'Description': 'SparkFun I2C Standard Pinout Header', 'BOM': 'CONN-13729'}, {'Part': 'J3', 'Value': 'PTH', 'Device': 'I2C_STANDARD_NO_SILK', 'Package': '1X04_NO_SILK', 'Description': 'SparkFun I2C Standard Pinout Header', 'BOM': ''}, {'Part': 'J4', 'Value': 'Qwiic Right Angle', 'Device': 'I2C_STANDARDQWIIC', 'Package': '1X04_1MM_RA', 'Description': 'SparkFun I2C Standard Pinout Header', 'BOM': 'CONN-13729'}, {'Part': 'J5', 'Value': '', 'Device': 'CONN_01PTH_NO_SILK_YES_STOP', 'Package': '1X01_NO_SILK', 'Description': 'Single connection point. Often used as Generic Header-pin footprint for 0.1 inch spaced/style header connections', 'BOM': ''}, {'Part': 'J7', 'Value': '', 'Device': 'CONN_05NO_SILK', 'Package': '1X05_NO_SILK', 'Description': 'Multi connection point. Often used as Generic Header-pin footprint for 0.1 inch spaced/style header connections', 'BOM': ''}, {'Part': 'JP1', 'Value': '', 'Device': 'JUMPER-SMT_3_2-NC_PASTE_SILK', 'Package': 'SMT-JUMPER_3_2-NC_PASTE_SILK', 'Description': 'Normally closed solder jumper (2 of 2 connections)', 'BOM': ''}, {'Part': 'JP2', 'Value': 'FIDUCIALUFIDUCIAL', 'Device': 'FIDUCIALUFIDUCIAL', 'Package': 'MICRO-FIDUCIAL', 'Description': 'Fiducial Alignment Points', 'BOM': ''}, {'Part': 'JP3', 'Value': 'STAND-OFF', 'Device': 'STAND-OFF', 'Package': 'STAND-OFF', 'Description': 'Stand Off', 'BOM': ''}, {'Part': 'JP4', 'Value': 'STAND-OFF', 'Device': 'STAND-OFF', 'Package': 'STAND-OFF', 'Description': 'Stand Off', 'BOM': ''}, {'Part': 'JP5', 'Value': '', 'Device': 'JUMPER-SMT_2_NC_TRACE_NO-SILK', 'Package': 'SMT-JUMPER_2_NC_TRACE_NO-SILK', 'Description': 'Normally closed trace jumper', 'BOM': ''}, {'Part': 'JP6', 'Value': 'FIDUCIALUFIDUCIAL', 'Device': 'FIDUCIALUFIDUCIAL', 'Package': 'MICRO-FIDUCIAL', 'Description': 'Fiducial Alignment Points', 'BOM': ''}, {'Part': 'JP7', 'Value': 'FIDUCIALUFIDUCIAL', 'Device': 'FIDUCIALUFIDUCIAL', 'Package': 'MICRO-FIDUCIAL', 'Description': 'Fiducial Alignment Points', 'BOM': ''}, {'Part': 'JP8', 'Value': 'FIDUCIALUFIDUCIAL', 'Device': 'FIDUCIALUFIDUCIAL', 'Package': 'MICRO-FIDUCIAL', 'Description': 'Fiducial Alignment Points', 'BOM': ''}, {'Part': 'L1', 'Value': '33nH/±5%/500mA', 'Device': 'INDUCTOR-0603-33NH', 'Package': '0603', 'Description': 'Inductors', 'BOM': 'NDUC-07874'}, {'Part': 'LOGO1', 'Value': 'OSHW-LOGOMINI', 'Device': 'OSHW-LOGOMINI', 'Package': 'OSHW-LOGO-MINI', 'Description': 'Open-Source Hardware (OSHW) Logo', 'BOM': ''}, {'Part': 'LOGO2', 'Value': 'SFE_LOGO_NAME_FLAME.1_INCH', 'Device': 'SFE_LOGO_NAME_FLAME.1_INCH', 'Package': 'SFE_LOGO_NAME_FLAME_.1', 'Description': 'SparkFun Font Logo w/ Flame', 'BOM': ''}, {'Part': 'LOGO3', 'Value': 'REVISION', 'Device': 'REVISION', 'Package': 'REVISION', 'Description': 'Revision By Text', 'BOM': ''}, {'Part': 'R1', 'Value': '10k', 'Device': '10KOHM-0603-1/10W-1%', 'Package': '0603', 'Description': '10kΩ resistor', 'BOM': 'RES-00824'}, {'Part': 'R2', 'Value': '10k', 'Device': '10KOHM-0603-1/10W-1%', 'Package': '0603', 'Description': '10kΩ resistor', 'BOM': 'RES-00824'}, {'Part': 'R3', 'Value': '470', 'Device': '470OHM-0603-1/10W-1%', 'Package': '0603', 'Description': '470Ω resistor', 'BOM': 'RES-07869'}, {'Part': 'R5', 'Value': '1k', 'Device': '1KOHM-0603-1/10W-1%', 'Package': '0603', 'Description': '1kΩ resistor', 'BOM': 'RES-07856'}, {'Part': 'R6', 'Value': '470', 'Device': '470OHM-0603-1/10W-1%', 'Package': '0603', 'Description': '470Ω resistor', 'BOM': 'RES-07869'}, {'Part': 'R7', 'Value': '4.7k', 'Device': '4.7KOHM-0603-1/10W-1%', 'Package': '0603', 'Description': '4.7kΩ resistor', 'BOM': 'RES-07857'}, {'Part': 'R8', 'Value': '4.7k', 'Device': '4.7KOHM-0603-1/10W-1%', 'Package': '0603', 'Description': '4.7kΩ resistor', 'BOM': 'RES-07857'}, {'Part': 'R11', 'Value': '470', 'Device': '470OHM-0603-1/10W-1%', 'Package': '0603', 'Description': '470Ω resistor', 'BOM': 'RES-07869'}, {'Part': 'U$3', 'Value': 'SPECIAL_INSTRUCTIONS-PRODUCTION', 'Device': 'SPECIAL_INSTRUCTIONS-PRODUCTION', 'Package': 'PRODUCTION_INSTRUCTIONS', 'Description': 'Special Ordering/Production Instructions Alert', 'BOM': ''}, {'Part': 'U1', 'Value': 'Titan X1 GPS', 'Device': 'TITAN_X1_GPS', 'Package': 'TITAN_X1_GPS', 'Description': 'Titan X1 GPS', 'BOM': 'GPS-13693'}]}, {}]
