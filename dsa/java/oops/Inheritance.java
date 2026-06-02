public class Inheritance {
    static class Parents {
        String name;
        int age;

        Parents() { System.out.println("this is parent"); }
    }

    static class Child extends Parents {
        int rollno;

        Child() { System.out.println("This is child"); }
    }

    public static void main(String[] args) {
        Child c1 = new Child();
        c1.name = "siddharth";
        c1.age = 23;
        c1.rollno = 24111042;
        System.out.println("Name" + c1.name);
        System.out.println("Age" + c1.age);
        System.out.println("Roll no" + c1.rollno);
    }
}
