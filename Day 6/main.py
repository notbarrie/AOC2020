if __name__ == "__main__":
    filename = "Day 6/input.txt"
    lines = open(filename, 'r').readlines()
    # print(len(lines))
    characters_seen = set()
    total = 0
    for line in lines:
        if line == "\n":
            # add set count to cum_total
            total += len(characters_seen)
            # clear set
            characters_seen = set()
            continue

        line = line.replace("\n", "")
        for character in line:
            if character not in characters_seen:
                characters_seen.add(character)
    total += len(characters_seen)
    print(total)
        
    
            
    