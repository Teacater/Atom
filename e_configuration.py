from typing import Tuple, List

levels = ["", "s", "p", "d", "f", "g", "h", "i"]


def get_cap(l: int) -> int:
    """
    calculates max number of electrons on layer
    :param l: layer
    :return: number of electrons
    """
    return ((l - 1) * 2 + 1) * 2


def get_index(n: str) -> str:
    """
        converts integer string to index string

        :param n: integer number in string format
        :return: integer index in string format
        """
    var = list(n)
    powers = "₀₁₂₃₄₅₆₇₈₉"
    result = ""
    for i in var:
        if i == ".":
            result += ","
        else:
            result += powers[int(i)]
    return result


def get_power(n: str) -> str:
    """
    converts integer string to power string

    :param n: integer number in string format
    :return: integer power in string format
    """
    var = list(n)
    powers = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    result = ""
    for i in var:
        result += powers[int(i)]
    return result


def print_e_configuration(conf: List[Tuple[int, int]], last: int):
    """
    prints electron configuration in console
    :param conf: Electron configuration as list of n, l quantum numbers
    :param last: Number of electrons at last layer
    """
    print("Электронная конфигурация")
    for i in range(len(conf)):
        n, l = conf[i]
        if i == len(conf) - 1:
            max_cap = str(last)
        else:
            max_cap = str(get_cap(l))
        print(str(n) + levels[l] + get_power(max_cap), end="")
    print("")


def get_electron_configuration(electron_number: int) -> Tuple[int, List[Tuple[int, int]]]:
    """
    calculates electron configuration
    :param electron_number: electron number in atom
    :return: Number of electrons at last layer, Electron configuration as list of n, l quantum numbers
    """
    electron_remains = electron_number
    current_cap = 2
    current_n = 1
    current_l = 1
    configuration = [(current_n, current_l)]
    start = 1
    while electron_remains > current_cap:
        electron_remains -= current_cap
        current_n += 1
        current_l -= 1
        if current_l < 1 or current_n < 1:
            current_n = 1
            start += 1
            current_l = start
            while current_l > current_n:
                current_n += 1
                current_l -= 1

        configuration.append((current_n, current_l))
        current_cap = get_cap(current_l)

    return electron_remains, configuration
