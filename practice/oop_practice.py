class students:

    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


student1 = students('harry', 85)
student2 = students("janet", 30)

did_pass = student1.check_pass_fail()
print(did_pass)
did_pass = student2.check_pass_fail()
print(did_pass)
