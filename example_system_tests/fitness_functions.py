from cmath import log10

from AST.MiniLangInterpreter import MiniLangInterpreter


def calculate_numeric_similarity(actual, target):
    """
    Oblicza podobieństwo między dwiema liczbami.
    Zwraca wartość w przedziale [0, 1], gdzie 1 oznacza identyczne liczby.
    """
    if actual == target:
        return 1.0

    actual = abs(actual)
    target = abs(target)

    if max(actual, target) > 1000:
        similarity = 1.0 / (1.0 + abs(log10(actual + 1) - log10(target + 1)))
    else:
        max_diff = max(target * 2, 100)
        diff = abs(actual - target)
        similarity = max(0, 1.0 - (diff / max_diff))

    return similarity


def evaluate_output_position(output, target, desired_position=None):
    """
    Ocenia występowanie liczby target w output z uwzględnieniem pozycji.
    Jeśli desired_position jest podane, sprawdza, czy wartość na tej pozycji
    jest równa target. Zwraca:
      - 1.0, jeśli wartość na desired_position jest równa target,
      - 0.5, jeśli target występuje gdzie indziej w output,
      - lub wagę podobieństwa, gdy nie ma targetu.
    """
    if not output:
        return 0.0

    if desired_position is not None and desired_position < len(output) and output[desired_position] == target:
        return 1.0

    if target in output:
        return 0.5

    if desired_position is not None and desired_position < len(output):
        similarity = calculate_numeric_similarity(output[desired_position], target)
        return similarity * 0.5

    return 0.0


def evaluate_output_length(output, desired_length=1):
    """
    Ocenia długość wyjścia.
    """
    if not output:
        return 0.0
    if len(output) == desired_length:
        return 1.0
    return max(0, 1.0 - abs(len(output) - desired_length) * 0.2)


def fitness_1_1_A(program):
    """
    Program powinien wygenerować na wyjściu (na dowolnej pozycji) liczbę 1.
    Inne liczby są dozwolone.
    """
    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)
    interpreter.execute_program(program)
    output = interpreter.output_buffer

    if any(value == 1 for value in output):
        return 1.0
    elif output:
        return max(calculate_numeric_similarity(x, 1) for x in output)
    else:
        return 0.0


def fitness_1_1_B(program):
    """
    Program powinien wygenerować na wyjściu (na dowolnej pozycji) liczbę 789.
    Inne liczby są dozwolone.
    """
    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)
    interpreter.execute_program(program)
    output = interpreter.output_buffer

    if any(value == 789 for value in output):
        return 1.0
    elif output:
        return max(calculate_numeric_similarity(x, 789) for x in output)
    else:
        return 0.0


def fitness_1_1_C(program):
    """
    Program powinien wygenerować na wyjściu (na dowolnej pozycji) liczbę 31415.
    Inne liczby są dozwolone.
    """
    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)
    interpreter.execute_program(program)
    output = interpreter.output_buffer

    if any(value == 31415 for value in output):
        return 1.0
    elif output:
        return max(calculate_numeric_similarity(x, 31415) for x in output)
    else:
        return 0.0


def fitness_1_1_D(program):
    """
    Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 1.
    Inne liczby mogą się pojawić.
    """
    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)
    interpreter.execute_program(program)
    output = interpreter.output_buffer

    position_score = evaluate_output_position(output, 1, desired_position=0)
    range_score = 0.0
    if output:
        range_score = max(calculate_numeric_similarity(x, 1) for x in output)
    return 0.8 * position_score + 0.2 * range_score


def fitness_1_1_E(program):
    """
    Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 789.
    Inne liczby mogą się pojawić.
    """
    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)
    interpreter.execute_program(program)
    output = interpreter.output_buffer

    position_score = evaluate_output_position(output, 789, desired_position=0)

    range_score = 0.0
    if output:
        range_score = max(calculate_numeric_similarity(x, 789) for x in output)

    return 0.8 * position_score + 0.2 * range_score


def fitness_1_1_F(program):
    """
    Program powinien wygenerować na wyjściu liczbę jako jedyną liczbę 1.
    Nie powinien generować nic poza tą liczbą.
    """
    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)
    interpreter.execute_program(program)
    output = interpreter.output_buffer

    value_score = 0.0
    if output:
        value_score = calculate_numeric_similarity(output[0], 1)
    length_score = evaluate_output_length(output, 1)
    return 0.7 * value_score + 0.3 * length_score


def fitness_1_2_A(program):
    """
    Zadanie 1.2.A:
    Program powinien odczytać dwie pierwsze liczby z wejścia i zwrócić na wyjściu (jedynie) ich sumę.
    Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [0,9].
    """
    test_data = {
        "inputs":
            [{"var_0": 9, "var_1": 9}, {"var_0": 9, "var_1": 2}, {"var_0": 2, "var_1": 8}, {"var_0": 9, "var_1": 7},
             {"var_0": 1, "var_1": 2}, {"var_0": 3, "var_1": 0}, {"var_0": 1, "var_1": 2}, {"var_0": 1, "var_1": 6},
             {"var_0": 8, "var_1": 9}, {"var_0": 0, "var_1": 2}, {"var_0": 5, "var_1": 8}, {"var_0": 9, "var_1": 4},
             {"var_0": 3, "var_1": 5}, {"var_0": 7, "var_1": 7}, {"var_0": 6, "var_1": 7}, {"var_0": 7, "var_1": 6},
             {"var_0": 4, "var_1": 6}, {"var_0": 6, "var_1": 8}, {"var_0": 7, "var_1": 7}, {"var_0": 9, "var_1": 8},
             {"var_0": 9, "var_1": 2}, {"var_0": 3, "var_1": 9}, {"var_0": 2, "var_1": 7}, {"var_0": 6, "var_1": 8},
             {"var_0": 4, "var_1": 2}, {"var_0": 7, "var_1": 2}, {"var_0": 8, "var_1": 5}, {"var_0": 6, "var_1": 3},
             {"var_0": 5, "var_1": 4}, {"var_0": 6, "var_1": 6}, {"var_0": 2, "var_1": 1}, {"var_0": 8, "var_1": 4},
             {"var_0": 0, "var_1": 3}, {"var_0": 9, "var_1": 3}, {"var_0": 5, "var_1": 2}, {"var_0": 1, "var_1": 3},
             {"var_0": 1, "var_1": 0}, {"var_0": 8, "var_1": 9}, {"var_0": 4, "var_1": 9}, {"var_0": 0, "var_1": 6},
             {"var_0": 6, "var_1": 6}, {"var_0": 1, "var_1": 8}, {"var_0": 0, "var_1": 8}, {"var_0": 3, "var_1": 2},
             {"var_0": 5, "var_1": 8}, {"var_0": 5, "var_1": 7}, {"var_0": 1, "var_1": 1}, {"var_0": 0, "var_1": 8},
             {"var_0": 0, "var_1": 3}, {"var_0": 7, "var_1": 7}, {"var_0": 9, "var_1": 1}, {"var_0": 0, "var_1": 3},
             {"var_0": 6, "var_1": 8}, {"var_0": 6, "var_1": 2}, {"var_0": 1, "var_1": 9}, {"var_0": 2, "var_1": 3},
             {"var_0": 9, "var_1": 8}, {"var_0": 7, "var_1": 5}, {"var_0": 2, "var_1": 7}, {"var_0": 0, "var_1": 2},
             {"var_0": 1, "var_1": 5}, {"var_0": 7, "var_1": 9}, {"var_0": 4, "var_1": 5}, {"var_0": 3, "var_1": 1},
             {"var_0": 9, "var_1": 8}, {"var_0": 3, "var_1": 6}, {"var_0": 1, "var_1": 4}, {"var_0": 7, "var_1": 5},
             {"var_0": 9, "var_1": 9}, {"var_0": 1, "var_1": 1}, {"var_0": 7, "var_1": 5}, {"var_0": 1, "var_1": 4},
             {"var_0": 2, "var_1": 5}, {"var_0": 9, "var_1": 7}, {"var_0": 6, "var_1": 8}, {"var_0": 4, "var_1": 8},
             {"var_0": 1, "var_1": 1}, {"var_0": 8, "var_1": 1}, {"var_0": 5, "var_1": 2}, {"var_0": 4, "var_1": 5},
             {"var_0": 8, "var_1": 0}, {"var_0": 8, "var_1": 2}, {"var_0": 7, "var_1": 6}, {"var_0": 9, "var_1": 2},
             {"var_0": 8, "var_1": 6}, {"var_0": 7, "var_1": 9}, {"var_0": 0, "var_1": 4}, {"var_0": 8, "var_1": 7},
             {"var_0": 5, "var_1": 6}, {"var_0": 9, "var_1": 7}, {"var_0": 3, "var_1": 8}, {"var_0": 7, "var_1": 3},
             {"var_0": 2, "var_1": 4}, {"var_0": 9, "var_1": 6}, {"var_0": 7, "var_1": 3}, {"var_0": 7, "var_1": 6},
             {"var_0": 2, "var_1": 8}, {"var_0": 3, "var_1": 0}, {"var_0": 2, "var_1": 4}, {"var_0": 2, "var_1": 6}],
        "expected_outputs":
            [18, 11, 10, 16, 3, 3, 3, 7, 17, 2, 13, 13, 8, 14, 13, 13, 10, 14, 14, 17, 11, 12, 9, 14, 6, 9, 13, 9, 9,
             12, 3, 12, 3, 12, 7, 4, 1, 17, 13, 6, 12, 9, 8, 5, 13, 12, 2, 8, 3, 14, 10, 3, 14, 8, 10, 5, 17, 12, 9, 2,
             6, 16, 9, 4, 17, 9, 5, 12, 18, 2, 12, 5, 7, 16, 14, 12, 2, 9, 7, 9, 8, 10, 13, 11, 14, 16, 4, 15, 11, 16,
             11, 10, 6, 15, 10, 13, 10, 3, 6, 8]
    }
    total_error = 0.0

    for input_set, expected_output in zip(test_data["inputs"], test_data["expected_outputs"]):
        interpreter = MiniLangInterpreter(input_data=input_set, max_loop_iterations=1000, max_execution_time=3)
        interpreter.execute_program(program)
        output = interpreter.output_buffer

        length_score = evaluate_output_length(output, desired_length=1)
        total_error += (1.0 - length_score) * 10

        if output:
            actual_output = float(output[-1])
            expected_output = float(expected_output)
            total_error += abs(actual_output - expected_output)
        else:
            total_error += float('inf')

    return 1.0 / (1.0 + total_error)


