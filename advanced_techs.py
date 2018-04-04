''' template '''
from string import Template

import argparse

'''$ is used to denote a placeholder in template_mod
    We can provide ur own template as following
class my_template(Template):
    delimiter = "&" # replace & with whatever you like

    '''
def template_mod():
    student = []
    student.append({"name": "Long", "GPA": "4.0"})
    student.append({"name": "Wu", "GPA": "2.5"})
    student.append({"name": "Dee", "GPA": "3"})
    student.append({"name": "To", "GPA": "-2"})

    t = Template("$name with $GPA with $dick")
    for st in student:
        print(t.safe_substitute(st))
    return student

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", help = "Long-winded curse",\
    action = "store_true")
    group.add_argument("-q", "--quiet", help = "Concise curse",\
    action = "store_true")

    parser.add_argument("name", help = "Enter your name ", type = str)
    parser.add_argument("-f", "--fuck", help = "Fuck you Berkeley", \
    action = "store_true")


    args = parser.parse_args()
    print("Hello", args.name)

    if args.fuck:
        if args.verbose:
            print("May Heaven unleash its full rage on the University of California at Berkeley")
        elif args.quiet:
            print("Fuck you Berkeley")

if __name__ == "__main__":
    main()
