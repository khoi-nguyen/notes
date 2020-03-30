from math import floor, ceil

def mean(number_list, frequencies = False):
    if frequencies:
        # KHOI TODO (Calculate variable question)
        running_total = 0
        for i in range(0, len(number_list)):
            running_total += number_list[i] * frequencies[i]
        answer = running_total / sum(frequencies)
    else:
        question = ", ".join([str(n) for n in number_list])
        answer = sum(number_list) / len(number_list)
    return (question, str(answer))

def median(number_list):
    question = ", ".join([str(n) for n in number_list])
    pos = (len(number_list) + 1)/2 - 1
    number_list.sort()
    answer = mean([number_list[floor(pos)], number_list[ceil(pos)]])[1]
    return (question, answer)
