public class length_last {
    public int lengthofLastWord(String s){
        String[] words = s.trim().split(" ");
        return words[words.length - 1].length();

    }
}