import json
import sys

def fill_values(tests, values_dict):
    
    for test in tests:
        test_id = test.get("id")
        if test_id in values_dict:
            test["value"] = values_dict[test_id]
        
        if "values" in test:
            test["values"] = fill_values(test["values"], values_dict)
    return tests


def main(tests_path, values_path, report_path):
    
    try:
        with open(tests_path, "r") as f:
            tests_data = json.load(f)

        with open(values_path, "r") as f:
            values_data = json.load(f)

    except FileNotFoundError as e:
        print(f"Error: File not found: {e.filename}")
        return
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in file: {e.doc}")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return


    values_dict = {item["id"]: item["value"] for item in values_data["values"]}

    filled_tests = fill_values(tests_data["tests"], values_dict)

    try:
        with open(report_path, "w") as f:
            json.dump(tests_data, f, indent=2)
    except Exception as e:
        print(f"Error writing to report file: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <tests_path> <values_path> <report_path>")
    else:
        tests_path = sys.argv[1]
        values_path = sys.argv[2]
        report_path = sys.argv[3]
        main(tests_path, values_path, report_path)
