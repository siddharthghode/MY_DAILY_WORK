import java.util.ArrayList;

public class ClosestPreset {
    static class Rectangle {
        String name;
        int w, l;
        Rectangle(String name, int w, int l) { this.name = name; this.w = w; this.l = l; }
    }

    public static void main(String[] args) {
        ArrayList<Rectangle> boxes = new ArrayList<>();
        boxes.add(new Rectangle("Shipping Box", 10, 20));
        boxes.add(new Rectangle("Gift Box", 5, 5));
        boxes.add(new Rectangle("Storage Bin", 40, 60));

        System.out.println("--- Inventory Dimensions ---");
        for (Rectangle box : boxes) {
            System.out.println("Item: " + box.name);
            System.out.println("  Width (w):  " + box.w);
            System.out.println("  Length (l): " + box.l);
            System.out.println("---------------------------");
        }
    }
}
