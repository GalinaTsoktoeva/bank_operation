from utils.util import download_data, refactor_string
from datetime import datetime

def main():
    count_str = 0
    result = ""
    filename = "utils/operations.json"
    data = download_data(filename)

    for item in range(len(data)):

        try:
            str = refactor_string(data[item])
            if str:
                print()
                str = ""

            if count_str == 5:
                break
            count_str += 1
        except:
            pass



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

