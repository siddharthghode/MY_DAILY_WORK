public class Encapsulation {
    static class Teacher {
        private int salary;
        String name, subject, standard;

        Teacher() { System.out.println("Here comes the constructor"); }
        void setSalary(int s) { salary = s; }
        int getSalary() { return salary; }
    }

    public static void main(String[] args) {
        Teacher t1 = new Teacher();
        t1.name = "siddharth";
        t1.subject = "maths";
        t1.standard = "12th";
        t1.setSalary(25000);
        System.out.println(t1.getSalary());
    }
}
