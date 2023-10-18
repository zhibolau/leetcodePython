import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class EconomyMart {
    public static void main(String[] args) {
        String[][] test = {{"INSERT", "milk ", "4"},
                {"INSERT", "coffee ", "3"},
                {"VIEW", "-", "-"},
                {"INSERT", "pizza  ", "5"},
                {"INSERT", "apple  ", "3"},
                {"INSERT", "gum ", "1"},
                {"VIEW", "-", "-"}
        };
        for (String s : getCheapestProducts(test))
            System.out.println(s);
    }

    private static class Product implements Comparable<Product>{
        long price;
        String name;

        public Product(long price, String name) {
            this.price = price;
            this.name = name;
        }

        public int compareTo(Product another) {
            int diff = (int) (this.price - another.price);
            if (diff != 0) return diff;
            return this.name.compareTo(another.name);
        }
    }


    public static List<String> getCheapestProducts(String[][] entries) {
        List<Product> items = new ArrayList<>();
        List<String> returnValues = new ArrayList<>();
        int noOfViewing = 0;
        for (String[] entry : entries) {
            String command = entry[0];
            switch (command) {
                case "INSERT":
                    String itemName = entry[1];
                    long itemPrice = Long.parseLong(entry[2]);
                    items.add(new Product(itemPrice, itemName));
                    break;
                case "VIEW":
                    Collections.sort(items);
                    returnValues.add(items.get(noOfViewing++).name);
            }
        }
        return returnValues;
    }
}
