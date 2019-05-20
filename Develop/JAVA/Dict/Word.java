import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Word {
    public String word;
    public String meaning;
    public List<String> attributes;

    public Word(String w, String m) {
        word = w;
        meaning = m;
        attributes = new ArrayList<String>();
    }

    public String getWord() {
        return word;
    }
    public String getMeaning() {
        return meaning;
    }
    public String[] getAttributes() {
        return (String[])(attributes.toArray());
    }

    public void setAttributes(String[] att) {
        attributes = Arrays.asList(att);
    }
    public void addAttribute(String att) {
        attributes.add(att);
    }
    public void remAttribute(String att) {
        attributes.remove(att);
    }
}