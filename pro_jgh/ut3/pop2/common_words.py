# *************************
# BUSCANDO PALABRAS COMUNES
# *************************
import filecmp
from pathlib import Path


def run(input_path: Path) -> bool:
    output_path = "data/common_words/output.txt"
    # TU CÓDIGO AQUÍ
    with open(input_path, "r") as f:
        data_rows = f.readlines()
    matches = []
    for data_row1 in data_rows:
        words1 = set(data_row1.strip().lower().split())
        for data_row2 in data_rows:
            words2 = set(data_row2.strip().lower().split())
            match_count = len(words1 & words2)
            matches.append(f"{match_count}\n")
    with open(output_path, "w") as f:
        f.writelines(matches)
    return filecmp.cmp(output_path, "data/common_words/.expected", shallow=False)


if __name__ == "__main__":
    run("data/common_words/minizen.txt")
