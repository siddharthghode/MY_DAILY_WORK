public class CopyConstructor {
    static class Teacher {
        int salary = 30000;
        String name = "siddharth", subject = "math";

        Teacher() {}
        Teacher(Teacher custom) {
            System.out.println("custome constructor called");
            salary = custom.salary;
            name = custom.name;
            subject = custom.subject;
        }

        void getInfo() {
            System.out.println(salary);
            System.out.println(name);
            System.out.println(subject);
        }
    }

    public static void main(String[] args) {
        Teacher t1 = new Teacher();
        Teacher t2 = new Teacher(t1);
        t2.getInfo();
    }
}