def fitness_1_2_B(program):
    """
    Zadanie 1.2.B:
    Program powinien odczytać dwie pierwsze liczby z wejścia i zwrócić na wyjściu (jedynie) ich sumę.
    Na wejściu mogą być tylko całkowite liczby w zakresie [-9,9].
    """
    test_data = {
        "inputs":
            [{"var_0": 2, "var_1": 1}, {"var_0": -7, "var_1": 7}, {"var_0": 5, "var_1": 4}, {"var_0": 6, "var_1": 6},
             {"var_0": -9, "var_1": 7}, {"var_0": 4, "var_1": -4}, {"var_0": 0, "var_1": 1}, {"var_0": 2, "var_1": 2},
             {"var_0": -7, "var_1": 2}, {"var_0": -9, "var_1": 7}, {"var_0": -6, "var_1": -1},
             {"var_0": 1, "var_1": -5}, {"var_0": -9, "var_1": 4}, {"var_0": 2, "var_1": -4}, {"var_0": 5, "var_1": 1},
             {"var_0": 3, "var_1": 1}, {"var_0": 0, "var_1": -1}, {"var_0": -9, "var_1": 6}, {"var_0": -9, "var_1": -2},
             {"var_0": -9, "var_1": -3}, {"var_0": 1, "var_1": -9}, {"var_0": 9, "var_1": -2},
             {"var_0": -7, "var_1": -2}, {"var_0": 1, "var_1": -9}, {"var_0": -2, "var_1": -4},
             {"var_0": 8, "var_1": 0}, {"var_0": 0, "var_1": -7}, {"var_0": -8, "var_1": 6}, {"var_0": 5, "var_1": 0},
             {"var_0": 4, "var_1": 0}, {"var_0": 3, "var_1": -1}, {"var_0": 4, "var_1": -9}, {"var_0": 1, "var_1": 1},
             {"var_0": 3, "var_1": 7}, {"var_0": 5, "var_1": -1}, {"var_0": 7, "var_1": -3}, {"var_0": 9, "var_1": -9},
             {"var_0": 1, "var_1": -3}, {"var_0": -9, "var_1": 6}, {"var_0": 1, "var_1": -7}, {"var_0": -3, "var_1": 4},
             {"var_0": 1, "var_1": 0}, {"var_0": -3, "var_1": -1}, {"var_0": 3, "var_1": -5}, {"var_0": 5, "var_1": -6},
             {"var_0": -6, "var_1": -7}, {"var_0": -8, "var_1": -7}, {"var_0": -3, "var_1": -8},
             {"var_0": -7, "var_1": 7}, {"var_0": 9, "var_1": 5}, {"var_0": -4, "var_1": 3}, {"var_0": -5, "var_1": -4},
             {"var_0": 8, "var_1": -6}, {"var_0": -7, "var_1": 4}, {"var_0": 1, "var_1": -1}, {"var_0": -9, "var_1": 0},
             {"var_0": 9, "var_1": 2}, {"var_0": 0, "var_1": 2}, {"var_0": -3, "var_1": 9}, {"var_0": 1, "var_1": -9},
             {"var_0": -5, "var_1": 3}, {"var_0": 7, "var_1": -4}, {"var_0": 8, "var_1": 2}, {"var_0": -2, "var_1": -4},
             {"var_0": -1, "var_1": -7}, {"var_0": -3, "var_1": 6}, {"var_0": -3, "var_1": -9},
             {"var_0": -6, "var_1": 4}, {"var_0": -3, "var_1": -5}, {"var_0": -1, "var_1": 0},
             {"var_0": -5, "var_1": -3}, {"var_0": 8, "var_1": 6}, {"var_0": -7, "var_1": -7},
             {"var_0": -7, "var_1": -2}, {"var_0": -4, "var_1": -3}, {"var_0": 4, "var_1": 6},
             {"var_0": 4, "var_1": -3}, {"var_0": 6, "var_1": 8}, {"var_0": -7, "var_1": 1}, {"var_0": 5, "var_1": -9},
             {"var_0": 3, "var_1": -4}, {"var_0": 9, "var_1": 1}, {"var_0": 0, "var_1": -8}, {"var_0": 9, "var_1": 9},
             {"var_0": -6, "var_1": -5}, {"var_0": 8, "var_1": 9}, {"var_0": -6, "var_1": -3}, {"var_0": 5, "var_1": 7},
             {"var_0": 7, "var_1": 2}, {"var_0": -9, "var_1": -6}, {"var_0": -2, "var_1": 3}, {"var_0": 2, "var_1": 4},
             {"var_0": 5, "var_1": -7}, {"var_0": -3, "var_1": 9}, {"var_0": -3, "var_1": -5},
             {"var_0": -6, "var_1": 9}, {"var_0": 7, "var_1": 4}, {"var_0": 6, "var_1": -5}, {"var_0": -2, "var_1": 1},
             {"var_0": -6, "var_1": 1}],
        "expected_outputs":
            [3, 0, 9, 12, -2, 0, 1, 4, -5, -2, -7, -4, -5, -2, 6, 4, -1, -3, -11, -12, -8, 7, -9, -8, -6, 8, -7, -2, 5,
             4, 2, -5, 2, 10, 4, 4, 0, -2, -3, -6, 1, 1, -4, -2, -1, -13, -15, -11, 0, 14, -1, -9, 2, -3, 0, -9, 11, 2,
             6, -8, -2, 3, 10, -6, -8, 3, -12, -2, -8, -1, -8, 14, -14, -9, -7, 10, 1, 14, -6, -4, -1, 10, -8, 18, -11,
             17, -9, 12, 9, -15, 1, 6, -2, 6, -8, 3, 11, 1, -1, -5]
    }

    total_error = 0.0

    for input_set, expected_output in zip(test_data["inputs"], test_data["expected_outputs"]):
        interpreter = MiniLangInterpreter(input_data=input_set, max_loop_iterations=1000, max_execution_time=3)
        interpreter.execute_program(program)
        output = interpreter.output_buffer

        length_score = evaluate_output_length(output, desired_length=1)
        total_error += (1.0 - length_score) * 10

        if output:
            actual_output = float(output[-1])
            expected_output = float(expected_output)
            total_error += abs(actual_output - expected_output)
        else:
            total_error += float('inf')

    return 1.0 / (1.0 + total_error)


def fitness_1_2_C(program):
    """
    Zadanie 1.2.C:
    Program powinien odczytać dwie pierwsze liczby z wejścia i zwrócić na wyjściu (jedynie) ich sumę.
    Na wejściu mogą być tylko całkowite liczby w zakresie [-9999,9999].
    """
    test_data = {
        "inputs":
            [{"var_0": 2708, "var_1": 1497}, {"var_0": 6889, "var_1": -2146}, {"var_0": 8027, "var_1": 1624},
             {"var_0": 6392, "var_1": 529}, {"var_0": 108, "var_1": 4323}, {"var_0": -6431, "var_1": -2475},
             {"var_0": 4079, "var_1": -2093}, {"var_0": -5104, "var_1": -9440}, {"var_0": 4545, "var_1": -465},
             {"var_0": -5293, "var_1": 4338}, {"var_0": -9626, "var_1": -4850}, {"var_0": 4548, "var_1": -8460},
             {"var_0": -2766, "var_1": 19}, {"var_0": -6454, "var_1": 1056}, {"var_0": 2805, "var_1": 9260},
             {"var_0": 7280, "var_1": -5595}, {"var_0": -5428, "var_1": -7572}, {"var_0": -7403, "var_1": 8521},
             {"var_0": -5778, "var_1": 6365}, {"var_0": -8728, "var_1": 2141}, {"var_0": 9925, "var_1": -1078},
             {"var_0": 2506, "var_1": -9434}, {"var_0": 3480, "var_1": -4686}, {"var_0": -9344, "var_1": -3903},
             {"var_0": 6654, "var_1": -9852}, {"var_0": 8470, "var_1": 3325}, {"var_0": 256, "var_1": 2169},
             {"var_0": 6630, "var_1": -2985}, {"var_0": -2150, "var_1": -2956}, {"var_0": -7093, "var_1": 8387},
             {"var_0": 5098, "var_1": -146}, {"var_0": 339, "var_1": -4961}, {"var_0": -5820, "var_1": -913},
             {"var_0": -2103, "var_1": -4766}, {"var_0": -802, "var_1": 236}, {"var_0": -7786, "var_1": -9216},
             {"var_0": -4480, "var_1": 6392}, {"var_0": -3044, "var_1": 5498}, {"var_0": -9880, "var_1": 9846},
             {"var_0": 3122, "var_1": 6624}, {"var_0": -5102, "var_1": 5127}, {"var_0": 6596, "var_1": 4493},
             {"var_0": 4081, "var_1": 3982}, {"var_0": 545, "var_1": 8513}, {"var_0": -7498, "var_1": -4940},
             {"var_0": 5312, "var_1": -8117}, {"var_0": -8007, "var_1": -2062}, {"var_0": -5542, "var_1": 7933},
             {"var_0": 2462, "var_1": 9036}, {"var_0": -993, "var_1": -6768}, {"var_0": -3082, "var_1": 86},
             {"var_0": -4844, "var_1": 479}, {"var_0": 6882, "var_1": -393}, {"var_0": 6387, "var_1": -8179},
             {"var_0": -567, "var_1": -2085}, {"var_0": -5913, "var_1": -3071}, {"var_0": -1786, "var_1": 2498},
             {"var_0": 6282, "var_1": -6818}, {"var_0": 6651, "var_1": -3730}, {"var_0": 1112, "var_1": -8297},
             {"var_0": -3191, "var_1": 2033}, {"var_0": 6463, "var_1": 8612}, {"var_0": 6837, "var_1": 7571},
             {"var_0": 6747, "var_1": 2740}, {"var_0": -7666, "var_1": 619}, {"var_0": 4623, "var_1": 141},
             {"var_0": 454, "var_1": -413}, {"var_0": -2803, "var_1": -3653}, {"var_0": 3308, "var_1": 3415},
             {"var_0": -1158, "var_1": -549}, {"var_0": 5497, "var_1": -9662}, {"var_0": 7440, "var_1": -4438},
             {"var_0": 6293, "var_1": -5494}, {"var_0": -5792, "var_1": 6612}, {"var_0": -2392, "var_1": -8429},
             {"var_0": 7128, "var_1": 7112}, {"var_0": -9494, "var_1": 5250}, {"var_0": 1587, "var_1": 2506},
             {"var_0": -820, "var_1": -2164}, {"var_0": -9697, "var_1": 3826}, {"var_0": 5856, "var_1": 7479},
             {"var_0": -4122, "var_1": -7713}, {"var_0": -3124, "var_1": 2806}, {"var_0": -2113, "var_1": 9706},
             {"var_0": -7219, "var_1": -6345}, {"var_0": -6879, "var_1": -1625}, {"var_0": 9625, "var_1": -7452},
             {"var_0": 7189, "var_1": 9485}, {"var_0": 7932, "var_1": 4428}, {"var_0": 4458, "var_1": 3637},
             {"var_0": 9807, "var_1": 4905}, {"var_0": 2069, "var_1": 1461}, {"var_0": 6890, "var_1": 1026},
             {"var_0": 192, "var_1": -1863}, {"var_0": 401, "var_1": 750}, {"var_0": 2389, "var_1": -1149},
             {"var_0": -4495, "var_1": -5018}, {"var_0": 3752, "var_1": -1049}, {"var_0": 3756, "var_1": 4905},
             {"var_0": -9741, "var_1": 8935}],
        "expected_outputs":
            [4205, 4743, 9651, 6921, 4431, -8906, 1986, -14544, 4080, -955, -14476, -3912, -2747, -5398, 12065, 1685,
             -13000, 1118, 587, -6587, 8847, -6928, -1206, -13247, -3198, 11795, 2425, 3645, -5106, 1294, 4952, -4622,
             -6733, -6869, -566, -17002, 1912, 2454, -34, 9746, 25, 11089, 8063, 9058, -12438, -2805, -10069, 2391,
             11498, -7761, -2996, -4365, 6489, -1792, -2652, -8984, 712, -536, 2921, -7185, -1158, 15075, 14408, 9487,
             -7047, 4764, 41, -6456, 6723, -1707, -4165, 3002, 799, 820, -10821, 14240, -4244, 4093, -2984, -5871,
             13335, -11835, -318, 7593, -13564, -8504, 2173, 16674, 12360, 8095, 14712, 3530, 7916, -1671, 1151, 1240,
             -9513, 2703, 8661, -806]
    }
    total_error = 0.0

    for input_set, expected_output in zip(test_data["inputs"], test_data["expected_outputs"]):
        interpreter = MiniLangInterpreter(input_data=input_set, max_loop_iterations=1000, max_execution_time=3)
        interpreter.execute_program(program)
        output = interpreter.output_buffer

        length_score = evaluate_output_length(output, desired_length=1)
        total_error += (1.0 - length_score) * 10

        if output:
            actual_output = float(output[-1])
            expected_output = float(expected_output)
            total_error += abs(actual_output - expected_output)
        else:
            total_error += float('inf')

    return 1.0 / (1.0 + total_error)


