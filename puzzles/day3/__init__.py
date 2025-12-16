def compute_total_joltage(banks: list[str], nof_batteries) -> int:
    total_joltage = 0
    for bank in banks:
        joltage = find_joltage(bank, nof_batteries)
        total_joltage += joltage

    return total_joltage


def find_joltage(bank: str, nof_batteries: int) -> int:
    def find_max_battery_index(
        bank: str, index_start: int, batteries_left_to_find: int
    ):
        sub_bank = bank[index_start:]
        max_index = index_start
        max = 9

        for i in range(max, 0, -1):
            max_index = sub_bank.find(str(i))
            if max_index != -1:
                # Make sure that it is the max that's returned given the fact that nof_batteries has to be fulfilled
                if len(sub_bank[max_index:]) < batteries_left_to_find:
                    max = max - 1
                else:
                    break

        return (
            max_index + index_start
        )  # Make sure the index relatively to the original bank is returned

    index = 0
    joltage = ""
    for i in range(nof_batteries):
        battery_index = find_max_battery_index(bank, index, nof_batteries - i)
        index = (
            battery_index + 1
        )  # We don't want to include the battery_index found in the next iteration
        joltage += bank[battery_index]

    return int(joltage)
