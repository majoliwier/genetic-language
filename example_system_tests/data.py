import json
import random


def generate_test_data(count, value_range, operation="multiply"):
    test_data = {"inputs": [], "expected_outputs": []}

    for _ in range(count):
        if operation == "average":
            var_0 = random.randint(1, 10)
            numbers = {"var_0": var_0}
            numbers.update({f"var_{i}": random.randint(*value_range) for i in range(1, var_0 + 1)})
            result = round(sum(value for key, value in numbers.items() if key != "var_0") / var_0)
            test_data["inputs"].append(numbers)
        else:
            var_0 = random.randint(*value_range)
            var_1 = round(random.uniform(*value_range), 3)

            if operation == "multiply":
                result = var_0 * var_1
            elif operation == "add":
                result = var_0 + var_1
                result = round(result, 3)
            elif operation == "subtract":
                result = var_0 - var_1
            elif operation == "bigger":
                result = var_0 if var_0 > var_1 else var_1

            test_data["inputs"].append({"var_0": var_0, "var_1": var_1})

        test_data["expected_outputs"].append(result)

    return json.dumps(test_data, separators=(",", ":"))


if __name__ == "__main__":
    count = 100
    value_range = (-99, 99)
    operation = "add"

    json_data = generate_test_data(count, value_range, operation)
    print(json_data)