def fitness_1_2_D(program):
    """
    Zadanie 1.2.D:
    Program powinien odczytać dwie pierwsze liczby z wejścia i zwrócić na wyjściu (jedynie) ich różnicę.
    Na wejściu mogą być tylko całkowite liczby w zakresie [-9999,9999].
    """
    test_data = {
        "inputs":
            [{"var_0": 1069, "var_1": 7369}, {"var_0": 8327, "var_1": 4256}, {"var_0": 1369, "var_1": 4417},
             {"var_0": 9151, "var_1": 6986}, {"var_0": 9129, "var_1": 5615}, {"var_0": -1399, "var_1": -7672},
             {"var_0": 5829, "var_1": -3256}, {"var_0": -1401, "var_1": 3236}, {"var_0": 9966, "var_1": -3986},
             {"var_0": 5877, "var_1": 5952}, {"var_0": 9499, "var_1": -1801}, {"var_0": -4397, "var_1": 9567},
             {"var_0": 7807, "var_1": 4776}, {"var_0": -1371, "var_1": 2181}, {"var_0": 7604, "var_1": 1509},
             {"var_0": 3672, "var_1": -2126}, {"var_0": -8873, "var_1": 6268}, {"var_0": 7216, "var_1": -513},
             {"var_0": -8438, "var_1": 4858}, {"var_0": -6440, "var_1": -7763}, {"var_0": -4892, "var_1": -5483},
             {"var_0": 1570, "var_1": 7150}, {"var_0": -4975, "var_1": 171}, {"var_0": -8499, "var_1": -6171},
             {"var_0": 1274, "var_1": 1260}, {"var_0": 2726, "var_1": 9132}, {"var_0": -2571, "var_1": -7602},
             {"var_0": 1417, "var_1": -6392}, {"var_0": -5624, "var_1": -9123}, {"var_0": 8221, "var_1": -6447},
             {"var_0": -232, "var_1": 6507}, {"var_0": 2248, "var_1": -5741}, {"var_0": 935, "var_1": -1563},
             {"var_0": -2698, "var_1": -7572}, {"var_0": 4073, "var_1": 611}, {"var_0": 9742, "var_1": -4948},
             {"var_0": 701, "var_1": 6265}, {"var_0": 7307, "var_1": 8602}, {"var_0": 1484, "var_1": 8776},
             {"var_0": -1243, "var_1": 8091}, {"var_0": -708, "var_1": -5477}, {"var_0": 3643, "var_1": 3054},
             {"var_0": 751, "var_1": 6540}, {"var_0": -4526, "var_1": -3448}, {"var_0": -4448, "var_1": -3635},
             {"var_0": 1124, "var_1": -3813}, {"var_0": -7451, "var_1": -4918}, {"var_0": -8935, "var_1": -7477},
             {"var_0": 7505, "var_1": -4265}, {"var_0": -7459, "var_1": -4853}, {"var_0": -4514, "var_1": 5144},
             {"var_0": -6776, "var_1": 2710}, {"var_0": 2354, "var_1": 6267}, {"var_0": 554, "var_1": 4355},
             {"var_0": 1768, "var_1": 4924}, {"var_0": -69, "var_1": 5678}, {"var_0": 6151, "var_1": -1706},
             {"var_0": -3508, "var_1": 4186}, {"var_0": 7237, "var_1": 2349}, {"var_0": 8238, "var_1": 9291},
             {"var_0": -5112, "var_1": -7850}, {"var_0": -6463, "var_1": 8425}, {"var_0": -1141, "var_1": 3944},
             {"var_0": -5265, "var_1": 8678}, {"var_0": 1258, "var_1": 6247}, {"var_0": 8807, "var_1": -6248},
             {"var_0": 9256, "var_1": 9093}, {"var_0": -9140, "var_1": 9410}, {"var_0": 7672, "var_1": 6457},
             {"var_0": 9280, "var_1": -4552}, {"var_0": -808, "var_1": -575}, {"var_0": 8791, "var_1": 1663},
             {"var_0": 220, "var_1": 6485}, {"var_0": 2191, "var_1": 5629}, {"var_0": -4379, "var_1": -7533},
             {"var_0": 1409, "var_1": -6282}, {"var_0": -2236, "var_1": -6302}, {"var_0": -5771, "var_1": 231},
             {"var_0": -4035, "var_1": -1791}, {"var_0": -7756, "var_1": 5924}, {"var_0": 4767, "var_1": -8333},
             {"var_0": 6675, "var_1": -7971}, {"var_0": -8561, "var_1": -4374}, {"var_0": 1209, "var_1": 4580},
             {"var_0": -5712, "var_1": 5247}, {"var_0": -3714, "var_1": -5861}, {"var_0": -7352, "var_1": 8505},
             {"var_0": -4299, "var_1": 7624}, {"var_0": -180, "var_1": -2052}, {"var_0": 9065, "var_1": -1154},
             {"var_0": 4687, "var_1": -8978}, {"var_0": -718, "var_1": 3200}, {"var_0": 8537, "var_1": 7270},
             {"var_0": -5174, "var_1": 3292}, {"var_0": 956, "var_1": -2819}, {"var_0": -1221, "var_1": 4786},
             {"var_0": 7997, "var_1": -3396}, {"var_0": 24, "var_1": 4874}, {"var_0": -4578, "var_1": -2477},
             {"var_0": 7496, "var_1": -355}],
        "expected_outputs":
            [-6300, 4071, -3048, 2165, 3514, 6273, 9085, -4637, 13952, -75, 11300, -13964, 3031, -3552, 6095, 5798,
             -15141, 7729, -13296, 1323, 591, -5580, -5146, -2328, 14, -6406, 5031, 7809, 3499, 14668, -6739, 7989,
             2498, 4874, 3462, 14690, -5564, -1295, -7292, -9334, 4769, 589, -5789, -1078, -813, 4937, -2533, -1458,
             11770, -2606, -9658, -9486, -3913, -3801, -3156, -5747, 7857, -7694, 4888, -1053, 2738, -14888, -5085,
             -13943, -4989, 15055, 163, -18550, 1215, 13832, -233, 7128, -6265, -3438, 3154, 7691, 4066, -6002, -2244,
             -13680, 13100, 14646, -4187, -3371, -10959, 2147, -15857, -11923, 1872, 10219, 13665, -3918, 1267, -8466,
             3775, -6007, 11393, -4850, -2101, 7851]
    }
    total_error = 0.0

    for input_set, expected_output in zip(test_data["inputs"], test_data["expected_outputs"]):
        interpreter = MiniLangInterpreter(input_data=input_set, max_loop_iterations=1000, max_execution_time=3)
        interpreter.execute_program(program)
        output = interpreter.output_buffer

        length_score = evaluate_output_length(output, desired_length=1)
        total_error += (1.0 - length_score) * 10

        if output:
            actual_output = float(output[-1])
            expected_output = float(expected_output)
            total_error += abs(actual_output - expected_output)
        else:
            total_error += float('inf')

    return 1.0 / (1.0 + total_error)


def fitness_1_2_E(program):
    """
    Zadanie 1.2.E:
    Program powinien odczytać dwie pierwsze liczby z wejścia i zwrócić na wyjściu (jedynie) ich iloczyn.
    Na wejściu mogą być tylko całkowite liczby w zakresie [-9999,9999].
    """
    test_data = {
        "inputs":
            [{"var_0": -2237, "var_1": -1290}, {"var_0": -6701, "var_1": -4333}, {"var_0": 1138, "var_1": 5432},
             {"var_0": -3823, "var_1": 5803}, {"var_0": 6205, "var_1": 2958}, {"var_0": -5551, "var_1": 9217},
             {"var_0": -3137, "var_1": 5622}, {"var_0": -6936, "var_1": 8553}, {"var_0": -5728, "var_1": -8701},
             {"var_0": -1886, "var_1": -2561}, {"var_0": -1735, "var_1": 7045}, {"var_0": -1943, "var_1": -1892},
             {"var_0": -9540, "var_1": 8335}, {"var_0": 1739, "var_1": -7256}, {"var_0": 4048, "var_1": 9651},
             {"var_0": -2987, "var_1": 710}, {"var_0": 2829, "var_1": -3366}, {"var_0": -7034, "var_1": -6483},
             {"var_0": -6691, "var_1": 8538}, {"var_0": 1791, "var_1": 5595}, {"var_0": -2958, "var_1": -335},
             {"var_0": 9601, "var_1": 7738}, {"var_0": 8770, "var_1": 8321}, {"var_0": 5069, "var_1": 149},
             {"var_0": 1025, "var_1": 356}, {"var_0": -607, "var_1": -881}, {"var_0": 9625, "var_1": 4974},
             {"var_0": 8353, "var_1": -4000}, {"var_0": 9264, "var_1": 825}, {"var_0": 4536, "var_1": -4426},
             {"var_0": 2562, "var_1": 1749}, {"var_0": -8856, "var_1": -2369}, {"var_0": -6702, "var_1": -7586},
             {"var_0": -3100, "var_1": 8768}, {"var_0": -7513, "var_1": -2748}, {"var_0": 1011, "var_1": -7994},
             {"var_0": -2569, "var_1": 8313}, {"var_0": 2937, "var_1": 8999}, {"var_0": -360, "var_1": -4402},
             {"var_0": -9111, "var_1": -240}, {"var_0": 2466, "var_1": -3901}, {"var_0": -7971, "var_1": 4258},
             {"var_0": 2547, "var_1": 9764}, {"var_0": -86, "var_1": 6187}, {"var_0": 7441, "var_1": 1667},
             {"var_0": 8647, "var_1": -7360}, {"var_0": -8909, "var_1": -6077}, {"var_0": 8795, "var_1": -4413},
             {"var_0": 8859, "var_1": -7080}, {"var_0": -6860, "var_1": 1477}, {"var_0": 7943, "var_1": -931},
             {"var_0": 8537, "var_1": 6617}, {"var_0": 4278, "var_1": -7617}, {"var_0": -4369, "var_1": 6283},
             {"var_0": 8498, "var_1": 6395}, {"var_0": -6517, "var_1": 9850}, {"var_0": -4719, "var_1": 3571},
             {"var_0": -6599, "var_1": -1388}, {"var_0": 4995, "var_1": 9917}, {"var_0": -9644, "var_1": -5036},
             {"var_0": -2954, "var_1": 2720}, {"var_0": 6132, "var_1": -1651}, {"var_0": 3554, "var_1": 1315},
             {"var_0": 1385, "var_1": -8023}, {"var_0": 5705, "var_1": 4074}, {"var_0": -8499, "var_1": -4090},
             {"var_0": -9089, "var_1": -7286}, {"var_0": 5460, "var_1": 7867}, {"var_0": -5515, "var_1": -2779},
             {"var_0": 2063, "var_1": 8339}, {"var_0": -9455, "var_1": -9623}, {"var_0": -6454, "var_1": 9162},
             {"var_0": 5689, "var_1": -7166}, {"var_0": -6635, "var_1": -9415}, {"var_0": -3285, "var_1": 646},
             {"var_0": 3236, "var_1": -5903}, {"var_0": -1375, "var_1": -6914}, {"var_0": 5280, "var_1": 8992},
             {"var_0": 2975, "var_1": -5032}, {"var_0": -3320, "var_1": -9945}, {"var_0": -4724, "var_1": -4092},
             {"var_0": -9392, "var_1": -7228}, {"var_0": -7707, "var_1": 666}, {"var_0": -7977, "var_1": -8209},
             {"var_0": 7079, "var_1": -6306}, {"var_0": 4721, "var_1": 5792}, {"var_0": -9999, "var_1": 5511},
             {"var_0": 89, "var_1": -1162}, {"var_0": 5303, "var_1": -2802}, {"var_0": -5787, "var_1": 6755},
             {"var_0": 2005, "var_1": -8168}, {"var_0": 8295, "var_1": 220}, {"var_0": -2363, "var_1": -8365},
             {"var_0": -6098, "var_1": 2082}, {"var_0": 5144, "var_1": -8939}, {"var_0": 7586, "var_1": -7912},
             {"var_0": -8669, "var_1": 1924}, {"var_0": 9055, "var_1": -7145}, {"var_0": 7631, "var_1": -698},
             {"var_0": 1824, "var_1": -9917}],
        "expected_outputs":
            [2885730, 29035433, 6181616, -22184869, 18354390, -51163567, -17636214, -59323608, 49839328, 4830046,
             -12223075, 3676156, -79515900, -12618184, 39067248, -2120770, -9522414, 45601422, -57127758, 10020645,
             990930, 74292538, 72975170, 755281, 364900, 534767, 47874750, -33412000, 7642800, -20076336, 4480938,
             20979864, 50841372, -27180800, 20645724, -8081934, -21356097, 26430063, 1584720, 2186640, -9619866,
             -33940518, 24868908, -532082, 12404147, -63641920, 54139993, -38812335, -62721720, -10132220, -7394933,
             56489329, -32585526, -27450427, 54344710, -64192450, -16851549, 9159412, 49535415, 48567184, -8034880,
             -10123932, 4673510, -11111855, 23242170, 34760910, 66222454, 42953820, 15326185, 17203357, 90985465,
             -59131548, -40767374, 62468525, -2122110, -19102108, 9506750, 47477760, -14970200, 33017400, 19330608,
             67885376, -5132862, 65483193, -44640174, 27344032, -55104489, -103418, -14859006, -39091185, -16376840,
             1824900, 19766495, -12696036, -45982216, -60020432, -16679156, -64697975, -5326438, -18088608]
    }

    total_error = 0.0

    for input_set, expected_output in zip(test_data["inputs"], test_data["expected_outputs"]):
        interpreter = MiniLangInterpreter(input_data=input_set, max_loop_iterations=1000, max_execution_time=3)
        interpreter.execute_program(program)
        output = interpreter.output_buffer

        length_score = evaluate_output_length(output, desired_length=1)
        total_error += (1.0 - length_score) * 10

        if output:
            actual_output = float(output[-1])
            expected_output = float(expected_output)
            total_error += abs(actual_output - expected_output)
        else:
            total_error += float('inf')

    return 1.0 / (1.0 + total_error)


