def load(newPart,it):
    it['PROJ-ADAF-3191-STAN-01']['oompParts'] = [{'D1': {'OOMPID': 'DIOD-S323-X-K4148-01', 'FULL': {'PART': 'D1', 'PARTLETTER': 'D', 'VALUE': '1N4148', 'VALUENUMBER': '14148', 'DEVICE': 'DIODESOD-323', 'PACKAGE': 'SOD-323', 'PACKAGENUMBER': '323', 'DESC': 'Diode', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'D1,1N4148,DIODESOD-323,SOD-323,Diode,,'}}, 'D2': {'OOMPID': 'LEDS-0805-R-STAN-01', 'FULL': {'PART': 'D2', 'PARTLETTER': 'D', 'VALUE': 'RED', 'VALUENUMBER': '', 'DEVICE': 'LED0805_NOOUTLINE', 'PACKAGE': 'CHIPLED_0805_NOOUTLINE', 'PACKAGENUMBER': '0805', 'DESC': 'LED', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'D2,RED,LED0805_NOOUTLINE,CHIPLED_0805_NOOUTLINE,LED,,'}}, 'JP1': {'OOMPID': 'HEAD-UNMATCHED-X-UNMATCHED-01', 'FULL': {'PART': 'JP1', 'PARTLETTER': 'JP', 'VALUE': '', 'VALUENUMBER': '', 'DEVICE': 'HEADER-1X3_508TERM', 'PACKAGE': 'TERMBLOCK_1X3_5.08MM', 'PACKAGENUMBER': '13508', 'DESC': 'PIN HEADER', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'JP1,,HEADER-1X3_508TERM,TERMBLOCK_1X3_5.08MM,PIN HEADER,,'}}, 'JP2': {'OOMPID': 'HEAD-I01-X-PI01-01', 'FULL': {'PART': 'JP2', 'PARTLETTER': 'JP', 'VALUE': '', 'VALUENUMBER': '', 'DEVICE': 'HEADER-1X1ROUND', 'PACKAGE': '1X01_ROUND', 'PACKAGENUMBER': '101', 'DESC': 'PIN HEADER', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'JP2,,HEADER-1X1ROUND,1X01_ROUND,PIN HEADER,,'}}, 'MS2': {'OOMPID': 'SKIP-UNMATCHED-X-UNMATCHED-01', 'FULL': {'PART': 'MS2', 'PARTLETTER': 'MS', 'VALUE': 'FEATHERWING', 'VALUENUMBER': '', 'DEVICE': 'FEATHERWING', 'PACKAGE': 'FEATHERWING', 'PACKAGENUMBER': '', 'DESC': '', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'MS2,FEATHERWING,FEATHERWING,FEATHERWING,,,'}}, 'Q1': {'OOMPID': 'UNMATCHED-SO23-X-UNMATCHED-01', 'FULL': {'PART': 'Q1', 'PARTLETTER': 'Q', 'VALUE': 'MMBT2222', 'VALUENUMBER': '2222', 'DEVICE': 'TRANSISTOR_NPN', 'PACKAGE': 'SOT23-R', 'PACKAGENUMBER': '23', 'DESC': 'NPN Transistor', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'Q1,MMBT2222,TRANSISTOR_NPN,SOT23-R,NPN Transistor,,'}}, 'R1': {'OOMPID': 'RESE-0805-X-O102-01', 'FULL': {'PART': 'R1', 'PARTLETTER': 'R', 'VALUE': '1K', 'VALUENUMBER': '1', 'DEVICE': 'RESISTOR0805_NOOUTLINE', 'PACKAGE': '0805-NO', 'PACKAGENUMBER': '0805', 'DESC': 'Resistors', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R1,1K,RESISTOR0805_NOOUTLINE,0805-NO,Resistors,,'}}, 'R2': {'OOMPID': 'RESE-0805-X-O103-01', 'FULL': {'PART': 'R2', 'PARTLETTER': 'R', 'VALUE': '10K', 'VALUENUMBER': '10', 'DEVICE': 'RESISTOR0805_NOOUTLINE', 'PACKAGE': '0805-NO', 'PACKAGENUMBER': '0805', 'DESC': 'Resistors', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R2,10K,RESISTOR0805_NOOUTLINE,0805-NO,Resistors,,'}}, 'R3': {'OOMPID': 'RESE-0805-X-O102-01', 'FULL': {'PART': 'R3', 'PARTLETTER': 'R', 'VALUE': '1K', 'VALUENUMBER': '1', 'DEVICE': 'RESISTOR0805_NOOUTLINE', 'PACKAGE': '0805-NO', 'PACKAGENUMBER': '0805', 'DESC': 'Resistors', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R3,1K,RESISTOR0805_NOOUTLINE,0805-NO,Resistors,,'}}, 'SJ1': {'OOMPID': 'SKIP-UNMATCHED-X-UNMATCHED-01', 'FULL': {'PART': 'SJ1', 'PARTLETTER': 'SJ', 'VALUE': '', 'VALUENUMBER': '', 'DEVICE': 'SOLDERJUMPER_CLOSED', 'PACKAGE': 'SOLDERJUMPER_CLOSEDWIRE', 'PACKAGENUMBER': '', 'DESC': 'Solder Jumper - Closed', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'SJ1,,SOLDERJUMPER_CLOSED,SOLDERJUMPER_CLOSEDWIRE,Solder Jumper - Closed,,'}}, 'SJ2': {'OOMPID': 'SKIP-UNMATCHED-X-UNMATCHED-01', 'FULL': {'PART': 'SJ2', 'PARTLETTER': 'SJ', 'VALUE': '', 'VALUENUMBER': '', 'DEVICE': 'SOLDERJUMPER', 'PACKAGE': 'SOLDERJUMPER_ARROW_NOPASTE', 'PACKAGENUMBER': '', 'DESC': 'SMD Solder JUMPER', 'BOM': 'EXCLUDE', 'OWNER': 'ADAF', 'FULL': 'SJ2,,SOLDERJUMPER,SOLDERJUMPER_ARROW_NOPASTE,SMD Solder JUMPER,EXCLUDE,'}}, 'SJ3': {'OOMPID': 'SKIP-UNMATCHED-X-UNMATCHED-01', 'FULL': {'PART': 'SJ3', 'PARTLETTER': 'SJ', 'VALUE': '', 'VALUENUMBER': '', 'DEVICE': 'SOLDERJUMPER', 'PACKAGE': 'SOLDERJUMPER_ARROW_NOPASTE', 'PACKAGENUMBER': '', 'DESC': 'SMD Solder JUMPER', 'BOM': 'EXCLUDE', 'OWNER': 'ADAF', 'FULL': 'SJ3,,SOLDERJUMPER,SOLDERJUMPER_ARROW_NOPASTE,SMD Solder JUMPER,EXCLUDE,'}}, 'SJ4': {'OOMPID': 'SKIP-UNMATCHED-X-UNMATCHED-01', 'FULL': {'PART': 'SJ4', 'PARTLETTER': 'SJ', 'VALUE': '', 'VALUENUMBER': '', 'DEVICE': 'SOLDERJUMPER', 'PACKAGE': 'SOLDERJUMPER_ARROW_NOPASTE', 'PACKAGENUMBER': '', 'DESC': 'SMD Solder JUMPER', 'BOM': 'EXCLUDE', 'OWNER': 'ADAF', 'FULL': 'SJ4,,SOLDERJUMPER,SOLDERJUMPER_ARROW_NOPASTE,SMD Solder JUMPER,EXCLUDE,'}}, 'SJ7': {'OOMPID': 'SKIP-UNMATCHED-X-UNMATCHED-01', 'FULL': {'PART': 'SJ7', 'PARTLETTER': 'SJ', 'VALUE': '', 'VALUENUMBER': '', 'DEVICE': 'SOLDERJUMPER', 'PACKAGE': 'SOLDERJUMPER_ARROW_NOPASTE', 'PACKAGENUMBER': '', 'DESC': 'SMD Solder JUMPER', 'BOM': 'EXCLUDE', 'OWNER': 'ADAF', 'FULL': 'SJ7,,SOLDERJUMPER,SOLDERJUMPER_ARROW_NOPASTE,SMD Solder JUMPER,EXCLUDE,'}}, 'SJ8': {'OOMPID': 'SKIP-UNMATCHED-X-UNMATCHED-01', 'FULL': {'PART': 'SJ8', 'PARTLETTER': 'SJ', 'VALUE': '', 'VALUENUMBER': '', 'DEVICE': 'SOLDERJUMPER', 'PACKAGE': 'SOLDERJUMPER_ARROW_NOPASTE', 'PACKAGENUMBER': '', 'DESC': 'SMD Solder JUMPER', 'BOM': 'EXCLUDE', 'OWNER': 'ADAF', 'FULL': 'SJ8,,SOLDERJUMPER,SOLDERJUMPER_ARROW_NOPASTE,SMD Solder JUMPER,EXCLUDE,'}}, 'SJ9': {'OOMPID': 'SKIP-UNMATCHED-X-UNMATCHED-01', 'FULL': {'PART': 'SJ9', 'PARTLETTER': 'SJ', 'VALUE': '', 'VALUENUMBER': '', 'DEVICE': 'SOLDERJUMPER', 'PACKAGE': 'SOLDERJUMPER_ARROW_NOPASTE', 'PACKAGENUMBER': '', 'DESC': 'SMD Solder JUMPER', 'BOM': 'EXCLUDE', 'OWNER': 'ADAF', 'FULL': 'SJ9,,SOLDERJUMPER,SOLDERJUMPER_ARROW_NOPASTE,SMD Solder JUMPER,EXCLUDE,'}}, 'SJ16': {'OOMPID': 'SKIP-UNMATCHED-X-UNMATCHED-01', 'FULL': {'PART': 'SJ16', 'PARTLETTER': 'SJ', 'VALUE': '', 'VALUENUMBER': '', 'DEVICE': 'SOLDERJUMPER', 'PACKAGE': 'SOLDERJUMPER_ARROW_NOPASTE', 'PACKAGENUMBER': '', 'DESC': 'SMD Solder JUMPER', 'BOM': 'EXCLUDE', 'OWNER': 'ADAF', 'FULL': 'SJ16,,SOLDERJUMPER,SOLDERJUMPER_ARROW_NOPASTE,SMD Solder JUMPER,EXCLUDE,'}}, 'SJ17': {'OOMPID': 'SKIP-UNMATCHED-X-UNMATCHED-01', 'FULL': {'PART': 'SJ17', 'PARTLETTER': 'SJ', 'VALUE': '', 'VALUENUMBER': '', 'DEVICE': 'SOLDERJUMPER', 'PACKAGE': 'SOLDERJUMPER_ARROW_NOPASTE', 'PACKAGENUMBER': '', 'DESC': 'SMD Solder JUMPER', 'BOM': 'EXCLUDE', 'OWNER': 'ADAF', 'FULL': 'SJ17,,SOLDERJUMPER,SOLDERJUMPER_ARROW_NOPASTE,SMD Solder JUMPER,EXCLUDE,'}}, 'SJ18': {'OOMPID': 'SKIP-UNMATCHED-X-UNMATCHED-01', 'FULL': {'PART': 'SJ18', 'PARTLETTER': 'SJ', 'VALUE': '', 'VALUENUMBER': '', 'DEVICE': 'SOLDERJUMPER', 'PACKAGE': 'SOLDERJUMPER_ARROW_NOPASTE', 'PACKAGENUMBER': '', 'DESC': 'SMD Solder JUMPER', 'BOM': 'EXCLUDE', 'OWNER': 'ADAF', 'FULL': 'SJ18,,SOLDERJUMPER,SOLDERJUMPER_ARROW_NOPASTE,SMD Solder JUMPER,EXCLUDE,'}}, 'SJ19': {'OOMPID': 'SKIP-UNMATCHED-X-UNMATCHED-01', 'FULL': {'PART': 'SJ19', 'PARTLETTER': 'SJ', 'VALUE': '', 'VALUENUMBER': '', 'DEVICE': 'SOLDERJUMPER', 'PACKAGE': 'SOLDERJUMPER_ARROW_NOPASTE', 'PACKAGENUMBER': '', 'DESC': 'SMD Solder JUMPER', 'BOM': 'EXCLUDE', 'OWNER': 'ADAF', 'FULL': 'SJ19,,SOLDERJUMPER,SOLDERJUMPER_ARROW_NOPASTE,SMD Solder JUMPER,EXCLUDE,'}}, 'SJ20': {'OOMPID': 'SKIP-UNMATCHED-X-UNMATCHED-01', 'FULL': {'PART': 'SJ20', 'PARTLETTER': 'SJ', 'VALUE': '', 'VALUENUMBER': '', 'DEVICE': 'SOLDERJUMPER', 'PACKAGE': 'SOLDERJUMPER_ARROW_NOPASTE', 'PACKAGENUMBER': '', 'DESC': 'SMD Solder JUMPER', 'BOM': 'EXCLUDE', 'OWNER': 'ADAF', 'FULL': 'SJ20,,SOLDERJUMPER,SOLDERJUMPER_ARROW_NOPASTE,SMD Solder JUMPER,EXCLUDE,'}}, 'SW1': {'OOMPID': 'BUTA-4628-X-STAN-01', 'FULL': {'PART': 'SW1', 'PARTLETTER': 'SW', 'VALUE': 'KMR2', 'VALUENUMBER': '2', 'DEVICE': 'SWITCH_TACT_SMT4.6X2.8', 'PACKAGE': 'BTN_KMR2_4.6X2.8', 'PACKAGENUMBER': '24628', 'DESC': 'SMT Tact Switches', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'SW1,KMR2,SWITCH_TACT_SMT4.6X2.8,BTN_KMR2_4.6X2.8,SMT Tact Switches,,'}}, 'U$1': {'OOMPID': 'SKIP-UNMATCHED-X-UNMATCHED-01', 'FULL': {'PART': 'U$1', 'PARTLETTER': 'U$', 'VALUE': 'RELAY_G5LE', 'VALUENUMBER': '_5', 'DEVICE': 'RELAY_G5LE', 'PACKAGE': 'RELAY_G5LE-1', 'PACKAGENUMBER': '51', 'DESC': '', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'U$1,RELAY_G5LE,RELAY_G5LE,RELAY_G5LE-1,,,'}}}]
