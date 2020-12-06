import re
def validate_fields(fields):
    '''
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    '''
    for field in fields:
        field_name, value = field.split(":")
        if "eyr" in field_name:
            if 2020 > int(value) or int(value)>2030:
                return False
            continue
        if "hgt" in field_name:
            unit = value[-2:]
            height_value = value[:-2]
            if "in" in unit:
                if 59>int(height_value) or int(height_value)>76:
                    return False 
                continue
                
            if "cm" in unit:
                if 150>int(height_value) or int(height_value)>193:
                    return False 
                continue
                
        if "byr" in field_name:
            if 1920 >int(value) or int(value)>2002:
                return False
            continue
            
        if "iyr" in field_name:
            if 2010 >int(value) or int(value) >2020:
                return False
            continue
            
        if "hcl" in field_name:
            if not re.match(r'^#(?:[0-9a-f]{3}){1,2}$', value):
                return False
            continue
        if "ecl" in field_name:
            options = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if value not in options:
                return False
            continue
            
        if "pid" in field_name:
            if len(value) != 9 or not value.isdigit():
                return False
            continue
        
        if "cid" in field_name:
            continue

    return True
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



        # if output == True:
        #     acc += 1
        #     print(record)
        # else:
        #     pass
        # print(record)
        if output == True:
            # now need to validate each field
            fields = record.split(" ")
            fields.pop(-1)
            fields_validated = validate_fields(fields)
            if fields_validated:
                acc +=1
                # print(fields)
            else:
                print(fields)

    print(acc)