def fitness_1_3_A(program):
    """
    Zadanie 1.3.A:
    Program powinien odczytać dwie pierwsze liczby z wejścia i zwrócić na wyjściu (jedynie) większą z nich.
    Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [0,9].
    """
    test_data = {
        "inputs":
            [{"var_0": 1, "var_1": 4}, {"var_0": 0, "var_1": 5}, {"var_0": 6, "var_1": 3}, {"var_0": 9, "var_1": 8},
             {"var_0": 0, "var_1": 5}, {"var_0": 7, "var_1": 8}, {"var_0": 3, "var_1": 5}, {"var_0": 7, "var_1": 2},
             {"var_0": 3, "var_1": 2}, {"var_0": 3, "var_1": 7}, {"var_0": 0, "var_1": 9}, {"var_0": 9, "var_1": 8},
             {"var_0": 7, "var_1": 4}, {"var_0": 7, "var_1": 7}, {"var_0": 7, "var_1": 3}, {"var_0": 3, "var_1": 4},
             {"var_0": 8, "var_1": 1}, {"var_0": 7, "var_1": 3}, {"var_0": 9, "var_1": 9}, {"var_0": 0, "var_1": 8},
             {"var_0": 6, "var_1": 6}, {"var_0": 3, "var_1": 4}, {"var_0": 1, "var_1": 9}, {"var_0": 2, "var_1": 7},
             {"var_0": 5, "var_1": 0}, {"var_0": 8, "var_1": 8}, {"var_0": 5, "var_1": 8}, {"var_0": 2, "var_1": 8},
             {"var_0": 6, "var_1": 3}, {"var_0": 4, "var_1": 4}, {"var_0": 1, "var_1": 8}, {"var_0": 4, "var_1": 7},
             {"var_0": 2, "var_1": 9}, {"var_0": 7, "var_1": 7}, {"var_0": 6, "var_1": 3}, {"var_0": 2, "var_1": 9},
             {"var_0": 4, "var_1": 4}, {"var_0": 7, "var_1": 9}, {"var_0": 4, "var_1": 1}, {"var_0": 4, "var_1": 2},
             {"var_0": 4, "var_1": 8}, {"var_0": 7, "var_1": 9}, {"var_0": 7, "var_1": 7}, {"var_0": 6, "var_1": 0},
             {"var_0": 8, "var_1": 0}, {"var_0": 0, "var_1": 9}, {"var_0": 2, "var_1": 5}, {"var_0": 6, "var_1": 9},
             {"var_0": 6, "var_1": 5}, {"var_0": 4, "var_1": 0}, {"var_0": 9, "var_1": 4}, {"var_0": 6, "var_1": 7},
             {"var_0": 6, "var_1": 9}, {"var_0": 0, "var_1": 7}, {"var_0": 8, "var_1": 0}, {"var_0": 2, "var_1": 1},
             {"var_0": 8, "var_1": 8}, {"var_0": 4, "var_1": 2}, {"var_0": 8, "var_1": 3}, {"var_0": 8, "var_1": 8},
             {"var_0": 7, "var_1": 9}, {"var_0": 4, "var_1": 4}, {"var_0": 6, "var_1": 5}, {"var_0": 3, "var_1": 0},
             {"var_0": 5, "var_1": 9}, {"var_0": 0, "var_1": 6}, {"var_0": 0, "var_1": 5}, {"var_0": 2, "var_1": 6},
             {"var_0": 9, "var_1": 0}, {"var_0": 1, "var_1": 0}, {"var_0": 3, "var_1": 0}, {"var_0": 4, "var_1": 4},
             {"var_0": 2, "var_1": 5}, {"var_0": 5, "var_1": 5}, {"var_0": 5, "var_1": 8}, {"var_0": 7, "var_1": 8},
             {"var_0": 4, "var_1": 4}, {"var_0": 5, "var_1": 2}, {"var_0": 9, "var_1": 0}, {"var_0": 1, "var_1": 7},
             {"var_0": 8, "var_1": 5}, {"var_0": 3, "var_1": 3}, {"var_0": 5, "var_1": 0}, {"var_0": 3, "var_1": 5},
             {"var_0": 6, "var_1": 8}, {"var_0": 5, "var_1": 8}, {"var_0": 5, "var_1": 4}, {"var_0": 1, "var_1": 3},
             {"var_0": 8, "var_1": 6}, {"var_0": 3, "var_1": 9}, {"var_0": 9, "var_1": 3}, {"var_0": 9, "var_1": 2},
             {"var_0": 3, "var_1": 7}, {"var_0": 6, "var_1": 2}, {"var_0": 7, "var_1": 3}, {"var_0": 0, "var_1": 2},
             {"var_0": 3, "var_1": 5}, {"var_0": 0, "var_1": 5}, {"var_0": 5, "var_1": 2}, {"var_0": 7, "var_1": 7}],
        "expected_outputs":
            [4, 5, 6, 9, 5, 8, 5, 7, 3, 7, 9, 9, 7, 7, 7, 4, 8, 7, 9, 8, 6, 4, 9, 7, 5, 8, 8, 8, 6, 4, 8, 7, 9, 7, 6, 9,
             4, 9, 4, 4, 8, 9, 7, 6, 8, 9, 5, 9, 6, 4, 9, 7, 9, 7, 8, 2, 8, 4, 8, 8, 9, 4, 6, 3, 9, 6, 5, 6, 9, 1, 3, 4,
             5, 5, 8, 8, 4, 5, 9, 7, 8, 3, 5, 5, 8, 8, 5, 3, 8, 9, 9, 9, 7, 6, 7, 2, 5, 5, 5, 7]
    }
    total_error = 0.0

    for input_set, expected_output in zip(test_data["inputs"], test_data["expected_outputs"]):
        interpreter = MiniLangInterpreter(input_data=input_set, max_loop_iterations=1000, max_execution_time=3)
        interpreter.execute_program(program)
        output = interpreter.output_buffer

        length_score = evaluate_output_length(output, desired_length=1)
        total_error += (1.0 - length_score) * 10

        if output:
            actual_output = float(output[-1])
            expected_output = float(expected_output)
            total_error += abs(actual_output - expected_output)
        else:
            total_error += float('inf')

    return 1.0 / (1.0 + total_error)


def fitness_1_3_B(program):
    """
    Zadanie 1.3.B:
    Program powinien odczytać dwie pierwsze liczby z wejścia i zwrócić na wyjściu (jedynie) większą z nich.
    Na wejściu mogą być tylko całkowite liczby w zakresie [-9999,9999].
    """
    test_data = {
        "inputs":
            [{"var_0": -3856, "var_1": 6890}, {"var_0": 9035, "var_1": -3439}, {"var_0": -5570, "var_1": -7455},
             {"var_0": 8661, "var_1": -8936}, {"var_0": 1963, "var_1": 9384}, {"var_0": -7972, "var_1": -4301},
             {"var_0": 9723, "var_1": -1995}, {"var_0": -3146, "var_1": -7413}, {"var_0": 7639, "var_1": -1027},
             {"var_0": 7565, "var_1": -6320}, {"var_0": -8821, "var_1": -5673}, {"var_0": -1582, "var_1": -2817},
             {"var_0": 8768, "var_1": -3478}, {"var_0": -242, "var_1": 1403}, {"var_0": 8802, "var_1": 8656},
             {"var_0": -9310, "var_1": -46}, {"var_0": 310, "var_1": -4281}, {"var_0": -3518, "var_1": -6296},
             {"var_0": 2346, "var_1": -4174}, {"var_0": -5139, "var_1": 9005}, {"var_0": 9418, "var_1": 3635},
             {"var_0": 5535, "var_1": -9966}, {"var_0": 8288, "var_1": -4238}, {"var_0": -888, "var_1": -5806},
             {"var_0": 1093, "var_1": -6945}, {"var_0": 5986, "var_1": -208}, {"var_0": -9704, "var_1": -8940},
             {"var_0": -6335, "var_1": 58}, {"var_0": -2982, "var_1": -8523}, {"var_0": -7282, "var_1": -7759},
             {"var_0": -8480, "var_1": 6457}, {"var_0": 2979, "var_1": 5365}, {"var_0": 6715, "var_1": 5220},
             {"var_0": -611, "var_1": -8463}, {"var_0": -819, "var_1": 4212}, {"var_0": -5030, "var_1": 4553},
             {"var_0": -7215, "var_1": 2205}, {"var_0": -2839, "var_1": 1304}, {"var_0": 3278, "var_1": 2264},
             {"var_0": 7920, "var_1": 9912}, {"var_0": 1655, "var_1": 7251}, {"var_0": -3079, "var_1": -7483},
             {"var_0": -6813, "var_1": -2335}, {"var_0": 1751, "var_1": 1902}, {"var_0": 993, "var_1": 6797},
             {"var_0": -1094, "var_1": 5947}, {"var_0": -8323, "var_1": -3032}, {"var_0": -4627, "var_1": -79},
             {"var_0": -4842, "var_1": -1399}, {"var_0": 1365, "var_1": -3578}, {"var_0": 2259, "var_1": 8360},
             {"var_0": 4101, "var_1": 7909}, {"var_0": 2518, "var_1": -3879}, {"var_0": -2779, "var_1": -5668},
             {"var_0": -3298, "var_1": 6333}, {"var_0": -549, "var_1": 146}, {"var_0": 931, "var_1": -6457},
             {"var_0": 6609, "var_1": 3682}, {"var_0": 2779, "var_1": 9526}, {"var_0": -8423, "var_1": -5473},
             {"var_0": -7551, "var_1": -5321}, {"var_0": -9355, "var_1": -9033}, {"var_0": 5892, "var_1": -3260},
             {"var_0": -3820, "var_1": -9075}, {"var_0": 5878, "var_1": 182}, {"var_0": -7674, "var_1": -4676},
             {"var_0": -7809, "var_1": 5869}, {"var_0": 4193, "var_1": -9395}, {"var_0": 7138, "var_1": 1387},
             {"var_0": 1829, "var_1": -1381}, {"var_0": -5490, "var_1": 3892}, {"var_0": 9805, "var_1": -930},
             {"var_0": -7768, "var_1": 4309}, {"var_0": 7684, "var_1": -8599}, {"var_0": 2764, "var_1": 2146},
             {"var_0": -4576, "var_1": -3692}, {"var_0": -6612, "var_1": -2015}, {"var_0": 7323, "var_1": 2694},
             {"var_0": -3182, "var_1": 9914}, {"var_0": 2651, "var_1": 9518}, {"var_0": -5871, "var_1": -9055},
             {"var_0": -1145, "var_1": -4975}, {"var_0": 4967, "var_1": 4396}, {"var_0": -8829, "var_1": 3218},
             {"var_0": 2722, "var_1": -8335}, {"var_0": 2171, "var_1": -2609}, {"var_0": -994, "var_1": 468},
             {"var_0": 6481, "var_1": -4802}, {"var_0": -4894, "var_1": -5545}, {"var_0": 7818, "var_1": -8154},
             {"var_0": -2473, "var_1": 7075}, {"var_0": 7508, "var_1": -8578}, {"var_0": 5767, "var_1": 8711},
             {"var_0": -5833, "var_1": 4311}, {"var_0": -482, "var_1": -2392}, {"var_0": -8195, "var_1": -9835},
             {"var_0": -7525, "var_1": 2131}, {"var_0": -9709, "var_1": 7477}, {"var_0": -2610, "var_1": 5689},
             {"var_0": 4311, "var_1": -6714}],
        "expected_outputs":
            [6890, 9035, -5570, 8661, 9384, -4301, 9723, -3146, 7639, 7565, -5673, -1582, 8768, 1403, 8802, -46, 310,
             -3518, 2346, 9005, 9418, 5535, 8288, -888, 1093, 5986, -8940, 58, -2982, -7282, 6457, 5365, 6715, -611,
             4212, 4553, 2205, 1304, 3278, 9912, 7251, -3079, -2335, 1902, 6797, 5947, -3032, -79, -1399, 1365, 8360,
             7909, 2518, -2779, 6333, 146, 931, 6609, 9526, -5473, -5321, -9033, 5892, -3820, 5878, -4676, 5869, 4193,
             7138, 1829, 3892, 9805, 4309, 7684, 2764, -3692, -2015, 7323, 9914, 9518, -5871, -1145, 4967, 3218, 2722,
             2171, 468, 6481, -4894, 7818, 7075, 7508, 8711, 4311, -482, -8195, 2131, 7477, 5689, 4311]
    }
    total_error = 0.0

    for input_set, expected_output in zip(test_data["inputs"], test_data["expected_outputs"]):
        interpreter = MiniLangInterpreter(input_data=input_set, max_loop_iterations=1000, max_execution_time=3)
        interpreter.execute_program(program)
        output = interpreter.output_buffer

        length_score = evaluate_output_length(output, desired_length=1)
        total_error += (1.0 - length_score) * 10

        if output:
            actual_output = float(output[-1])
            expected_output = float(expected_output)
            total_error += abs(actual_output - expected_output)
        else:
            total_error += float('inf')

    return 1.0 / (1.0 + total_error)


