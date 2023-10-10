public class justifyNewspaperText {
    public static final String STAR = "*";
    public static final String SPACE = " ";
    public static final String[] POS = new String[]{"LEFT", "RIGHT"};

    public justifyNewspaperText() {
    }

    public static void main(String[] args) {
        justifyNewspaperText test = new justifyNewspaperText();
        String[][] lines = new String[][]{{"hello", "world"}, {"How", "areYou", "doing"}, {"Please look", "and align", "to right", "OK?"}};
        String[] aligns = new String[]{"LEFT", "RIGHT", "RIGHT"};
        int width = 16;
        String[] res = test.justifyNewspaperText(lines, aligns, width);
        String[] var6 = res;
        int var7 = res.length;

        for(int var8 = 0; var8 < var7; ++var8) {
            String x = var6[var8];
            System.out.println(x);
        }

    }

    public String[] justifyNewspaperText(String[][] lines, String[] aligns, int width) {
        String bar = this.repeat("*", width + 2);
        List<String> output = new ArrayList();
        output.add(bar);

        for(int i = 0; i < lines.length; ++i) {
            String[] line = lines[i];
            List<StringBuilder> sbs = new ArrayList();
            sbs.add(new StringBuilder());
            int curSb = 0;
            ((StringBuilder)sbs.get(curSb)).append(line[0]);

            for(int j = 1; j < line.length; ++j) {
                String word = line[j];
                if (((StringBuilder)sbs.get(curSb)).length() + word.length() + 1 <= width) {
                    ((StringBuilder)sbs.get(curSb)).append(" ").append(word);
                } else {
                    sbs.add(new StringBuilder());
                    ++curSb;
                    ((StringBuilder)sbs.get(curSb)).append(word);
                }
            }

            Iterator var14 = sbs.iterator();

            while(var14.hasNext()) {
                StringBuilder sb = (StringBuilder)var14.next();
                output.add(this.getLine(sb, aligns[i], width));
            }
        }

        output.add(bar);
        String[] res = new String[output.size()];

        for(int i = 0; i < res.length; ++i) {
            res[i] = (String)output.get(i);
        }

        return res;
    }

    public String getLine(StringBuilder sb, String pos, int width) {
        int remainingSpace = width - sb.length();
        String res = "*";
        if (pos.equals(POS[0])) {
            res = res + sb.toString() + this.repeat(" ", remainingSpace) + "*";
        } else {
            res = res + this.repeat(" ", remainingSpace) + sb.toString() + "*";
        }

        return res;
    }

    private String repeat(String str, int time) {
        String newstring = "";

        for(int i = 0; i < time; ++i) {
            newstring = newstring + str;
        }

        return newstring;
    }
}

