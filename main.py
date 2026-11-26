LINE = "Exceeds expectations in turning five-minute tasks into week-long sagas, and somehow still gets promoted before the rest of us."

import os


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
