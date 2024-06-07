import sys
import csv

def main():
    check_file()
    students_data = ret_data()
    format_data(students_data)

def check_file():
    if len(sys.argv) == 3:
        return True
    elif len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too mant command-line arguments')

def ret_data():
    data_old = sys.argv[1]
    students = []

    try:
        with open(data_old) as file:
            data = csv.DictReader(file)
            for student in data:
                students.append({'full_name': student['name'],'house': student['house']})
            return students
    except FileNotFoundError:
        sys.exit('File does not exist')

def format_data(unparsed_data):
    data_new = sys.argv[2]

    with open(data_new,'w') as file:
        writer = csv.DictWriter(file,fieldnames = ['first','last','house'])
        writer.writeheader()
        for student in unparsed_data:
            last_name,first_name = student['full_name'].split(',')
            student_parsed = {'first':first_name.lstrip(),'last':last_name,'house':student['house']}
            writer.writerow(student_parsed)


if __name__ == "__main__":
    main()
