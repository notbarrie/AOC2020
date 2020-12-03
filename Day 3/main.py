if __name__ == "__main__":
    filename = "Day 3\\input.txt"
    lines = list(open(filename, 'r'))
    start_row = 0
    start_column = 0
    horizontal_speed = 3
    vertical_speed = 1
    current_position = [start_row, start_column]
    
    # loop the rows in lines
    acc = 0
    for row in lines:
        row = row.strip("\n")
        print(current_position)
        ypos = current_position[0]
        length =  len(row)
        xpos = current_position[1] 
        if current_position[1]>length-1 :
            xpos = current_position[1]%length

        try:
            current_character = lines[ypos][xpos]
            print(current_character)
            pass
        except IndexError as e:
            print("fuck")
        if current_character == "#":
            acc+=1
        current_position = [ypos + vertical_speed, xpos+horizontal_speed]
    print(acc)