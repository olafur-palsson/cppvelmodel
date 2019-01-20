
import os
import datetime as dt
import matplotlib.dates as mdates
InitialCNVfile = "hverahlid3.cnv"  # Name of the CNV database file to create
STATIONS = {"GEI": "XGEI", "LHL": "XLHL", "ASM": "XASM", "BJA": "XBJA", "EDA": "XEDA", "HAU": "XHAU",
            "HEI": "XHEI", "KAS": "XKAS", "KRO": "XKRO", "SAN": "XSAN", "SAU": "XSAU", "SOL": "XSOL", "SHR": "XSHR",
            "VOS": "XVOS", "HUMLI": "UMLI", "HVH": "XHVH", "IND": "XIND", "INNST": "NNST", "LSKAR": "SKAR",
            "SKARM": "KARM", "SVIN": "SVIN", "KRIST": "RIST", "GRAFN": "RAFN", "KOLDU": "OLDU", "NESJV": "ESJV",
            "SKEGG": "KEGG", "ORUST": "RUST", "TROLL": "ROLL", "HURD": "HURD", "LAKA": "LAKA", "VOG": "XVOG",
            "LAULA": "AULA", "SKINN": "KINN", "HAMAR": "AMAR", "LYTI": "LYTI", "GUNN": "GUNN", "GRV": "XGRV",
            "NYL": "XNYL", "RNE": "XRNE", "SIG": "XSIG", "MEL": "XMEL", "KVO": "XKVO", "RAH": "XRAH", "SYRA": "SYRA",
            "SYRD": "SYRD", "SYRN": "SYRN", "LANG": "LANG", "STMN": "STMN", "ELDBG": "LDBG", "GRA": "XGRA",
            "HLA": "XHLA", "MID": "XMID", "GAESK": "AESK", "DALFJ": "ALFJ", "BEINI": "EINI", "SBS": "XSBS",
            "SHN": "XSHN", "GFJ": "XGFJ", "HVET5": "VET5", "HVA": "XHVA", "THEIG": "HEIG", "SPB": "XSPB",
            "THORF": "HORF", "GRT": "XGRT", "SUH": "XSUH", "HSPHO": "SPHO", "LAUF": "LAUF", "YVIK": "YVIK",
            "SKI": "XSKI"}
# dictionary with the stations names so the names with a number of letters different to 4 can be
# easily changed to a 4 letter standar name

IN_FILES = os.listdir("database")  # Directory with the events files
V_Ids = list()                     # List where the valid events´ ids are added
EVENTS = dict()                    # Dictionary to add some of the valid events variables wwith its ID as a key

for file in IN_FILES:                                                             # Search in all files in the directory
    with open("database/"+file) as event:
        lineas = event.readlines()
    i = 0

    for linea in lineas:
        if "Public ID" in linea:                                                  # Read ID
            ID = linea[27:41]
        if "Date" in linea:                                                       # Read Date and time
            Timestring = linea[27:37]+lineas[i+1][27:39]
            Time = dt.datetime.strptime(Timestring, "%Y-%m-%d%H:%M:%S.%f")  # Save in 'datetime' variable
        if "Latitude   " in linea:                                                # Read Latitude
            LAT = float(linea[27:37])
        if "Longitude   " in linea:                                               # Read Longitude
            LON = float(linea[27:37])
        if "Depth    " in linea:                                                  # Read Depth
            Depth = float(linea[30:37])
            break                           # Stop reading file
        i += 1
    if 63.974 < LAT < 64.045:
        if -21.315 > LON > -21.38:
            V_Ids.append(ID)
            EVENTS[ID] = (Time, LAT, LON, Depth)        # Checking if the event is valid

CNVFILE = ""                                            # Variable where to input the tex as a string
CNVlist = list()                                        # List where all the string for each events are saved