def fitness_1_4_A(program):
    """
    Zadanie 1.4.A:
    Program powinien odczytać dziesięć pierwszych liczb z wejścia i zwrócić na wyjściu (jedynie) ich średnią arytmetyczną (zaokrągloną do pełnej liczby całkowitej).
    Na wejściu mogą być tylko całkowite liczby w zakresie [-99,99].
    """
    test_data = {
        "inputs":
            [{"var_0": 18, "var_1": -52, "var_2": 12, "var_3": 15, "var_4": -49, "var_5": 29, "var_6": 45, "var_7": 24,
              "var_8": -62, "var_9": 97},
             {"var_0": 8, "var_1": -86, "var_2": 93, "var_3": 35, "var_4": 84, "var_5": 74, "var_6": 79, "var_7": -86,
              "var_8": 11, "var_9": -66},
             {"var_0": 52, "var_1": -25, "var_2": -80, "var_3": 39, "var_4": 60, "var_5": 80, "var_6": 79, "var_7": -67,
              "var_8": 5, "var_9": -35},
             {"var_0": 31, "var_1": 4, "var_2": 2, "var_3": -48, "var_4": 19, "var_5": 13, "var_6": 7, "var_7": -49,
              "var_8": 45, "var_9": -82},
             {"var_0": 22, "var_1": -33, "var_2": -79, "var_3": -21, "var_4": -94, "var_5": 66, "var_6": -30,
              "var_7": 90, "var_8": -87, "var_9": 60},
             {"var_0": -64, "var_1": -89, "var_2": -3, "var_3": 7, "var_4": 71, "var_5": -31, "var_6": 1, "var_7": 32,
              "var_8": -70, "var_9": 87},
             {"var_0": -91, "var_1": -21, "var_2": 21, "var_3": 14, "var_4": -38, "var_5": -64, "var_6": 2, "var_7": 89,
              "var_8": 91, "var_9": 87},
             {"var_0": 49, "var_1": 43, "var_2": -23, "var_3": 87, "var_4": -90, "var_5": 1, "var_6": 45, "var_7": -19,
              "var_8": -82, "var_9": 64},
             {"var_0": 57, "var_1": -73, "var_2": 52, "var_3": 48, "var_4": -42, "var_5": -27, "var_6": -43,
              "var_7": -35, "var_8": -9, "var_9": 88},
             {"var_0": -57, "var_1": -61, "var_2": -93, "var_3": 39, "var_4": -15, "var_5": 82, "var_6": -88,
              "var_7": -19, "var_8": 11, "var_9": -71},
             {"var_0": -14, "var_1": 97, "var_2": -84, "var_3": 7, "var_4": 88, "var_5": 72, "var_6": -29, "var_7": -80,
              "var_8": -41, "var_9": 65},
             {"var_0": 75, "var_1": -32, "var_2": -3, "var_3": -74, "var_4": 19, "var_5": -9, "var_6": 10, "var_7": -72,
              "var_8": 20, "var_9": -67},
             {"var_0": -29, "var_1": 8, "var_2": -58, "var_3": -56, "var_4": 52, "var_5": 85, "var_6": -39, "var_7": 84,
              "var_8": -75, "var_9": -14},
             {"var_0": 78, "var_1": -14, "var_2": 30, "var_3": 52, "var_4": -91, "var_5": -18, "var_6": 9, "var_7": -76,
              "var_8": 84, "var_9": 14},
             {"var_0": -15, "var_1": -81, "var_2": 64, "var_3": -87, "var_4": -18, "var_5": -63, "var_6": -64,
              "var_7": 48, "var_8": -75, "var_9": -95},
             {"var_0": 2, "var_1": -75, "var_2": 20, "var_3": -1, "var_4": -31, "var_5": 71, "var_6": -91, "var_7": 52,
              "var_8": -69, "var_9": 82},
             {"var_0": -81, "var_1": -19, "var_2": -8, "var_3": 51, "var_4": 52, "var_5": -51, "var_6": 97,
              "var_7": -29, "var_8": 42, "var_9": 62},
             {"var_0": -38, "var_1": -72, "var_2": -88, "var_3": -42, "var_4": -79, "var_5": 59, "var_6": 1,
              "var_7": -33, "var_8": 47, "var_9": -2},
             {"var_0": 94, "var_1": -1, "var_2": -19, "var_3": 8, "var_4": 41, "var_5": 35, "var_6": 48, "var_7": -1,
              "var_8": 97, "var_9": -12},
             {"var_0": 0, "var_1": 91, "var_2": -40, "var_3": -71, "var_4": -73, "var_5": 75, "var_6": -61,
              "var_7": -70, "var_8": 65, "var_9": 42},
             {"var_0": -45, "var_1": 79, "var_2": 5, "var_3": -37, "var_4": -25, "var_5": 54, "var_6": -11,
              "var_7": -18, "var_8": 63, "var_9": 83},
             {"var_0": 80, "var_1": 45, "var_2": -56, "var_3": 53, "var_4": 19, "var_5": 70, "var_6": 17, "var_7": -41,
              "var_8": -36, "var_9": -27},
             {"var_0": -42, "var_1": -6, "var_2": 83, "var_3": -19, "var_4": -9, "var_5": 42, "var_6": 82, "var_7": 52,
              "var_8": -2, "var_9": 4},
             {"var_0": 93, "var_1": 34, "var_2": 42, "var_3": 35, "var_4": -25, "var_5": 80, "var_6": -37, "var_7": -31,
              "var_8": 20, "var_9": 46},
             {"var_0": -27, "var_1": -90, "var_2": 63, "var_3": -99, "var_4": -62, "var_5": -48, "var_6": 61,
              "var_7": -53, "var_8": -89, "var_9": 28},
             {"var_0": -31, "var_1": -39, "var_2": 62, "var_3": 80, "var_4": -78, "var_5": 18, "var_6": 71, "var_7": 63,
              "var_8": -61, "var_9": 27},
             {"var_0": 51, "var_1": -89, "var_2": 14, "var_3": -70, "var_4": -95, "var_5": -74, "var_6": 70,
              "var_7": 28, "var_8": 26, "var_9": -69},
             {"var_0": 99, "var_1": -40, "var_2": -9, "var_3": -86, "var_4": -40, "var_5": 33, "var_6": -49,
              "var_7": 17, "var_8": 27, "var_9": 36},
             {"var_0": 99, "var_1": -47, "var_2": -49, "var_3": -8, "var_4": -94, "var_5": 54, "var_6": -11,
              "var_7": -20, "var_8": -18, "var_9": -70},
             {"var_0": -59, "var_1": 68, "var_2": 15, "var_3": 23, "var_4": -48, "var_5": 86, "var_6": -54,
              "var_7": -61, "var_8": -10, "var_9": -55},
             {"var_0": -85, "var_1": 56, "var_2": -62, "var_3": 15, "var_4": 34, "var_5": 23, "var_6": 65, "var_7": 48,
              "var_8": 1, "var_9": -76},
             {"var_0": 68, "var_1": -8, "var_2": 58, "var_3": -71, "var_4": 37, "var_5": -20, "var_6": 6, "var_7": 84,
              "var_8": -80, "var_9": -52},
             {"var_0": -72, "var_1": 59, "var_2": -28, "var_3": -25, "var_4": -63, "var_5": 4, "var_6": -3,
              "var_7": -65, "var_8": -46, "var_9": 25},
             {"var_0": 14, "var_1": -48, "var_2": 5, "var_3": -35, "var_4": -30, "var_5": 46, "var_6": 21, "var_7": 10,
              "var_8": -89, "var_9": 50},
             {"var_0": -30, "var_1": 67, "var_2": -18, "var_3": -21, "var_4": 30, "var_5": -71, "var_6": 22, "var_7": 9,
              "var_8": -58, "var_9": 30},
             {"var_0": 35, "var_1": -91, "var_2": 84, "var_3": 52, "var_4": -46, "var_5": -90, "var_6": -63,
              "var_7": 83, "var_8": -24, "var_9": 61},
             {"var_0": -45, "var_1": -20, "var_2": 56, "var_3": 75, "var_4": 22, "var_5": -21, "var_6": 78, "var_7": 4,
              "var_8": 74, "var_9": -98},
             {"var_0": -43, "var_1": -72, "var_2": 12, "var_3": -49, "var_4": 9, "var_5": 94, "var_6": 5, "var_7": -79,
              "var_8": 37, "var_9": -87},
             {"var_0": -49, "var_1": 40, "var_2": -10, "var_3": -29, "var_4": -40, "var_5": 7, "var_6": -23,
              "var_7": 78, "var_8": -17, "var_9": -52},
             {"var_0": 26, "var_1": -61, "var_2": -98, "var_3": 32, "var_4": -7, "var_5": -40, "var_6": 29, "var_7": -4,
              "var_8": -50, "var_9": 41},
             {"var_0": -10, "var_1": -64, "var_2": -8, "var_3": -4, "var_4": 46, "var_5": -75, "var_6": 98, "var_7": -8,
              "var_8": -8, "var_9": 42},
             {"var_0": -68, "var_1": -71, "var_2": -98, "var_3": 7, "var_4": 31, "var_5": 29, "var_6": 84, "var_7": -22,
              "var_8": -89, "var_9": -83},
             {"var_0": -69, "var_1": -24, "var_2": 23, "var_3": 83, "var_4": -25, "var_5": -62, "var_6": 52,
              "var_7": 40, "var_8": 19, "var_9": 93},
             {"var_0": -95, "var_1": 74, "var_2": 96, "var_3": 84, "var_4": -89, "var_5": 9, "var_6": 92, "var_7": 95,
              "var_8": 78, "var_9": 34},
             {"var_0": 63, "var_1": 23, "var_2": -39, "var_3": -28, "var_4": 15, "var_5": -49, "var_6": 21, "var_7": 9,
              "var_8": -35, "var_9": -4},
             {"var_0": 24, "var_1": 37, "var_2": -20, "var_3": -46, "var_4": -68, "var_5": -79, "var_6": -93,
              "var_7": 84, "var_8": 54, "var_9": 74},
             {"var_0": -89, "var_1": -93, "var_2": 11, "var_3": -47, "var_4": 76, "var_5": -29, "var_6": -44,
              "var_7": -8, "var_8": 82, "var_9": 86},
             {"var_0": -88, "var_1": -59, "var_2": -69, "var_3": -72, "var_4": -66, "var_5": -66, "var_6": 19,
              "var_7": 25, "var_8": -25, "var_9": 80},
             {"var_0": -67, "var_1": 18, "var_2": -89, "var_3": -82, "var_4": -13, "var_5": 34, "var_6": -65,
              "var_7": -32, "var_8": -76, "var_9": -19},
             {"var_0": 55, "var_1": 58, "var_2": -42, "var_3": 26, "var_4": -65, "var_5": -65, "var_6": -48,
              "var_7": -50, "var_8": -69, "var_9": 67},
             {"var_0": 21, "var_1": 57, "var_2": -71, "var_3": 1, "var_4": -39, "var_5": -35, "var_6": 77, "var_7": -77,
              "var_8": 85, "var_9": -99},
             {"var_0": -59, "var_1": 44, "var_2": -17, "var_3": -47, "var_4": -73, "var_5": -11, "var_6": 8,
              "var_7": 44, "var_8": 98, "var_9": 60},
             {"var_0": -20, "var_1": -63, "var_2": 9, "var_3": 11, "var_4": -98, "var_5": 13, "var_6": 46, "var_7": -62,
              "var_8": 83, "var_9": -36},
             {"var_0": 94, "var_1": 11, "var_2": -43, "var_3": -4, "var_4": -68, "var_5": -93, "var_6": -49,
              "var_7": -58, "var_8": 79, "var_9": 45},
             {"var_0": 87, "var_1": -84, "var_2": -55, "var_3": 63, "var_4": -86, "var_5": 49, "var_6": 36, "var_7": 50,
              "var_8": 38, "var_9": -16},
             {"var_0": -65, "var_1": 19, "var_2": -34, "var_3": -9, "var_4": 55, "var_5": 50, "var_6": -95, "var_7": 0,
              "var_8": -11, "var_9": -49},
             {"var_0": -33, "var_1": -45, "var_2": 43, "var_3": 6, "var_4": 21, "var_5": 74, "var_6": 93, "var_7": 24,
              "var_8": 59, "var_9": -86},
             {"var_0": 41, "var_1": 71, "var_2": -50, "var_3": 0, "var_4": 41, "var_5": -7, "var_6": 83, "var_7": -65,
              "var_8": 48, "var_9": -33},
             {"var_0": 26, "var_1": -6, "var_2": -49, "var_3": 25, "var_4": -32, "var_5": 52, "var_6": 14, "var_7": -30,
              "var_8": 15, "var_9": 43},
             {"var_0": -28, "var_1": -18, "var_2": -26, "var_3": -72, "var_4": -99, "var_5": -48, "var_6": -12,
              "var_7": -73, "var_8": -4, "var_9": -51},
             {"var_0": -36, "var_1": -8, "var_2": -13, "var_3": 48, "var_4": 98, "var_5": -28, "var_6": 39, "var_7": 53,
              "var_8": 14, "var_9": -50},
             {"var_0": 76, "var_1": 40, "var_2": -33, "var_3": 68, "var_4": 41, "var_5": -62, "var_6": 28, "var_7": -28,
              "var_8": 80, "var_9": -30},
             {"var_0": -19, "var_1": -43, "var_2": -65, "var_3": 57, "var_4": 69, "var_5": -88, "var_6": 88,
              "var_7": -68, "var_8": 68, "var_9": 54},
             {"var_0": -60, "var_1": -67, "var_2": 40, "var_3": -68, "var_4": 20, "var_5": 96, "var_6": 89, "var_7": 34,
              "var_8": 35, "var_9": 75},
             {"var_0": -29, "var_1": 88, "var_2": 58, "var_3": 66, "var_4": 90, "var_5": 91, "var_6": -19, "var_7": 21,
              "var_8": -24, "var_9": 67},
             {"var_0": 78, "var_1": 78, "var_2": -98, "var_3": 42, "var_4": -38, "var_5": -7, "var_6": -42,
              "var_7": -49, "var_8": 61, "var_9": 59},
             {"var_0": 3, "var_1": -61, "var_2": -57, "var_3": -5, "var_4": -34, "var_5": 92, "var_6": 0, "var_7": 97,
              "var_8": -7, "var_9": -4},
             {"var_0": 3, "var_1": -19, "var_2": 47, "var_3": -17, "var_4": -68, "var_5": 41, "var_6": 78, "var_7": -8,
              "var_8": 62, "var_9": 9},
             {"var_0": -16, "var_1": -57, "var_2": 76, "var_3": -58, "var_4": -37, "var_5": 91, "var_6": 83,
              "var_7": -71, "var_8": 68, "var_9": -24},
             {"var_0": -62, "var_1": -70, "var_2": 84, "var_3": -38, "var_4": 48, "var_5": -92, "var_6": 78,
              "var_7": -28, "var_8": 18, "var_9": -22},
             {"var_0": -58, "var_1": 34, "var_2": -48, "var_3": 36, "var_4": -12, "var_5": 10, "var_6": 82, "var_7": 50,
              "var_8": 95, "var_9": -97},
             {"var_0": -41, "var_1": 64, "var_2": 21, "var_3": -7, "var_4": -75, "var_5": 77, "var_6": 25, "var_7": -88,
              "var_8": -13, "var_9": 75},
             {"var_0": -49, "var_1": -37, "var_2": -97, "var_3": 40, "var_4": 21, "var_5": 10, "var_6": -29,
              "var_7": 28, "var_8": 5, "var_9": -58},
             {"var_0": 64, "var_1": 87, "var_2": 24, "var_3": -96, "var_4": -75, "var_5": 44, "var_6": 47, "var_7": -14,
              "var_8": -79, "var_9": 77},
             {"var_0": -6, "var_1": 39, "var_2": 64, "var_3": 49, "var_4": 14, "var_5": -87, "var_6": 53, "var_7": 95,
              "var_8": 21, "var_9": -63},
             {"var_0": 94, "var_1": -34, "var_2": 14, "var_3": 34, "var_4": 17, "var_5": 88, "var_6": 28, "var_7": -9,
              "var_8": -19, "var_9": -35},
             {"var_0": -12, "var_1": 46, "var_2": -49, "var_3": 96, "var_4": 54, "var_5": -55, "var_6": -86,
              "var_7": -69, "var_8": -67, "var_9": 29},
             {"var_0": 50, "var_1": -56, "var_2": -54, "var_3": 28, "var_4": -73, "var_5": 25, "var_6": -98,
              "var_7": 95, "var_8": 73, "var_9": 36},
             {"var_0": -91, "var_1": -68, "var_2": 81, "var_3": 27, "var_4": 5, "var_5": 41, "var_6": -9, "var_7": 64,
              "var_8": 51, "var_9": -6},
             {"var_0": 3, "var_1": 86, "var_2": -57, "var_3": 17, "var_4": -40, "var_5": -39, "var_6": -30, "var_7": 9,
              "var_8": 48, "var_9": -96},
             {"var_0": -32, "var_1": 35, "var_2": -87, "var_3": -1, "var_4": 33, "var_5": 90, "var_6": 52, "var_7": 72,
              "var_8": -37, "var_9": 37},
             {"var_0": 73, "var_1": 97, "var_2": 30, "var_3": 48, "var_4": -29, "var_5": -30, "var_6": 35, "var_7": 60,
              "var_8": -80, "var_9": -96},
             {"var_0": 54, "var_1": -92, "var_2": 71, "var_3": -23, "var_4": -44, "var_5": 85, "var_6": -2,
              "var_7": -34, "var_8": 40, "var_9": 15},
             {"var_0": 45, "var_1": -34, "var_2": 69, "var_3": -7, "var_4": -26, "var_5": 12, "var_6": -55, "var_7": 20,
              "var_8": 73, "var_9": 23},
             {"var_0": -48, "var_1": 19, "var_2": -42, "var_3": -10, "var_4": 29, "var_5": -68, "var_6": -95,
              "var_7": 98, "var_8": -8, "var_9": -23},
             {"var_0": 78, "var_1": -92, "var_2": 64, "var_3": -45, "var_4": -88, "var_5": 86, "var_6": -93,
              "var_7": 86, "var_8": -16, "var_9": 99},
             {"var_0": -47, "var_1": -12, "var_2": 99, "var_3": -41, "var_4": -79, "var_5": 25, "var_6": 69,
              "var_7": -84, "var_8": 85, "var_9": -84},
             {"var_0": -3, "var_1": 64, "var_2": 51, "var_3": 15, "var_4": -81, "var_5": -18, "var_6": 29, "var_7": 67,
              "var_8": 28, "var_9": -80},
             {"var_0": 75, "var_1": -74, "var_2": 38, "var_3": -33, "var_4": 51, "var_5": -95, "var_6": -99,
              "var_7": -51, "var_8": -92, "var_9": 7},
             {"var_0": -53, "var_1": 33, "var_2": 58, "var_3": -78, "var_4": -34, "var_5": -59, "var_6": -96,
              "var_7": -30, "var_8": 78, "var_9": 11},
             {"var_0": 29, "var_1": -44, "var_2": 22, "var_3": 53, "var_4": -80, "var_5": -57, "var_6": -70,
              "var_7": -10, "var_8": 95, "var_9": 67},
             {"var_0": 34, "var_1": -13, "var_2": -52, "var_3": -8, "var_4": -20, "var_5": -80, "var_6": -70,
              "var_7": 2, "var_8": -67, "var_9": -20},
             {"var_0": -64, "var_1": 82, "var_2": -28, "var_3": -33, "var_4": -33, "var_5": -35, "var_6": -82,
              "var_7": 78, "var_8": -16, "var_9": -59},
             {"var_0": 99, "var_1": 12, "var_2": 38, "var_3": -74, "var_4": -84, "var_5": -68, "var_6": 65, "var_7": 95,
              "var_8": 64, "var_9": -82},
             {"var_0": 3, "var_1": -32, "var_2": 54, "var_3": -34, "var_4": -85, "var_5": -19, "var_6": 88, "var_7": 25,
              "var_8": -41, "var_9": -56},
             {"var_0": 93, "var_1": -1, "var_2": -8, "var_3": 95, "var_4": 60, "var_5": 21, "var_6": -2, "var_7": 54,
              "var_8": -55, "var_9": -49},
             {"var_0": 34, "var_1": 87, "var_2": 74, "var_3": 43, "var_4": -5, "var_5": 81, "var_6": -87, "var_7": 58,
              "var_8": 55, "var_9": 91},
             {"var_0": -34, "var_1": 35, "var_2": -40, "var_3": -84, "var_4": 32, "var_5": 5, "var_6": 42, "var_7": 79,
              "var_8": -32, "var_9": 34},
             {"var_0": -71, "var_1": 90, "var_2": -67, "var_3": -5, "var_4": 45, "var_5": 13, "var_6": -85,
              "var_7": -89, "var_8": -51, "var_9": -16},
             {"var_0": 7, "var_1": 40, "var_2": -55, "var_3": -90, "var_4": -74, "var_5": 52, "var_6": -9, "var_7": -86,
              "var_8": -27, "var_9": 24}],
        "expected_outputs":
            [8, 15, 11, -6, -11, -6, 9, 8, 2, -27, 8, -13, -4, 7, -39, -4, 12, -25, 29, -4, 15, 12, 18, 26, -32, 11,
             -21, -1, -16, -10, 2, 2, -21, -6, -4, 0, 12, -17, -10, -13, 1, -28, 13, 38, -2, -3, -6, -32, -39, -13, -8,
             5, -12, -9, 8, -14, 16, 13, 6, -43, 12, 18, 5, 19, 41, 8, 2, 13, 6, -8, 9, 4, -17, 8, 18, 18, -11, 3, 10,
             -10, 16, 11, 7, 12, -15, 8, -7, 7, -27, -17, 0, -29, -19, 6, -10, 21, 43, 4, -24, -22]
    }
    total_error = 0.0

    for input_set, expected_output in zip(test_data["inputs"], test_data["expected_outputs"]):
        interpreter = MiniLangInterpreter(input_data=input_set, max_loop_iterations=1000, max_execution_time=3)
        interpreter.execute_program(program)
        output = interpreter.output_buffer

        length_score = evaluate_output_length(output, desired_length=1)
        total_error += (1.0 - length_score) * 10

        if output:
            actual_output = float(output[-1])
            expected_output = float(expected_output)
            total_error += abs(actual_output - expected_output)
        else:
            total_error += float('inf')

    return 1.0 / (1.0 + total_error)


