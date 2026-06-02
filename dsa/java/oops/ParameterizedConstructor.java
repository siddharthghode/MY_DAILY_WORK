public class ParameterizedConstructor {
    static class Teacher {
        private int salary;
        String relationship, name, subject, standard;

        Teacher() { System.out.println("Here comes the constructor"); }
        Teacher(int s, String rel) { salary = s; relationship = rel; }
        void setSalary(int s) { salary = s; }
        int getSalary() { return salary; }
    }

    public static void main(String[] args) {
        Teacher t1 = new Teacher(24000, "commited");
        t1.name = "siddharth";
        t1.subject = "maths";
        t1.standard = "12th";
        t1.setSalary(25000);
        System.out.println(t1.getSalary());
        System.out.println(t1.relationship);
    }
}
