class Student:
    roll = ''
    gpa = ''

    def set_value(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa


    def display(self):
        print(f'Roll: {self.roll}, GPA : {self.gpa}')


rahim = Student()
rahim.set_value(101, 3.75)
rahim.display()


karim = Student()
karim.set_value(102, 3.50)
karim.display()