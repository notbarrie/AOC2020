def test_slope(current_position, horizontal_speed, vertical_speed):
    # loop the rows in lines
    acc = 0
    for i, row in enumerate(lines):
        if vertical_speed> 1 and i%vertical_speed != 0:
            continue
        
        row = row.strip("\n")
        ypos = current_position[0]
        length =  len(row)
        xpos = current_position[1] 

        if current_position[1]>length-1 :
            xpos = current_position[1]%length

        try:
            current_character = lines[ypos][xpos]
        except IndexError as e:
            print(e)
        if current_character == "#":
            acc+=1
        current_position = [ypos + vertical_speed, xpos+horizontal_speed]
    return acc

if __name__ == "__main__":
    filename = "Day 3\\input.txt"
    lines = list(open(filename, 'r'))
    start_row = 0
    start_column = 0
    horizontal_speed = 1
    vertical_speed = 1
    current_position = [start_row, start_column]
    test_one = test_slope(current_position, horizontal_speed, vertical_speed)
    horizontal_speed = 3
    vertical_speed = 1
    test_two = test_slope(current_position, horizontal_speed, vertical_speed)
    horizontal_speed = 5
    vertical_speed = 1
    test_three = test_slope(current_position, horizontal_speed, vertical_speed)
    horizontal_speed = 7
    vertical_speed = 1
    test_four = test_slope(current_position, horizontal_speed, vertical_speed)
    horizontal_speed = 1
    vertical_speed = 2
    test_five = test_slope(current_position, horizontal_speed, vertical_speed)
    print(str(int(test_five)*int(test_four)*int(test_three)*int(test_two)*int(test_one)))