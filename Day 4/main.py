def check_record(record_string):
    '''
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
    '''
    passport_criteria = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
    for category in passport_criteria:
        if category in record_string:
            pass
        else:
            return False
    return True
  
    




if __name__ == "__main__":
    filename = "Day 4\\input.txt"
    lines = list(open(filename, 'r'))
    all_records = []
    curr_record = ""
    for line in lines:
        if line == "\n":
            all_records.append(curr_record)
            curr_record = ""
            continue
        curr_record += line
    print(len(all_records))
        
    acc = 0
    for record in all_records:
        # using list comprehension 
        listToStr = ''.join(map(str, record)).replace("\n", " ")
        record = listToStr
        # print(listToStr)  
        output = check_record(record)
        if output == True:
            acc += 1
            print(record)
        else:
            pass
        print(record)

    print(acc)
