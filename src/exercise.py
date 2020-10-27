import csv
def main():
    file = input("filename:")

    records = read_records_from_file(file)
    print("persons: " + str(len(records)))
    print("persons:")
    for person in records:
        print(person)

def read_records_from_file(file):
    records = []
    # write here the code for reading from file
    # and printing the read records
    # person = Person("name",2)
    # print(person)
    try:
      with open(file) as f:
        reader = csv.reader(f,delimiter=',')
        for person in reader:
          name = person[0]
          age= int(person[1])
          records.append(name)
        
    except:
      print("Something went wrong opening the file")
    
    print(records)

    return records


if __name__ == '__main__':
    from person import Person
    main()
else:
    from src.person import Person