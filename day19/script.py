from collections import defaultdict
import re

lines = []
messages = []


def read_file():
    file = open("input.txt", "r")
    [lines.append(line.strip()) for line in file]
    file.close()


def parse_lines_get_dict():
    rule_dict = {}
    is_rule = True
    for line in lines:
        is_rule &= bool(line)
        if is_rule:
            rule_list = re.split(r": | \| ", line)
            rule_dict[rule_list[0]] = [rule.strip('"') for rule in rule_list[1:]]
        elif line:
            messages.append(line)
    return rule_dict


def get_rev_dict(rule_dict):
    for key, val in rule_dict.items():
        for i, rule in enumerate(val):
            if ' ' not in rule and rule.isnumeric():  # unit rule
                rule_dict[key][i] = rule_dict[rule]

    for key, val in rule_dict.items():  # all just to flatten substitutions...
        revised = []
        for sublist in val:
            if isinstance(sublist, list):
                for elem in sublist:
                    revised.append(elem)
            else:
                revised.append(sublist)
        rule_dict[key] = revised

    rev_dict = defaultdict(list)
    for key, val in rule_dict.items():
        for rule in val:
            rev_dict[rule].append(key)
    return rev_dict


def cyk_algorithm(message, rev_dict):
    n = len(message)
    backing_array = [[set() for j in range(n - i)] for i in range(n)]
    for i in range(n):
        backing_array[0][i].update(rev_dict[message[i]])

    for i in range(1, n):
        for j in range(n - i):
            for k in range(i):
                for rule_1 in backing_array[k][j]:
                    for rule_2 in backing_array[i - k - 1][j + k + 1]:
                        combo = f"{rule_1} {rule_2}"
                        if rev_dict.get(combo):
                            backing_array[i][j].update(rev_dict[combo])

    return '0' in backing_array[n - 1][0]


def main():
    read_file()

    rule_dict = parse_lines_get_dict()
    rev_dict_1 = get_rev_dict(rule_dict)

    message_valid = [cyk_algorithm(message, rev_dict_1) for message in messages]
    print(f"There are {message_valid.count(True)} valid messages.")

    # filthy hack
    rule_dict['8'] = ['42', '42 8']
    rule_dict['11'] = ['42 31', '42 no']
    rule_dict['no'] = ['11 31']

    rev_dict_2 = get_rev_dict(rule_dict)
    message_valid_2 = [cyk_algorithm(message, rev_dict_2) for message in messages]
    print(f"There are {message_valid_2.count(True)} valid messages in part 2.")


if __name__ == "__main__":
    main()
