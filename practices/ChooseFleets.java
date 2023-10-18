import java.util.Arrays;

/**
 * Given an integer denoting a total number of wheels, find the number of different ways to choose a fleet of vehicles
 * from 2 wheeled and 4 wheeled, such that the group of chosen vehicles has that exact total number of wheels
 * 2 ways of choosing vehicles are different if and only  if they contain different # of 2 /4 wheels
 * i.e. wheels=[4,5,6] return array: [2,0,2] 一个4轮可以是1*4或者2*2，不可以有5轮，6轮可以是4+2或3*2，所以是【2，0，2】种
 */
public class ChooseFleets {
    public int[] chooseFleets(int[] vehicles) {
        int[] ans = new int[vehicles.length];
        int len = ans.length;
        for (int i = 0; i < len; i++) {
            if (i % 2 != 0)
                continue;
            ans[i] = vehicles[i] / 4 + 1;
        }
        return ans;
    }

    public static void main(String[] args) {
        ChooseFleets test = new ChooseFleets();
        int[] vehicles = new int[] {6,3,2};
        System.out.println(Arrays.toString(test.chooseFleets(vehicles)));
    }
}
