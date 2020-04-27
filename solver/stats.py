from math import floor, ceil
import statistics

midval = lambda x: sum(x) / len(x) if isinstance(x, list) else x
display_val = lambda x: f"{x[0]}-{x[1]}" if isinstance(x, list) else x
columns = {
    "values": [
        "Values",
        lambda data, row: display_val(data[row][0]),
        lambda data: "Total",
    ],
    "frequencies": [
        "Frequencies",
        lambda data, row: data[row][1],
        lambda data: sum([f for (v, f) in data]),
    ],
    "average": [
        "$v \\times f$",
        lambda data, row: midval(data[row][0]) * data[row][1],
        lambda data: sum([midval(v) * f for (v, f) in data]),
    ],
    "cumulated": [
        "Cumulated Frequency",
        lambda data, row: sum([f for (v, f) in data[: row + 1]]),
        lambda data: "",
    ],
}


def frequencytable(data, show_cols=[]):
    global columns
    cols = {key: columns[key] for key in ["values", "frequencies"] + show_cols}
    nrows, ncols = len(data), len(cols)
    lines = [f'\\begin{{tabular}}{{{" | ".join(ncols * ["c"])}}}']
    lines.append("\\toprule")
    lines.append(f'{" & ".join([v[0] for (t, v) in cols.items()])}\\\\')
    lines.append("\\midrule")
    for row in range(0, nrows):
        col_values = [str(v[1](data, row)) for (t, v) in cols.items()]
        lines.append(f'{" & ".join(col_values)}\\\\')
    lines.append("\\midrule")
    lines.append(f'{" & ".join([str(v[2](data)) for (t, v) in cols.items()])}\\\\')
    lines.append("\\bottomrule")
    lines.append("\\end{tabular}")
    return "\n".join(lines)


def mean(number_list):
    question = ", ".join([str(n) for n in number_list])
    answer = statistics.mean(number_list)
    return (question, answer)


def median(number_list):
    question = ", ".join([str(n) for n in number_list])
    answer = statistics.median(number_list)
    return (question, answer)


def mode(number_list):
    question = ", ".join([str(n) for n in number_list])
    answer = statistics.multimode(number_list)
    return (question, answer)


def rnge(number_list):
    question = ", ".join([str(n) for n in number_list])
    answer = max(number_list) - min(number_list)
    return (question, answer)
