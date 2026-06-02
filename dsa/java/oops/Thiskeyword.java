public class Thiskeyword {
    static class Person {
        private int phoneNumber;
        String name, lname;
        int age, height;

        Person(int phoneNumber, String name, String lname, int age, int height) {
            this.phoneNumber = phoneNumber;
            this.name = name;
            this.lname = lname;
            this.age = age;
            this.height = height;
        }

        void display() {
            System.out.println("Name: " + name + " " + lname);
            System.out.println("Age: " + age);
            System.out.println("Height: " + height);
            System.out.println("Phone: " + phoneNumber);
        }
    }

    public static void main(String[] args) {
        Person p1 = new Person(1234567890, "abc", "xyz", 20, 5);
        p1.display();
    }
}
