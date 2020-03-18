file_name = 'data.txt'

def prep_record(line):
    line = line.split(':')
    first_name, last_name = line[0].split(',')
    course_detail = line[1].rstrip().split(',')
    return first_name, last_name, course_detail

def prep_to_write(first_name, last_name, courses):
    full_name = first_name+','+last_name
    courses = ','.join(courses)
    return full_name+','+courses

with open(file_name) as f:
    for line in f:
        print(line.strip())
        first_name, last_name, course_detail = prep_record(line)
        print(first_name, last_name, course_detail)

to_write = prep_to_write(first_name, last_name, course_detail)
print(to_write)
record_to_add = 'evgeny, doe:java, ruby, javascript'

# with open(file_name, "a+") as to_write: # a+: append, r:read, w:write
#    to_write.write(record_to_add+"\n")

#file_name = 'data.txt'
mashrur = Student('mashrur', 'hossain', ['python', 'ruby', 'javascript'])
print(mashrur.find_in_file(file_name))
#print(mashrur.add_to_file(file_name))
#joe = Student('joe', 'schmp', ['python', 'ruby', 'javascript'])
#print(joe.find_in_file(file_name))
#print(joe.add_to_file(file_name))
