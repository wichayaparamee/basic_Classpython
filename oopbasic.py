class Student:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender 

    def study(self):
        print(f'{self.name}กำลังเรียน.....')

    def sawatdee(self):
        if self.gender == 'ชาย':
            tail = 'ครับ'
            callme = 'ผม'
        else:
            tail = 'ค่ะ'
            callme = 'หนู'
        print(f'สวัสดี{tail} {callme}ชื่อ{self.name}')

class SpecailStudent(Student):
    def __init__ (self,name,age,gender,parent):
        super().__init__(name,age,gender)
        self.parent = parent 

    def hello(self,person = 'เพื่อน'):
        if person == 'เพื่อน':
            print('ว่าไงเพื่อน มีขนมป่าว')
        else:
            print('เดินหนีไป ดีกว่า')

    def sawatdee(self):
        print(f'สวัสดี ฉันชื่อ{self.name}')

    def myparent(self):
        print('คุณครู{self.}รู้ไหม? ผมลูกใคร')
        print(f'ผมลูก{self.parent}')

class Teacher:
    def __init__(self,name,age,gender,subject):
        self.name = name
        self.age = age
        self.gender = gender
        self.subject = subject

    def tech(self):
        print('คุณครู{}กำลังสอนวิชา{}'.format(self.name, self.subject))


print('NAME:', __name__) # หากปริ้นในที่นี้จะเป็น __main__ แต่หาก import ที่อื่น ก็จะเป็น ชื่อ ไฟล์ แทนเลย 
                         # ซึ่งหาก if ในที่นี้ ก็จะได ้__name__ = __main___ 
                         # ตัวปริ้น นี้ยังแสดงไปยังตัวที่ import ด้วย หรือใช้คำสั่ง run 
if __name__ == '__main__':
    student1 = Student('สมชาย',14,'ชาย') # ประกาศตัวแปร
    student2 = Student('สมศรี',14,'หญิง')
    teacher1  = Teacher('จอนห์',28,'ชาย','คณิต')
    student3 = SpecailStudent('joy',16,'ชาย','นายกเจต')

    print(teacher1.name)
    print(teacher1.subject)

    print('-------8.30--------')   
    teacher1.tech()
    student1.sawatdee()
    student2.sawatdee()
    student1.study()
    student2.study()

    print('------8.45----------')
    student3.sawatdee()
    student3.hello()
    student3.myparent()
