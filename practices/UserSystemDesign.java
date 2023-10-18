import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/**
 * 写一个简单的api，有三个功能 register，log in，log out。
 * register的时候要输入username和password，如果这个用户已经register过了要返回username already exists，没有的话返回registered successfully；
 * log in时也要name和password，如果该name并没有register或者已经logged in，或者password错误，要返回log in unsuccessful，如果都满足就返回logged in successfully；
 * 最后是log out，正常的话返回成功，没有register或者没有log in的name要返回log out失败。
 * Given a log of API requests，通过输入a list of strings然后你自己去parse出以上三个指令。
 *
 * 解法：两个hashmap，分别储存是否register和是否login !!!!!注意output的大小写！！！！！！
 * https://leetcode.com/discuss/interview-question/1759648/Amazon-or-OA-SDE-Intern-or-Amazon-Sign-In-pages-(register-login-logout)
 */
public class UserSystemDesign {
    public static void main(String[] args) {
        List<String> s = new ArrayList<>();
        s.add("register david david123"); // successful
        s.add("register david david123"); // fail because already exist
        s.add("register adam 1Adam1"); // successful

        s.add("login ddd david345"); // fail, user don't exist
        s.add("login david david123"); // success
        s.add("login adam 1adam1"); // fail, password don't match
        s.add("login david david123"); // fail, already logged in

        s.add("logout david"); // success
        s.add("logout ddd"); // fail, user don't exist
        s.add("logout david"); // fail, already logged out
        System.out.println(implementAPI(s));
    }
    public static List<String> implementAPI(List<String> logs) {
        HashMap<String, String> register = new HashMap<>();
        HashMap<String, String> login = new HashMap<>();
        List<String> ans = new ArrayList<>();
        for (String log : logs) {
            String[] split = log.split(" ");
            String command = split[0];
            String userName = split[1];
            String password = split[2];
            switch (command) {
                case "register":
                    // 1.Username already exists
                    if (register.containsKey(userName)) {
                        ans.add("Username already exists");
                    }
                    // 2.Username not exists
                    else {
                        register.put(userName, password);
                        ans.add("Registered successfully");
                    }
                    break;
                case "login":
                    // 1. registered users
                    if (register.containsKey(userName)) {
                        // 1.1 already logged in
                        if (login.containsKey(userName)) {
                            ans.add("Login Unsuccessfully");
                        }
                        // 1.2 not logged in
                        else {
                            // correct password
                            if (register.get(userName).equals(password)) {
                                login.put(userName, password);
                                ans.add("Logged in Successfully");
                            }// incorrect password
                            else {
                                ans.add("Login Unsuccessfully");
                            }
                        }
                    }// 2 not registered
                    else {
                        ans.add("Login Unsuccessfully");
                    }
                    break;
                case "logout":
                    if (register.containsKey(userName)) {
                        if (login.containsKey(userName)) {
                            login.remove(userName);
                            ans.add("Logged Out Successfully");
                        } else {
                            ans.add("Logged out unsuccessfully");
                        }
                    } else {
                        ans.add("Logout Unsuccessfully");
                    }
                    break;
            }
        }
        return ans;
    }
}
