public class ParemetrizedInheritance {
    static class Teacher {
        String name;
        int age;

        Teacher(String name, int age) { this.name = name; this.age = age; }
    }

    static class Student extends Teacher {
        int rollno;

        Student(String name, int age, int rollno) {
            super(name, age);
            this.rollno = rollno;
        }

        void getInfo() {
            System.out.println("Name:" + name);
            System.out.println("Age:" + age);
            System.out.println("Rollno" + rollno);
        }
    }

    public static void main(String[] args) {
        Student s1 = new Student("siddharth", 23, 24111042);
        s1.getInfo();
    }
}
