import sys

import pycheck

CHECK_CASES = [
    [["🟢"], "🟠"],
    [["🟠"], "🔴"],
    [["🔴"], "🟢"],
]


def run(color: str) -> str:
    # TU CÓDIGO AQUÍ
    match color:
        case "🟢":
            new_color = "🟠"
        case "🟠":
            new_color = "🔴"
        case "🔴":
            new_color = "🟢"
        case _:
            print("Este semáforo es raro")
    return new_color


if __name__ == "__main__":
    pycheck.check(run, CHECK_CASES, sys.argv)