for N_ID in V_Ids:                                          # For all the valid events
    with open("database/"+N_ID+".txt") as event2:
        lineas2 = event2.readlines()
    timestring2 = dt.datetime.strftime(EVENTS[N_ID][0], "%Y %m %d %H %M %S.%f")    # Convert the event
    # print(timestring2)                                                                 # variable into text
    Or_Year = int(timestring2[0:4])
    Or_Month = int(timestring2[5:7])
    Or_Day = int(timestring2[8:10])
    Or_Hour = int(timestring2[11:13])
    Or_Minute = int(timestring2[14:16])
    Or_Second = float(timestring2[17:23])                                              # convert the string into numbers
    # print(Or_Year, end=" ")
    # print(Or_Month, end=" ")
    # print(Or_Day, end=" ")
    # print(Or_Hour, end=":")
    # print(Or_Minute, end=":")
    # print(Or_Second)
    i = 0
    for linea2 in lineas2:
        i += 1
        if "Phase arrivals:" in linea2:                # Search for the line where the phases srtart to be listed
            break
    N_PH = int(lineas2[i-1][0:2])                      # Number of phases of this event
    phases = list()                                    # List to save the phases
    Autophases = 0                                     # Counter to keep an eye on the number of Autopick events
    for j in range(i+1, i+1+N_PH):
        SStr_station = lineas2[j][4:9]                 # Read the station name for the phase
        str_station = ""
        for letra in SStr_station:
            if letra != " ":
                str_station += letra                   # Eliminate white spaces
        if str_station in STATIONS:                    # use the STATIONS dictionary for the 4 letters name
            station = STATIONS[str_station]
        else:
            print(str_station+" "+str(len(str_station)))    # if the statsation name is not in the dictionary
            if len(str_station) < 4:                        # these lines create a 4-letter name
                station = "X"+str_station                # if the name is only 3 letters an X is added at the beggining
            elif len(str_station) == 4:
                station = str_station
            elif len(str_station) > 4:                  # if the name if longer than 4 letters, only the last 4 letters
                station = str_station[-4:]              # are taken

        fase = lineas2[j][32]                           # The type of phase is readed (P or S)
        thora = dt.datetime.strptime(lineas2[j][40:52], "%H:%M:%S.%f")   # the time of the phase is saved in a
        timestring3 = dt.datetime.strftime(thora, "%H %M %S.%f")         # time variable
        ph_Hour = int(timestring3[0:2])
        ph_minute = int(timestring3[3:5])
        ph_second = float(timestring3[6:12])                                    # the time of arrival is save in numbers

        # Calcualte the time difference between the event and the arrival in seconds:
        if Or_Hour > ph_Hour:
            # ESPECIAL CASE: if the event occurs at the end of one day and it's detected on the next day
            DeltaPhase = (60-Or_Second)+((59-Or_Minute)*60)+(ph_minute*60)+ph_second
            print("###CASO ESPECIAL DETECTADO###")
        else:
            DeltaPhase = ((ph_Hour-Or_Hour)*3600) + ((ph_minute-Or_Minute)*60) + (ph_second-Or_Second)
            # Normal case: the event and the arrival occurs in the same day
        # string = station+"1"+fase+" "+str(DeltaPhase)

        if DeltaPhase < 0:
            # if the time difference is negative we can assume that it is a bad picking and skip this phase
            print(N_ID)
            continue
        # The phase string is created STATION 4-letters name, Phase type and delta time of arrival
        string = "{0}{1}1{2:6.2f}".format(station, fase, DeltaPhase)

        if lineas2[j][61] == "A":  # if the phase is automatically picked the counters registered
            Autophases += 1
        phases.append(string)
    # end of the phases loop

    if Autophases > 3:             # Events with 3 or more Automatic picks are skiped
        print(N_ID+" Automaticks picks Alert")
        continue
    i = 0

    # The maginuted of the event per station are saved
    for linea2 in lineas2:
        i += 1
        if "Station magnitudes:" in linea2:
            break
    N_M = int(lineas2[i - 1][0:2])
    event_MAG_list = list()
    for j in range(i + 1, i + 1 + N_M):
        if "MLv" in lineas2[j]:
            event_MAG_list.append(float(lineas2[j][34:38]))
    j = 0
    MAG = 0.00
    for Magnitud in event_MAG_list:
        j += 1
        MAG += Magnitud
    MAG = MAG/j

    # These lines define the letters N, S, E, W dependin on the hemisphere location
    if EVENTS[N_ID][1] > 0:
        rLAT = EVENTS[N_ID][1]
        LM = "N"
    elif EVENTS[N_ID][1] < 0:
        rLAT = EVENTS[N_ID][1]*-1
        LM = "S"
    if EVENTS[N_ID][2] > 0:
        rLON = EVENTS[N_ID][2]
        LH = "E"
    elif EVENTS[N_ID][2] < 0:
        rLON = EVENTS[N_ID][2]*-1
        LH = "W"

    Y = str(Or_Year)[-2:]  # Only the 2 last digits of the year are added to the header
    # The Header of the event string is created
    event_string = """{0}{1:02}{2:02} {3:02}{4:02} {5:05.2f} {6:7.4f}{7} {8:8.4f}{9}{10:7.2f}{11:7.2f} 0"""\
        .format(Y, Or_Month, Or_Day, Or_Hour, Or_Minute, Or_Second, rLAT, LM, rLON, LH, EVENTS[N_ID][3], MAG)
    i = 0
    event_string += "\n"
    # the phases strings are added by rows of 6 event per row
    for element in phases:
        if i == 6:
            event_string += "\n"
            i = 0
        event_string += element
        i += 1
    event_string += "\n"
    event_string += "\n"

    # The event is added to the CNV file and CNV list
    CNVFILE += event_string
    CNVlist.append(event_string)
# End of the events loop

# Number of events on the CNV file
N_Events = len(CNVlist)
print(N_Events)

# The CNV file is written
with open(InitialCNVfile, 'w+') as Modelo:
    Modelo.write(CNVFILE)
