''' template '''
from string import Template

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
    t = Template("$name with $GPA with $dick")
    for st in student:
        print(t.safe_substitute(st))
    return student

print(template_mod())
