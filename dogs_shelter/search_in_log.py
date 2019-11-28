def main(path):

    with open(path, mode='r') as file:
        lines = file.readlines()

        amount = 0
        for raw_index in range(len(lines)):

            row_data = lines[raw_index].split('\t')
            current_amount = int(row_data[3])
            if current_amount > amount:
                amount = current_amount
                raw = row_data


        print(raw[3], raw[4], raw[5])


if __name__ == '__main__':

    # path = 'C:\Users\Panov\Desktop\neurotrend log.txt'
    path = input('Enter log file path: ')
    main(path)