def fitness_1_4_B(program):
    """
    Zadanie 1.4.B:
    Program powinien odczytać na początek z wejścia pierwszą liczbę (ma być to wartość nieujemna) a następnie tyle liczb (całkowitych) jaka jest wartość pierwszej odczytanej liczby i zwrócić na wyjściu (jedynie) ich średnią arytmetyczną zaokrągloną do pełnej liczby całkowitej (do średniej nie jest wliczana pierwsza odczytana liczba, która mówi z ilu liczb chcemy obliczyć średnią).
    Na wejściu mogą być tylko całkowite liczby w zakresie [-99,99], pierwsza liczba może być tylko w zakresie [0,99].
    """
    test_data = {
        "inputs":
            [{"var_0": 6, "var_1": -45, "var_2": -66, "var_3": -95, "var_4": -88, "var_5": -49, "var_6": -94},
             {"var_0": 10, "var_1": 56, "var_2": 81, "var_3": -34, "var_4": 15, "var_5": -20, "var_6": 2, "var_7": 65,
              "var_8": 17, "var_9": -51, "var_10": -6}, {"var_0": 2, "var_1": -85, "var_2": -22},
             {"var_0": 9, "var_1": -29, "var_2": -45, "var_3": 44, "var_4": 67, "var_5": 47, "var_6": -99, "var_7": 49,
              "var_8": -78, "var_9": -22}, {"var_0": 1, "var_1": -68}, {"var_0": 1, "var_1": 55},
             {"var_0": 10, "var_1": -66, "var_2": -52, "var_3": 1, "var_4": 27, "var_5": -49, "var_6": 74, "var_7": 90,
              "var_8": 95, "var_9": 17, "var_10": -73}, {"var_0": 2, "var_1": 6, "var_2": -51},
             {"var_0": 3, "var_1": 1, "var_2": -2, "var_3": -51},
             {"var_0": 10, "var_1": -25, "var_2": 29, "var_3": -83, "var_4": 30, "var_5": 65, "var_6": -32, "var_7": 33,
              "var_8": -66, "var_9": 76, "var_10": -1},
             {"var_0": 5, "var_1": -4, "var_2": 16, "var_3": 28, "var_4": 38, "var_5": -72},
             {"var_0": 2, "var_1": 5, "var_2": -39},
             {"var_0": 6, "var_1": -6, "var_2": -80, "var_3": -19, "var_4": 93, "var_5": -2, "var_6": -93},
             {"var_0": 3, "var_1": -23, "var_2": 42, "var_3": -44}, {"var_0": 2, "var_1": -25, "var_2": -34},
             {"var_0": 7, "var_1": -74, "var_2": 11, "var_3": -65, "var_4": -65, "var_5": 37, "var_6": -87, "var_7": 2},
             {"var_0": 7, "var_1": -86, "var_2": -9, "var_3": -79, "var_4": 30, "var_5": -49, "var_6": 2, "var_7": -59},
             {"var_0": 9, "var_1": -64, "var_2": 28, "var_3": 50, "var_4": -18, "var_5": -98, "var_6": -52, "var_7": -9,
              "var_8": 24, "var_9": 5}, {"var_0": 4, "var_1": -18, "var_2": 0, "var_3": -54, "var_4": -81},
             {"var_0": 1, "var_1": 69}, {"var_0": 5, "var_1": 49, "var_2": -89, "var_3": 56, "var_4": 42, "var_5": 16},
             {"var_0": 3, "var_1": -20, "var_2": -32, "var_3": 15},
             {"var_0": 4, "var_1": 76, "var_2": -44, "var_3": 35, "var_4": 31},
             {"var_0": 10, "var_1": 92, "var_2": 16, "var_3": -5, "var_4": -51, "var_5": -66, "var_6": -61,
              "var_7": -93, "var_8": 53, "var_9": -29, "var_10": 7},
             {"var_0": 5, "var_1": 2, "var_2": 72, "var_3": -89, "var_4": 52, "var_5": -56},
             {"var_0": 6, "var_1": 25, "var_2": 88, "var_3": 64, "var_4": 38, "var_5": 7, "var_6": -61},
             {"var_0": 3, "var_1": -43, "var_2": 36, "var_3": 56},
             {"var_0": 6, "var_1": -17, "var_2": -72, "var_3": 49, "var_4": -90, "var_5": 42, "var_6": 83},
             {"var_0": 8, "var_1": 64, "var_2": 63, "var_3": 48, "var_4": -54, "var_5": -40, "var_6": -79, "var_7": -31,
              "var_8": -63}, {"var_0": 6, "var_1": 3, "var_2": 56, "var_3": 56, "var_4": -64, "var_5": 64, "var_6": 6},
             {"var_0": 9, "var_1": -31, "var_2": -92, "var_3": 24, "var_4": -43, "var_5": -66, "var_6": -88,
              "var_7": 14, "var_8": 2, "var_9": -33},
             {"var_0": 9, "var_1": -19, "var_2": -90, "var_3": 22, "var_4": 5, "var_5": -53, "var_6": 35, "var_7": -53,
              "var_8": 70, "var_9": 62},
             {"var_0": 7, "var_1": 13, "var_2": -40, "var_3": -88, "var_4": 93, "var_5": -59, "var_6": -72,
              "var_7": 35},
             {"var_0": 9, "var_1": 46, "var_2": -95, "var_3": 66, "var_4": -13, "var_5": 16, "var_6": -63, "var_7": -98,
              "var_8": -35, "var_9": -5},
             {"var_0": 5, "var_1": 24, "var_2": -47, "var_3": 25, "var_4": 8, "var_5": -34},
             {"var_0": 8, "var_1": 30, "var_2": -19, "var_3": -60, "var_4": -43, "var_5": 93, "var_6": 51, "var_7": -40,
              "var_8": 31}, {"var_0": 5, "var_1": 23, "var_2": -35, "var_3": -1, "var_4": -92, "var_5": 38},
             {"var_0": 4, "var_1": -81, "var_2": 55, "var_3": -61, "var_4": 88},
             {"var_0": 8, "var_1": 8, "var_2": -81, "var_3": 31, "var_4": 34, "var_5": -57, "var_6": -28, "var_7": 43,
              "var_8": 93},
             {"var_0": 7, "var_1": -62, "var_2": 6, "var_3": 72, "var_4": 1, "var_5": 55, "var_6": -64, "var_7": 1},
             {"var_0": 8, "var_1": 33, "var_2": 15, "var_3": -15, "var_4": 95, "var_5": -71, "var_6": 82, "var_7": 25,
              "var_8": 88}, {"var_0": 2, "var_1": -81, "var_2": 79},
             {"var_0": 10, "var_1": -68, "var_2": -18, "var_3": -88, "var_4": 13, "var_5": 95, "var_6": -95,
              "var_7": 28, "var_8": 17, "var_9": -66, "var_10": -74}, {"var_0": 2, "var_1": 88, "var_2": -70},
             {"var_0": 3, "var_1": 4, "var_2": 77, "var_3": -61}, {"var_0": 1, "var_1": 99},
             {"var_0": 3, "var_1": -85, "var_2": -75, "var_3": 76},
             {"var_0": 4, "var_1": -75, "var_2": -32, "var_3": -5, "var_4": -71},
             {"var_0": 7, "var_1": 83, "var_2": 8, "var_3": 62, "var_4": 64, "var_5": -17, "var_6": 83, "var_7": -68},
             {"var_0": 9, "var_1": -98, "var_2": -45, "var_3": -43, "var_4": -23, "var_5": -68, "var_6": -23,
              "var_7": -46, "var_8": 80, "var_9": -19},
             {"var_0": 7, "var_1": 12, "var_2": 16, "var_3": 14, "var_4": 51, "var_5": -29, "var_6": 1, "var_7": 94},
             {"var_0": 10, "var_1": -70, "var_2": -32, "var_3": 54, "var_4": 63, "var_5": -43, "var_6": -64,
              "var_7": 24, "var_8": -22, "var_9": 44, "var_10": -77}, {"var_0": 1, "var_1": -71},
             {"var_0": 5, "var_1": -87, "var_2": -16, "var_3": -51, "var_4": 56, "var_5": -7},
             {"var_0": 4, "var_1": -16, "var_2": 41, "var_3": -90, "var_4": 83},
             {"var_0": 5, "var_1": -67, "var_2": 57, "var_3": -93, "var_4": -17, "var_5": 85},
             {"var_0": 2, "var_1": -47, "var_2": -35},
             {"var_0": 6, "var_1": 17, "var_2": 68, "var_3": 73, "var_4": 54, "var_5": -73, "var_6": -28},
             {"var_0": 10, "var_1": -28, "var_2": 93, "var_3": -10, "var_4": -24, "var_5": 73, "var_6": 62,
              "var_7": -30, "var_8": -1, "var_9": -80, "var_10": -25},
             {"var_0": 7, "var_1": 69, "var_2": -93, "var_3": 97, "var_4": -26, "var_5": -25, "var_6": 66,
              "var_7": -60},
             {"var_0": 7, "var_1": 54, "var_2": -16, "var_3": -98, "var_4": -18, "var_5": 4, "var_6": -18,
              "var_7": -88},
             {"var_0": 6, "var_1": 65, "var_2": -38, "var_3": -75, "var_4": -17, "var_5": -44, "var_6": 75},
             {"var_0": 10, "var_1": 12, "var_2": -88, "var_3": 0, "var_4": 93, "var_5": 61, "var_6": -1, "var_7": -89,
              "var_8": -35, "var_9": -84, "var_10": 30},
             {"var_0": 9, "var_1": -12, "var_2": 7, "var_3": -15, "var_4": 16, "var_5": 29, "var_6": -50, "var_7": 55,
              "var_8": -42, "var_9": -70},
             {"var_0": 9, "var_1": 90, "var_2": 37, "var_3": 85, "var_4": -25, "var_5": 25, "var_6": 79, "var_7": 23,
              "var_8": -32, "var_9": 37},
             {"var_0": 8, "var_1": -50, "var_2": -77, "var_3": 53, "var_4": 96, "var_5": -66, "var_6": 23, "var_7": 49,
              "var_8": -49},
             {"var_0": 6, "var_1": -65, "var_2": 58, "var_3": 29, "var_4": -32, "var_5": 59, "var_6": -81},
             {"var_0": 2, "var_1": 56, "var_2": -47}, {"var_0": 4, "var_1": 2, "var_2": 30, "var_3": 13, "var_4": -76},
             {"var_0": 5, "var_1": 66, "var_2": -40, "var_3": 55, "var_4": 11, "var_5": -46},
             {"var_0": 10, "var_1": 43, "var_2": -61, "var_3": 28, "var_4": 46, "var_5": -78, "var_6": -76, "var_7": 9,
              "var_8": 96, "var_9": 99, "var_10": -29}, {"var_0": 1, "var_1": -72},
             {"var_0": 7, "var_1": -57, "var_2": -98, "var_3": 53, "var_4": 98, "var_5": -24, "var_6": 96,
              "var_7": -22},
             {"var_0": 10, "var_1": 2, "var_2": 77, "var_3": -88, "var_4": -60, "var_5": -90, "var_6": 11, "var_7": 51,
              "var_8": 96, "var_9": 3, "var_10": 98},
             {"var_0": 9, "var_1": 95, "var_2": -68, "var_3": -53, "var_4": -7, "var_5": -63, "var_6": 57, "var_7": -22,
              "var_8": 44, "var_9": -30}, {"var_0": 2, "var_1": 67, "var_2": -60},
             {"var_0": 4, "var_1": -97, "var_2": 26, "var_3": -97, "var_4": 86},
             {"var_0": 7, "var_1": 83, "var_2": -44, "var_3": 24, "var_4": -60, "var_5": 50, "var_6": -67,
              "var_7": -99},
             {"var_0": 7, "var_1": 66, "var_2": 30, "var_3": 29, "var_4": -36, "var_5": -34, "var_6": 19, "var_7": 19},
             {"var_0": 9, "var_1": 9, "var_2": -37, "var_3": 9, "var_4": -44, "var_5": 87, "var_6": 47, "var_7": -94,
              "var_8": -92, "var_9": 25}, {"var_0": 4, "var_1": -8, "var_2": -1, "var_3": -24, "var_4": 30},
             {"var_0": 5, "var_1": 67, "var_2": 90, "var_3": 75, "var_4": 54, "var_5": 49},
             {"var_0": 4, "var_1": -97, "var_2": -97, "var_3": 79, "var_4": 59},
             {"var_0": 5, "var_1": 52, "var_2": 24, "var_3": -33, "var_4": -80, "var_5": 93},
             {"var_0": 9, "var_1": -94, "var_2": 55, "var_3": -86, "var_4": -4, "var_5": 46, "var_6": 19, "var_7": -80,
              "var_8": -89, "var_9": 99},
             {"var_0": 8, "var_1": -1, "var_2": -16, "var_3": 42, "var_4": -72, "var_5": 71, "var_6": 31, "var_7": -80,
              "var_8": 10},
             {"var_0": 9, "var_1": -61, "var_2": 13, "var_3": -79, "var_4": -79, "var_5": -8, "var_6": -62,
              "var_7": -40, "var_8": 97, "var_9": -38}, {"var_0": 3, "var_1": -12, "var_2": 16, "var_3": 15},
             {"var_0": 1, "var_1": -81},
             {"var_0": 6, "var_1": 26, "var_2": -83, "var_3": -71, "var_4": 77, "var_5": -51, "var_6": 30},
             {"var_0": 6, "var_1": 94, "var_2": 5, "var_3": 84, "var_4": 10, "var_5": 78, "var_6": 88},
             {"var_0": 1, "var_1": -67}, {"var_0": 4, "var_1": -72, "var_2": 27, "var_3": -67, "var_4": -83},
             {"var_0": 2, "var_1": -48, "var_2": -35},
             {"var_0": 4, "var_1": 26, "var_2": 83, "var_3": -82, "var_4": -65},
             {"var_0": 7, "var_1": -45, "var_2": 23, "var_3": 24, "var_4": 94, "var_5": -86, "var_6": -78, "var_7": 22},
             {"var_0": 1, "var_1": 65}, {"var_0": 3, "var_1": 30, "var_2": -85, "var_3": 88},
             {"var_0": 6, "var_1": -13, "var_2": -75, "var_3": 32, "var_4": 8, "var_5": 97, "var_6": -47},
             {"var_0": 4, "var_1": -69, "var_2": 36, "var_3": -99, "var_4": 76}],
        "expected_outputs":
            [-73, 12, -54, -7, -68, 55, 6, -22, -17, 3, 1, -17, -18, -8, -30, -34, -36, -15, -38, 69, 15, -12, 24, -14,
             -4, 27, 16, -1, -12, 20, -35, -2, -17, -20, -5, 5, -13, 0, 5, 1, 32, -1, -26, 9, 7, 99, -28, -46, 31, -32,
             23, -12, -71, -21, 4, -7, -41, 18, 3, 4, -26, -6, -10, -9, 35, -3, -5, 4, -8, 9, 8, -72, 7, 10, -5, 4, -20,
             -16, 13, -10, -1, 67, -14, 11, -15, -2, -29, 6, -81, -12, 60, -67, -49, -42, -10, -7, 65, 11, 0, -14]
    }
    total_error = 0.0

    for input_set, expected_output in zip(test_data["inputs"], test_data["expected_outputs"]):
        interpreter = MiniLangInterpreter(input_data=input_set, max_loop_iterations=1000, max_execution_time=3)
        interpreter.execute_program(program)
        output = interpreter.output_buffer

        length_score = evaluate_output_length(output, desired_length=1)
        total_error += (1.0 - length_score) * 10

        if output:
            actual_output = float(output[-1])
            expected_output = float(expected_output)
            total_error += abs(actual_output - expected_output)
        else:
            total_error += float('inf')

    return 1.0 / (1.0 + total_error)


