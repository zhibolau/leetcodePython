#002 给一串string 比如“I have a card”再给一个键盘char[]。 键盘里有h，a，v，e。问句子里几个字可以被键盘打出来。
#只有have和a可以。 然后所有标点符号都可以被打出来

public class brokeKeyboard {
    public int solution(String sentence, List<Character> list){
         if(list.size() == 0){
             return sentence.split(" ").length;
         }
         int res = 0;
         boolean flag = false;
         String[] words = sentence.toLowerCase().split(" ");//先化为小写，然后按空格分割
         for(String word: words){
             for(Character i: word.toCharArray()){
                 if(Character.isLowerCase(i)){
                     if(!list.contains(i)){//如果出现不存在的字母立马break，走完循环res就加一
                         flag = true;
                         break;
                     }
                 }
             }
             if(!flag) {
                 res++;
             }else{
                 flag = false;
             }
         }
         return res;
    }

    public static void main(String[] args){
        brokeKeyboard bk = new brokeKeyboard();
        String sentence = "hEllo##, This^^";
        List<Character> list = Arrays.asList('i','e','o','l','h');
        int res = bk.solution(sentence, list);
        System.out.print("res: ");
        System.out.print(res);
    }
}
