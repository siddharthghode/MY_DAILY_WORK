public class ClassAndObject {
    static class Student {
        private int age = 22;
        String name = "siddharth";
        int roll = 24111042;
        String lname = "ghode";

        int changeRollNumber(int newRoll) { roll = newRoll; return roll; }
        String getName() { return name; }
        int getAge() { return age; }
    }

    public static void main(String[] args) {
        Student st1 = new Student();
        st1.changeRollNumber(45);
        System.out.println(st1.roll);
        System.out.println(st1.getName());
        System.out.println(st1.getAge());
        System.out.println(st1.name + " " + st1.lname);
    }
}
