def mean(number_list, frequencies = False):
    if frequencies:
        running_total = 0
        for i in range(0, len(number_list)):
            running_total += number_list[i] * frequencies[i]
        return running_total / sum(frequencies)
    else:
        return sum(number_list) / len(number_list)
