import re


rule_dict = {}
my_ticket = []
nearby_tickets = []
valid_tickets = []


def read_file():
    file = open("input.txt", "r")
    lines = [line.strip() for line in file]

    i = 0
    while lines[i]:
        name, low1, high1, low2, high2 = re.split(": |-| or ", lines[i])
        rule_dict[name] = ((int(low1), int(high1)), (int(low2), int(high2)))
        i += 1

    my_ticket.extend([int(x) for x in re.findall('\d+', lines[i + 2])])

    for line in lines[i + 5:]:
        nearby_tickets.append([int(x) for x in re.findall('\d+', line)])

    file.close()


def num_in_rule(num, rule):
    return (rule[0][0] <= num <= rule[0][1]) or (rule[1][0] <= num <= rule[1][1])


def find_errors_and_valid_tickets():
    to_return = 0
    for ticket in nearby_tickets:
        ticket_valid = True
        for num in ticket:
            num_valid = any([num_in_rule(num, rule) for rule in rule_dict.values()])
            to_return += num if not num_valid else 0
            ticket_valid = ticket_valid and num_valid
        valid_tickets.append(ticket) if ticket_valid else None

    return to_return


def match_fields():  # If multiple solutions may exist
    valid_rules_list = []
    for i in range(len(valid_tickets[0])):
        field = [ticket[i] for ticket in valid_tickets]
        valid_rules_list.append([i, set([rule for rule in rule_dict.keys() if all([num_in_rule(num, rule_dict[rule]) for num in field])])])
    valid_rules_list.sort(key=lambda x: len(x[1]))
    mappings = [[[option], [valid_rules_list[0][0]], {option}] for option in valid_rules_list[0][1]]
    curr_mapping = mappings.pop()
    while curr_mapping:
        if len(curr_mapping[0]) == len(valid_rules_list):
            break
        next_index = curr_mapping[1] + [valid_rules_list[len(curr_mapping[0])][0]]
        next_set_of_options = valid_rules_list[len(curr_mapping[0])][1].difference(curr_mapping[2])
        for i in next_set_of_options:
            new_rules = curr_mapping[0] + [i]
            new_rules_set = set(new_rules)
            mappings.append([new_rules, next_index, new_rules_set])
        curr_mapping = mappings.pop()

    return [x for y, x in sorted(zip(curr_mapping[1], curr_mapping[0]))]


def match_fields_unambiguous():  # If there's only one possible match
    valid_rules_list = []
    for i in range(len(valid_tickets[0])):
        field = [ticket[i] for ticket in valid_tickets]
        valid_rules_list.append([i, set([rule for rule in rule_dict.keys() if all([num_in_rule(num, rule_dict[rule]) for num in field])])])
    valid_rules_list.sort(key=lambda x: len(x[1]))

    mapping = []
    prev_set = set()
    for i in range(len(valid_rules_list)):
        mapping.append([valid_rules_list[i][0], valid_rules_list[i][1].difference(prev_set).pop()])
        prev_set = valid_rules_list[i][1]

    return [y for x, y in sorted(mapping)]


def multiply_fields():
    mapping = match_fields_unambiguous()
    to_return = 1
    for i, field in enumerate(mapping):
        if field[:9] == 'departure':
            to_return *= my_ticket[i]
    return to_return


def main():
    read_file()
    error_rate = find_errors_and_valid_tickets()
    field_product = multiply_fields()

    print(f"The error rate is {error_rate}")
    print(f"The product of the departure fields is {field_product}")


if __name__ == "__main__":
    main()
