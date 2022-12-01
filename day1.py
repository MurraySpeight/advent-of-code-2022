def elves_list():
    with open('day1.txt', 'r') as f:
        elves = []
        calories = 0
        for line in f:
            if line.strip().isdigit():
                calories += int(line)
            else:
                elves.append(calories)
                calories = 0
        elves.append(calories)
        return elves


def main():
    elves = elves_list()
    max_value = max(elves)
    print("Most calories carried by a single elf is " + str(max_value))
    total_elves = len(elves)
    total_cals = 0
    top_elf_amount = 3
    while len(elves) > total_elves - top_elf_amount:
        total_cals += max(elves)
        elves.remove((max(elves)))
    print(f"Total of {total_cals} calories for the top {top_elf_amount} elves")


if __name__ == '__main__':
    main()
