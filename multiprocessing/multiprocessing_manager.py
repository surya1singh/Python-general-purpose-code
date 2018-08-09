import multiprocessing

def print_records(records):
    p = multiprocessing.current_process()
    print(f'records in {p.name} : {records[:]}')

def insert_record(record, records):
    p = multiprocessing.current_process()
    records.append(record)
    print(f"New record added! by {p.name}")

if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        p = multiprocessing.current_process()
        records = manager.list([('Sam', 10), ('Adam', 9), ('Kevin',9)]) # try other object like dictionaries, Queue, Value, Array etc
        new_record = ('Jeff', 8)
        print(f'records initially in {p.name} : {records[:]}')
        p1 = multiprocessing.Process(target=insert_record, args=(new_record, records))
        p2 = multiprocessing.Process(target=print_records, args=(records,))

        p1.start()
        p1.join()

        p2.start()
        p2.join()
