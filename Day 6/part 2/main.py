if __name__ == "__main__":
    filename = "Day 6/input.txt"
    lines = open(filename, 'r').readlines()
    # print(len(lines))
    characters_seen = set()
    group = set()
    total = 0
    for line in lines:
        if line == "\n":
            # add set count to cum_total
            big_string = "".join(group)
            for char in characters_seen:
                # if char occurrs in big string len(group) times, add one to total
                if big_string.count(char) == len(group):
                    total += 1
            # clear set
            characters_seen = set()
            group = set()

            continue

        line = line.replace("\n", "")
        group.add(line)
        for character in line:
            if character not in characters_seen:
                characters_seen.add(character)
    # total += 1
    print(total)
        
    
            
    