csv_file = open("testing_postable.csv", "w")
csv_file.close

with open("testing_postable.xls") as xls_file:
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

    try:
        name = words[0] + ' ' + words[1]
        if words[8] == "Birthday":
            continue

        print name, words
        
        p_name = words[2] + ' ' + words[3]
        # p_bday = words[23]

    except (IndexError):
        pass

    # if bday:
    #     bday_dict[bday] = name
    # if p_bday != '':
    #     bday_dict[p_bday] = p_name

# for k, v in sorted(bday_dict.items()):
#     print k, v


    # for line in xls_file:
    #     line = line.split('\t', 1)
    #     print line