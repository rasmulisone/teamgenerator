import faker, random, openpyxl, time
print("Football team generator 1.0")
print("(C) 2019 Rasmulisone Games")
print("")
countries = ["Heigery", "Raceny", "Zilk", "Milestan", "Beanthe", "Fushaly", "Orda", "Berter"]
allpos_ = ["GK", "RB", "CB", "CB", "LB", "RM", "CM", "LM", "CDM", "CAM", "ST", "ST", "RW", "LW"]
allpos = ["GK", "RB", "CB", "LB", "RM", "CM", "LM", "CDM", "CAM", "ST", "RW", "LW"]
allcountries = []
print("Reading countries.txt...")
file = open("countries.txt")
for line in file:
    allcountries.append(line.strip())
print("Completed.")
langs = []
print("Reading locales.txt...")
langfile = open("locales.txt")
for line in langfile:
    langs.append(line.strip())
print("Completed.")
print("")
while True:
    teamovr_ = input("Team overall (1-99): ")
    if teamovr_ == "exit":
        break
    else:
        teamovr = int(teamovr_)
    var = int(input("Overall variation (+/-): "))
    teamcountry = input("Team country: ")
    GK = 0
    RB = 0
    CB = 0
    LB = 0
    RM = 0
    CM = 0
    LM = 0
    CDM = 0
    CAM = 0
    ST = 0
    RW = 0
    LW = 0
    defenders = 0
    midfielders = 0
    forwards = 0
    squad = random.randint(19, 40)
    subs = squad - 11
    povrs = []
    ppositions = []
    pfirstnames = []
    psurnames = []
    pnationalities = []
    pbirthyears = []
    pclubs = []
    pclubcountries = []
    pclubleagues = []
    pcontracts = []
    curryear = int(time.strftime("%Y"))
    formation = random.choice(["4-4-2", "4-4-2 diamond", "3-5-2", "4-3-3", "4-3-3 ATT", "4-3-3 DEF"])
    if formation == "4-4-2":
        positions = ["GK", "RB", "CB", "CB", "LB", "RM", "CM", "CM", "LM", "ST", "ST"]
    elif formation == "4-4-2 diamond":
        positions = ["GK", "RB", "CB", "CB", "LB", "CDM", "CM", "CM", "CAM", "ST", "ST"]
    elif formation == "3-5-2":
        positions = ["GK", "RB", "CB", "LB", "RM", "CM", "CM", "CM", "LM", "ST", "ST"]
    elif formation == "4-3-3":
        positions = ["GK", "RB", "CB", "CB", "LB", "RM", "CM", "LM", "RW", "ST", "LW"]
    elif formation == "4-3-3 ATT":
        positions = ["GK", "RB", "CB", "CB", "LB", "CM", "CM", "CAM", "RW", "ST", "LW"]
    elif formation == "4-3-3 DEF":
        positions = ["GK", "RB", "CB", "CB", "LB", "CDM", "CM", "CM", "RW", "ST", "LW"]
    print("Formation: " + formation)
    print("STARTING LINEUP")
    for pos in positions:
        allc = random.randint(0, 2)
        if allc == 1:
            country = random.choice(allcountries)
        elif allc == 2:
            country = teamcountry
        else:
            country = random.choice(countries)
        eng = random.choice(["en_AU", "en_CA", "en_GB", "en_NZ", "en_US"])
        if country == "Heigery":
            locale = "de_DE"
        elif country == "Raceny":
            locale = random.choice([eng, eng, "fi_FI"])
        elif country == "Zilk" or country == "UIA":
            locale = eng
        elif country == "Milestan" or country == "El Furt" or country == "Las Sange" or country == "La Miewa" or country == "Los Tarmes":
            locale = random.choice(["es_ES", "es_MX"])
        elif country == "Beanthe" or country == "Lily Island":
            locale = "fr_FR"
        elif country == "Fushaly":
            locale = "it_IT"
        elif country == "Berter":
            locale = "sv_SE"
        elif country == "Fjørk Islands":
            locale = "no_NO"
        elif country == "La La Islands":
            locale = "fi_FI"
        else:
            locale = random.choice(langs)
        gen = faker.Faker(locale)
        firstname = gen.first_name_male()
        surname = gen.last_name_male()
        name = firstname + " " + surname
        birthyear = gen.date_of_birth(minimum_age=19, maximum_age=random.randint(30, 42)).year
        age = curryear - birthyear
        ovr = random.randint(teamovr - var, teamovr + var)
        if ovr > 99:
            ovr = 99
        elif ovr < 1:
            ovr = 1
        if age >= 35:
            contractlength = random.randint(0, 2)
        elif age > 31 and age < 35:
            contractlength = random.randint(0, 3)
        else:
            contractlength = random.randint(0, 5)
        contractuntil = curryear + contractlength
        print("OVR " + str(ovr) + " " + pos + " " + name + ", " + country + ", born " + str(birthyear) + " (age " + str(age) + "), contract until " + str(contractuntil))
        povrs.append(ovr)
        ppositions.append(pos)
        pfirstnames.append(firstname)
        psurnames.append(surname)
        pnationalities.append(country)
        pbirthyears.append(birthyear)
        pcontracts.append(contractuntil)
        exec(pos + " += 1")
    print("SUBSTITUTES & REVERSES")
    for i in range(subs):
        if GK < 2:
            pos = "GK"
        else:
            pos = random.choice(allpos_)
        allc = random.randint(0, 2)
        if allc == 1:
            country = random.choice(allcountries)
        elif allc == 2:
            country = teamcountry
        else:
            country = random.choice(countries)
        eng = random.choice(["en_AU", "en_CA", "en_GB", "en_NZ", "en_US"])
        if country == "Heigery":
            locale = "de_DE"
        elif country == "Raceny":
            locale = random.choice([eng, eng, "fi_FI"])
        elif country == "Zilk" or country == "UIA":
            locale = eng
        elif country == "Milestan" or country == "El Furt" or country == "Las Sange" or country == "La Miewa" or country == "Los Tarmes":
            locale = random.choice(["es_ES", "es_MX"])
        elif country == "Beanthe" or country == "Lily Island":
            locale = "fr_FR"
        elif country == "Fushaly":
            locale = "it_IT"
        elif country == "Berter":
            locale = "sv_SE"
        elif country == "Fjørk Islands":
            locale = "no_NO"
        elif country == "La La Islands":
            locale = "fi_FI"
        else:
            locale = random.choice(langs)
        gen = faker.Faker(locale)
        firstname = gen.first_name_male()
        surname = gen.last_name_male()
        name = firstname + " " + surname
        subovr = random.randint(0, 20)
        birthyear = gen.date_of_birth(minimum_age=16, maximum_age=random.randint(30, 42)).year
        age = curryear - birthyear
        youthovr = random.randint(10, 25)
        if age > 18:
            ovr = random.randint(teamovr - subovr - var, teamovr - subovr + var)
        else:
            ovr = random.randint(teamovr - youthovr - var, teamovr - youthovr + var)
        if ovr > 99:
            ovr = 99
        elif ovr < 1:
            ovr = 1
        if age >= 35:
            contractlength = random.randint(0, 2)
        elif age > 31 and age < 35:
            contractlength = random.randint(0, 3)
        else:
            contractlength = random.randint(0, 5)
        contractuntil = curryear + contractlength
        print("OVR " + str(ovr) + " " + pos + " " + name + ", " + country + ", born " + str(birthyear) + " (age " + str(age) + "), contract until " + str(contractuntil))
        povrs.append(ovr)
        ppositions.append(pos)
        pfirstnames.append(firstname)
        psurnames.append(surname)
        pnationalities.append(country)
        pbirthyears.append(birthyear)
        pcontracts.append(contractuntil)
        exec(pos + " += 1")
    defenders = RB + CB + LB
    midfielders = RM + CM + LM + CDM + CAM
    forwards = ST + RW + LW
    for pos in allpos:
        exec('print("' + pos + ': " + ' + 'str(' + pos + '))')
    print("")
    print("Goalkeepers: " + str(GK))
    print("Defenders: " + str(defenders))
    print("Midfielders: " + str(midfielders))
    print("Forwards: " + str(forwards))
    print("")
    print("Players: " + str(squad))
    print("")
    writetoexcel = input("Write to Excel file (y for yes)? ")
    if writetoexcel == "y":
        teamname = input("Club name: ")
        teamleague = input("Club league in " + teamcountry + ": ")
        for player in range(squad):
            pclubs.append(teamname)
            pclubcountries.append(teamcountry)
            pclubleagues.append(teamleague)
        excelname = "players.xlsx"
        excel = openpyxl.load_workbook(excelname)
        backup = "players_backup.xlsx"
        print("Saving backup to " + backup + "...")
        excel.save(backup)
        ws = excel.active
        print("Writing to " + excelname + "...")
        row = ws.max_row + 1
        for player in range(squad):
            ws.cell(row=row, column=1, value=pfirstnames[player])
            ws.cell(row=row, column=2, value=psurnames[player])
            ws.cell(row=row, column=3, value=pnationalities[player])
            ws.cell(row=row, column=4, value=ppositions[player])
            ws.cell(row=row, column=5, value=povrs[player])
            ws.cell(row=row, column=6, value=pbirthyears[player])
            ws.cell(row=row, column=7, value=pclubs[player])
            ws.cell(row=row, column=8, value=pclubcountries[player])
            ws.cell(row=row, column=9, value=pclubleagues[player])
            ws.cell(row=row, column=10, value=pcontracts[player])
            row += 1
        excel.save(excelname)
        print("Squad saved to " + excelname + ".")
        print("")
