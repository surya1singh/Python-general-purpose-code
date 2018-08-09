import multiprocessing

def print_records(records):
    print('records : {records[:]}')

def insert_record(record, records):
    records.append(record)
    print("New record added!")

if __name__ == '__main__':
    with multiprocessing.Manager() as manager:

        records = manager.list([('Sam', 10), ('Adam', 9), ('Kevin',9)]) # try other object like dictionaries, Queue, Value, Array etc
        new_record = ('Jeff', 8)

        p1 = multiprocessing.Process(target=insert_record, args=(new_record, records))
        p2 = multiprocessing.Process(target=print_records, args=(records,))

        p1.start()
        p1.join()

        p2.start()
        p2.join()
