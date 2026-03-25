class person:
    def __init__(self,name,gender,age):
         self.name=name
         self.gender=gender
         self.age=age
    def add(self,personlist): 
        personlist.append({"name":self.name, "gender":self.gender, "age":self.age})
    def delete(self,list1,name):
        for i in list1:
            if i["name"]==name:
                return list1.remove(i)
        return "oops"
class teacher(person):
    def __init__(self, name, gender, age, subject):
         super().__init__(name, gender, age)
         self.subject=subject
    def add(self, teacherlist):
        teacherlist.append({"name":self.name, "gender":self.gender, "age":self.age, "subject":self.subject})
list1=[]
list2=[]
p1=person("sid",True,21)
p1.add(personlist)
t1=teacher("ashhutosh",True,21,"maths")
t1.add(teacherlist)
ti3=timepass()





