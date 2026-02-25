import os
import subprocess

TESTS_DIR = "test"
RESULTS_DIR = "results"
MINITRICE_PATH = "./minitrice"


def ensure_results_dir():
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)


def get_result_filename(test_filename):
    name, ext = os.path.splitext(test_filename)
    return f"{name}-result{ext}"


def process_file(test_file):
    input_path = os.path.join(TESTS_DIR, test_file)
    result_file = get_result_filename(test_file)
    output_path = os.path.join(RESULTS_DIR, result_file)

    with open(input_path, "r") as infile:
        try:
            result = subprocess.run(
                [MINITRICE_PATH],
                stdin=infile,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            with open(output_path, "w") as outfile:
                outfile.write(result.stdout)

            print(f"[OK] {test_file} -> {result_file}")

        except Exception as e:
            print(f"[ERROR] {test_file}: {e}")


def main():
    ensure_results_dir()

    for file in os.listdir(TESTS_DIR):
        if file.endswith(".txt"):
            process_file(file)


if __name__ == "__main__":
    main()