def fitness_benchmark_1(program):
    """
    Given an integer and a float print their sum.
    """

    test_data = {
        "inputs":
            [{"var_0": -4, "var_1": -32.012}, {"var_0": 52, "var_1": -14.404}, {"var_0": -87, "var_1": -66.444},
             {"var_0": 8, "var_1": -43.848}, {"var_0": -44, "var_1": 94.786}, {"var_0": -79, "var_1": 35.984},
             {"var_0": 98, "var_1": -67.078}, {"var_0": -74, "var_1": 57.209}, {"var_0": -37, "var_1": -97.411},
             {"var_0": 52, "var_1": -54.434}, {"var_0": 82, "var_1": 65.636}, {"var_0": 85, "var_1": -71.472},
             {"var_0": 92, "var_1": -10.595}, {"var_0": -92, "var_1": 91.396}, {"var_0": -67, "var_1": 34.058},
             {"var_0": -69, "var_1": 4.25}, {"var_0": 41, "var_1": 81.323}, {"var_0": 46, "var_1": -93.858},
             {"var_0": 66, "var_1": -67.256}, {"var_0": 42, "var_1": -68.191}, {"var_0": -82, "var_1": 50.783},
             {"var_0": 31, "var_1": 58.968}, {"var_0": -29, "var_1": -88.425}, {"var_0": 61, "var_1": 45.035},
             {"var_0": 62, "var_1": -43.038}, {"var_0": 27, "var_1": 67.545}, {"var_0": 45, "var_1": -86.76},
             {"var_0": -24, "var_1": -66.259}, {"var_0": -82, "var_1": 75.46}, {"var_0": -96, "var_1": 10.262},
             {"var_0": 28, "var_1": 89.32}, {"var_0": -95, "var_1": -7.611}, {"var_0": 69, "var_1": 56.968},
             {"var_0": 14, "var_1": 81.77}, {"var_0": 9, "var_1": 12.391}, {"var_0": -79, "var_1": -75.341},
             {"var_0": 18, "var_1": 66.527}, {"var_0": 73, "var_1": -70.792}, {"var_0": -84, "var_1": -91.396},
             {"var_0": -65, "var_1": -44.878}, {"var_0": -1, "var_1": 75.469}, {"var_0": -33, "var_1": 58.801},
             {"var_0": -13, "var_1": -51.614}, {"var_0": 47, "var_1": 4.319}, {"var_0": -54, "var_1": -84.329},
             {"var_0": -32, "var_1": -76.014}, {"var_0": -24, "var_1": -23.459}, {"var_0": 83, "var_1": -96.339},
             {"var_0": 0, "var_1": 98.574}, {"var_0": -85, "var_1": 52.283}, {"var_0": 8, "var_1": -63.443},
             {"var_0": -18, "var_1": -39.084}, {"var_0": -26, "var_1": -13.176}, {"var_0": -47, "var_1": 54.136},
             {"var_0": -49, "var_1": -17.099}, {"var_0": 81, "var_1": 53.237}, {"var_0": 22, "var_1": -49.32},
             {"var_0": 6, "var_1": -26.457}, {"var_0": -10, "var_1": 88.662}, {"var_0": -56, "var_1": 52.015},
             {"var_0": -68, "var_1": -28.087}, {"var_0": -58, "var_1": -19.186}, {"var_0": -69, "var_1": -83.475},
             {"var_0": -41, "var_1": -46.967}, {"var_0": 64, "var_1": 40.133}, {"var_0": 55, "var_1": 54.92},
             {"var_0": -76, "var_1": 98.868}, {"var_0": -48, "var_1": -15.605}, {"var_0": -14, "var_1": -78.62},
             {"var_0": -75, "var_1": 3.179}, {"var_0": 2, "var_1": 22.404}, {"var_0": 0, "var_1": -72.429},
             {"var_0": -8, "var_1": 61.665}, {"var_0": 84, "var_1": -41.848}, {"var_0": -31, "var_1": 96.247},
             {"var_0": -68, "var_1": -28.793}, {"var_0": -98, "var_1": -21.662}, {"var_0": 40, "var_1": -11.068},
             {"var_0": -9, "var_1": -74.882}, {"var_0": -23, "var_1": 0.141}, {"var_0": -46, "var_1": -46.711},
             {"var_0": 89, "var_1": 65.931}, {"var_0": 65, "var_1": 93.522}, {"var_0": 24, "var_1": -27.423},
             {"var_0": -78, "var_1": 93.371}, {"var_0": 37, "var_1": 22.179}, {"var_0": -37, "var_1": 69.187},
             {"var_0": -56, "var_1": -54.281}, {"var_0": 31, "var_1": -12.86}, {"var_0": -89, "var_1": 94.527},
             {"var_0": -35, "var_1": 55.207}, {"var_0": 34, "var_1": 47.268}, {"var_0": 30, "var_1": 24.737},
             {"var_0": -15, "var_1": -85.172}, {"var_0": -48, "var_1": 47.612}, {"var_0": -66, "var_1": 67.806},
             {"var_0": 39, "var_1": 67.118}, {"var_0": 66, "var_1": -31.297}, {"var_0": -21, "var_1": 96.952},
             {"var_0": -30, "var_1": 38.336}],
        "expected_outputs":
            [-36.012, 37.596, -153.444, -35.848, 50.786, -43.016, 30.922, -16.791, -134.411, -2.434, 147.636, 13.528,
             81.405, -0.604, -32.942, -64.75, 122.323, -47.858, -1.256, -26.191, -31.217, 89.968, -117.425, 106.035,
             18.962, 94.545, -41.76, -90.259, -6.54, -85.738, 117.32, -102.611, 125.968, 95.77, 21.391, -154.341,
             84.527, 2.208, -175.396, -109.878, 74.469, 25.801, -64.614, 51.319, -138.329, -108.014, -47.459, -13.339,
             98.574, -32.717, -55.443, -57.084, -39.176, 7.136, -66.099, 134.237, -27.32, -20.457, 78.662, -3.985,
             -96.087, -77.186, -152.475, -87.967, 104.133, 109.92, 22.868, -63.605, -92.62, -71.821, 24.404, -72.429,
             53.665, 42.152, 65.247, -96.793, -119.662, 28.932, -83.882, -22.859, -92.711, 154.931, 158.522, -3.423,
             15.371, 59.179, 32.187, -110.281, 18.14, 5.527, 20.207, 81.268, 54.737, -100.172, -0.388, 1.806, 106.118,
             34.703, 75.952, 8.336]
    }
    total_error = 0.0

    for input_set, expected_output in zip(test_data["inputs"], test_data["expected_outputs"]):
        interpreter = MiniLangInterpreter(input_data=input_set, max_loop_iterations=1000, max_execution_time=3)
        interpreter.execute_program(program)
        output = interpreter.output_buffer

        length_score = evaluate_output_length(output, desired_length=1)
        total_error += (1.0 - length_score) * 10

        if output:
            actual_output = float(output[-1])
            total_error += abs(actual_output - expected_output)
        else:
            total_error += float('inf')

    return 1.0 / (1.0 + total_error)


