if __name__ == "__main__":
    good_pass_count = 0
    f = open("inputs.txt", "r")
    for line in f:
        instruction = line.split(":")[0]
        instruct_count = instruction.split(" ")[0]
        instruct_count_min = instruct_count.split("-")[0]
        instruct_count_max = instruct_count.split("-")[1]
        instruct_letter = instruction.split(" ")[1]
        password = line.split(":")[1]
        password = password[0:-1].strip(" ")
        if not (password[int(instruct_count_min)-1] == instruct_letter and password[int(instruct_count_max)-1] == instruct_letter):
            if password[int(instruct_count_min)-1] == instruct_letter or password[int(instruct_count_max)-1] == instruct_letter:
                print(line)
                good_pass_count += 1
    print(good_pass_count)