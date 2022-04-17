levels = ["", "s", "p", "d", "f", "g", "h", "i"]


def get_cap(l):
    return ((l - 1) * 2 + 1) * 2


def get_index(n):
    var = list(n)
    powers = "₀₁₂₃₄₅₆₇₈₉"
    result = ""
    for i in var:
        if i == ".":
            result += ","
        else:
            result += powers[int(i)]
    return result


def get_power(n):
    var = list(n)
    powers = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    result = ""
    for i in var:
        result += powers[int(i)]
    return result


def print_e_configuration(conf, last):
    print("Электронная конфигурация")
    for i in range(len(conf)):
        n, l = conf[i]
        if i == len(conf) - 1:
            max_cap = str(last)
        else:
            max_cap = str(get_cap(l))
        print(str(n) + levels[l] + get_power(max_cap), end="")
    print("")


def get_electron_configuration(n):
    s = n
    current_cap = 2
    current_n = 1
    current_l = 1
    conf = [(current_n, current_l)]
    start = 1
    while s > current_cap:
        s -= current_cap
        current_n += 1
        current_l -= 1
        if current_l < 1 or current_n < 1:
            current_n = 1
            start += 1
            current_l = start
            while current_l > current_n:
                current_n += 1
                current_l -= 1

        conf.append((current_n, current_l))
        current_cap = get_cap(current_l)

    return current_cap, s, conf