def fitness_benchmark_17(program):
    """
    Given integer n (var_0), return on output the sum of squares of each integer in [1, n].
    That is sum_{i=1..n} i^2.
    Example:
      Input: 3   -> 1^2 + 2^2 + 3^2 = 14
      Input: 5   -> 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55
      If n <= 0, expected sum = 0.
    """
    test_data = {
        "inputs": [
            {"var_0": -5},
            {"var_0": -1},
            {"var_0": 0},
            {"var_0": 1},
            {"var_0": 2},
            {"var_0": 3},
            {"var_0": 5},
            {"var_0": 6},
            {"var_0": 10},
            {"var_0": 12},
            {"var_0": 15},
            {"var_0": 17},
            {"var_0": 20},
            {"var_0": 25},
            {"var_0": 30},
            {"var_0": 33},
            {"var_0": 50},
            {"var_0": 99},
            {"var_0": 100},
            {"var_0": 101},
        ],
        "expected_outputs": [
            0,  # n=-5  -> 0
            0,  # n=-1  -> 0
            0,  # n=0   -> 0
            1,  # 1^2
            5,  # 1^2+2^2=5
            14,  # 1^2+2^2+3^2=14
            55,  # do 5^2
            91,  # do 6^2
            385,  # do 10^2
            650,  # do 12^2
            1240,  # do 15^2
            1785,  # do 17^2
            2870,  # do 20^2
            5525,  # do 25^2
            9455,  # do 30^2
            12529,  # do 33^2
            42925,  # do 50^2
            328350,  # do 99^2
            338350,  # do 100^2
            348551,  # do 101^2
        ]
    }

    total_error = 0.0

    for input_set, expected_output in zip(test_data["inputs"], test_data["expected_outputs"]):
        interpreter = MiniLangInterpreter(input_data=input_set, max_loop_iterations=1000, max_execution_time=3)
        interpreter.execute_program(program)
        output = interpreter.output_buffer

        length_score = evaluate_output_length(output, desired_length=1)
        total_error += (1.0 - length_score) * 10

        if output:
            actual_output = float(output[-1])
            total_error += abs(actual_output - expected_output)
        else:
            total_error += float('inf')

    return 1.0 / (1.0 + total_error)


def fitness_benchmark_28(program):
    """
    Given 4 integers (var_0, var_1, var_2, var_3), the program should output only the smallest of them.
    Example:
      Input: (3, 7, 2, 5) -> 2
      Input: (10,15,5,20) -> 5
    """
    test_data = {
        "inputs": [
            {"var_0": 3, "var_1": 7, "var_2": 2, "var_3": 5},
            {"var_0": 10, "var_1": 15, "var_2": 5, "var_3": 20},
            {"var_0": -1, "var_1": -2, "var_2": -3, "var_3": -4},
            {"var_0": 0, "var_1": 0, "var_2": 0, "var_3": 0},
            {"var_0": 100, "var_1": 50, "var_2": 75, "var_3": 25},
            {"var_0": -5, "var_1": -5, "var_2": -5, "var_3": 2},
            {"var_0": 1, "var_1": 1, "var_2": 1, "var_3": 1},
            {"var_0": 99, "var_1": 99, "var_2": 0, "var_3": -1},
            {"var_0": -10, "var_1": 15, "var_2": -9, "var_3": -9},
            {"var_0": 30, "var_1": 30, "var_2": 29, "var_3": 30},
            {"var_0": 1, "var_1": -1, "var_2": 0, "var_3": 2},
            {"var_0": -7, "var_1": -7, "var_2": -10, "var_3": -10},
            {"var_0": 50, "var_1": 50, "var_2": 50, "var_3": 49},
            {"var_0": -20, "var_1": -19, "var_2": -5, "var_3": -19},
            {"var_0": 15, "var_1": 27, "var_2": 9, "var_3": 10},
            {"var_0": -100, "var_1": 100, "var_2": 99, "var_3": 98},
            {"var_0": 4, "var_1": 4, "var_2": 4, "var_3": 4},
            {"var_0": -50, "var_1": -51, "var_2": -49, "var_3": -50},
            {"var_0": 7, "var_1": 7, "var_2": -8, "var_3": 0},
            {"var_0": 999, "var_1": 1000, "var_2": 1001, "var_3": 998},
        ],
        "expected_outputs": [
            2,  # [3,7,2,5]
            5,  # [10,15,5,20]
            -4,  # [-1,-2,-3,-4]
            0,  # [0,0,0,0]
            25,  # [100,50,75,25]
            -5,  # [-5,-5,-5,2]
            1,  # [1,1,1,1]
            -1,  # [99,99,0,-1]
            -10,  # [-10,15,-9,-9] -> -10 is smallest
            29,  # [30,30,29,30]
            -1,  # [1,-1,0,2]
            -10,  # [-7,-7,-10,-10]
            49,  # [50,50,50,49]
            -20,  # [-20,-19,-5,-19] -> -20
            9,  # [15,27,9,10]
            -100,  # [-100,100,99,98]
            4,  # [4,4,4,4]
            -51,  # [-50,-51,-49,-50] -> -51
            -8,  # [7,7,-8,0]
            998,  # [999,1000,1001,998]
        ]
    }

    total_error = 0.0

    for input_set, expected_output in zip(test_data["inputs"], test_data["expected_outputs"]):
        interpreter = MiniLangInterpreter(input_data=input_set, max_loop_iterations=1000, max_execution_time=3)
        interpreter.execute_program(program)
        output = interpreter.output_buffer

        length_score = evaluate_output_length(output, desired_length=1)
        total_error += (1.0 - length_score) * 10

        if output:
            actual_output = float(output[-1])
            total_error += abs(actual_output - expected_output)
        else:
            total_error += float('inf')

    return 1.0 / (1.0 + total_error)


def fitness_symbolic_regression(program):
    """
    Przykład: sprawdzamy, czy program potrafi odwzorować funkcję XOR przy k=2:
      f(D0, D1) = D0 XOR D1
    W tym przypadku test_data zawiera wszystkie możliwe wejścia: (0,0), (0,1), (1,0), (1,1).
    Można zmienić te dane, jeśli chcemy testować inne funkcje (OR, AND, random itp.) lub większe k.
    """
    all_inputs = []
    all_outputs = []
    for i in range(64):
        bits = [(i >> b) & 1 for b in range(6)]  # b=0..5
        d0, d1, d2, d3, d4, d5 = bits
        all_inputs.append({
            "var_0": d0,
            "var_1": d1,
            "var_2": d2,
            "var_3": d3,
            "var_4": d4,
            "var_5": d5,
        })
        value = sum(bits) % 2
        all_outputs.append(value)

    test_data = {
        "inputs": all_inputs,
        "expected_outputs": all_outputs
    }

    total_error = 0.0

    for input_set, expected_output in zip(test_data["inputs"], test_data["expected_outputs"]):
        interpreter = MiniLangInterpreter(input_data=input_set, max_loop_iterations=1000, max_execution_time=3)
        interpreter.execute_program(program)
        output = interpreter.output_buffer

        length_score = evaluate_output_length(output, desired_length=1)
        total_error += (1.0 - length_score) * 10

        if output:
            actual_output = float(output[-1])
            total_error += abs(actual_output - expected_output)
        else:
            total_error += float('inf')

    return 1.0 / (1.0 + total_error)
