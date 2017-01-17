from datetime import datetime

csv_file = open("testing_postable.csv", "w")
csv_file.close

def kid_bday_date_conversion(date):

    try:
        if "," in date:
            date = date[:-6]
        return datetime.strptime(date, "%B %d").date()
    except (ValueError):
        return "Invalid Format"


def create_bday_dict(file):

    with open(file) as xls_file:
        data = xls_file.readlines()

    bday_dict = {}

    for line in data:
        line = line.rstrip()
        words = line.split('\t')
        words = words[1:-2]
        del words[7:18]
        if len(words) < 14:
            continue
        del words[5]
        del words [3]
        del words[1]

        if words[7] == "Birthday":
            continue

        try:

            name = words[0].rstrip() + ' ' + words[1].rstrip()
            for i, word in enumerate(words):
                if "@" in word:
                    index = i + 1
                    bday = words[index]

                    if bday:
                        if type(bday) == str:
                            bday = datetime.strptime(bday, "%B %d").date()
                        bday_dict[name] = bday

                
                    p_name = words[2].rstrip() + ' ' + words[3].rstrip()
                    p_bday = words[index + 1]

                    if p_bday and p_name != ' ':
                        p_bday = datetime.strptime(p_bday, "%B %d").date()
                        bday_dict[p_name] = p_bday

                    kid1 = words[index + 2]
                    kid1_bday = words[index + 3]
                    if kid1 and kid1_bday:
                        kid1_bday = kid_bday_date_conversion(kid1_bday)
                        if kid1_bday == "Invalid Format":
                            continue
                        bday_dict[kid1] = kid1_bday
            else:
                continue

            kid2 = words[index + 4]
            kid2_bday = words[index + 5]
            if kid2 and kid2_bday:
                kid2_bday = kid_bday_date_conversion(kid2_bday)
                if kid2_bday == "Invalid Format":
                    continue
                bday_dict[kid2] = kid2_bday
            else:
                continue

            kid3 = words[index + 6]
            kid3_bday = words[index + 7]
            if kid3 and kid3_bday:
                kid3_bday = kid_bday_date_conversion(kid3_bday)
                if kid3_bday == "Invalid Format":
                    continue
                bday_dict[kid3] = kid3_bday
            else:
                continue

        except (IndexError):
            pass

    bday_dict["Sandy Riemer"] = datetime(1900, 7, 19).date()
    bday_dict["Anna & Ray <3"] = datetime(1900, 8, 6).date()
    bday_dict["Chuck & Ariella <3"] = datetime(1900, 6, 4).date()
    bday_dict["Ashley & Nick Popio <3"] = datetime(1900, 8, 2).date()
    bday_dict["Ben B & Catherine C <3"] = datetime(1900, 11, 1).date()
    bday_dict["Christine & Andrew <3"] = datetime(1900, 11, 9).date()
    bday_dict["Rick & Diane <3"] = datetime(1900, 6, 6).date()
    bday_dict["Ellie & Mick <3"] = datetime(1900, 5, 29).date()
    bday_dict["Emily M & Paul <3"] = datetime(1900, 11, 10).date()
    bday_dict["Emily G & Art <3"] = datetime(1900, 6, 29).date()
    bday_dict["Erik & Erica <3"] = datetime(1900, 5, 23).date()
    bday_dict["Katy & Jeff <3"] = datetime(1900, 8, 29).date()
    bday_dict["Luke & Jenn <3"] = datetime(1900, 6, 9).date()
    bday_dict["Brian & Maria <3"] = datetime(1900, 7, 5).date()
    bday_dict["Matt & Laura <3"] = datetime(1900, 4, 16).date()
    bday_dict["Nick & Chloe <3"] = datetime(1900, 6, 22).date()
    bday_dict["Steve & Sherri <3"] = datetime(1900, 8, 8).date()
    bday_dict["Sue & Ira <3"] = datetime(1900, 8, 6).date()
    bday_dict["Mom's Special Day"] = datetime(1900, 8, 4).date()
    bday_dict["Tim & Darya <3"] = datetime(1900, 4, 1).date()
    bday_dict["Paul & Christina <3"] = datetime(1900, 12, 31).date()

    for k in sorted(bday_dict, key=bday_dict.get):
        print k, bday_dict[k]

create_bday_dict("testing_postable.xls")


    # for line in xls_file:
    #     line = line.split('\t', 1)
    #     print line