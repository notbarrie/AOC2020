if __name__ == "__main__":
    filename = "input.txt"
    lines = list(open(filename, 'r'))
    outputs = []
    for line in lines:
        one_input = line
        rows = list(range(0, 128))
        columns = list(range(0, 8))
        for i, instruction in enumerate(one_input):
            if "F" in instruction:
                '''
                F means to take the lower half, keeping rows 0 through 63.
                '''
                new_rows = int((len(rows))/2)
                rows = rows[:new_rows] 
            if "B" in instruction:
                new_rows = int((len(rows))/2)
                rows = rows[new_rows:] 
            if "R" in instruction:
                new_cols = int((len(columns))/2)
                columns = columns[new_cols:]
            if "L" in instruction:
                new_cols = int((len(columns))/2)
                columns = columns[:new_cols] 
            '''
            Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

            '''
        output = (rows[0]*8) + columns[0]
        outputs.append(output)

    outputs.sort()
    for i, seat_id in enumerate(outputs):
        if seat_id + 1 in outputs:
            continue
        else:
            print(seat_id+1)
    # print(max(outputs))