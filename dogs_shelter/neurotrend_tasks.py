import os

def file_generator(file_path, stimuls):

    stimul_index = 0

    with  open(file_path, mode='r', encoding='utf-8') as file:

        sliced_event = list()
        while stimul_index < len(stimuls):

            if not stimuls[stimul_index]['tech']:
                stimul_index += 1
                continue

            stimul_name = stimuls[stimul_index]['name']
            stimul_duration = stimuls[stimul_index]['length']
            lines_to_write = list()

            events_total_duration = 0
            while events_total_duration < stimul_duration:

                if len(sliced_event):
                    event = sliced_event.copy()

                else:
                    line = file.readline()

                    if line == '':
                        break
                    else:
                        event = line.split()

                event_duration = int(event[5])
                if (events_total_duration + event_duration) > stimul_duration:
                    event_end_new = int(event[3]) + (stimul_duration - events_total_duration)

                    sliced_event = event.copy()
                    sliced_event[3] = str(event_end_new)
                    sliced_event[5] = str(int(sliced_event[4]) - int(sliced_event[3]))

                    event[4] = str(event_end_new)
                    event[5] = str(int(event[4]) - int(event[3]))

                    event_duration = int(event[5])

                elif len(sliced_event):
                    sliced_event.clear()

                events_total_duration += event_duration
                lines_to_write.append(' '.join(event) + '\n')

            if len(lines_to_write):
                create_file(stimul_name, lines_to_write)

            yield

            stimul_index += 1

def create_file(name, lines):

    file_path = os.path.join(os.getcwd(), name + '.txt')

    with  open(file_path, mode='w', encoding='utf-8') as file:
        file.writelines(lines)

if __name__ == '__main__':

    stimuls = [
        {'name' : 'Stimul1', 'num': 1, 'length': 15, 'tech': False},
        {'name': 'Stimul2', 'num': 2, 'length': 25, 'tech': True},
        {'name': 'Stimul3', 'num': 3, 'length': 20, 'tech': False}
    ]
    path = os.path.join(os.getcwd(), 'neurotrend_input.txt')

    for g in file_generator(path, stimuls):
        pass