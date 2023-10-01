public class Main {
	private static char[] dict = new char[26];

    public static void build() {
        Da da = new Da();
        Db db = new Db();
        Dc dc = new Dc();
        Dd dd = new Dd();
        De de = new De();
        Df df = new Df();

        dd.tr(dict);
        df.tr(dict);
        de.tr(dict);
        db.tr(dict);
        da.tr(dict);
        dc.tr(dict);
    }

    public static void main(String[] args) {
        build();
        
        String key = args[0];

        if (key.length() != 10) {
            System.out.println("false");
            return;
        }

        String transformed = "";

        for(char c : key.toCharArray()) {
            transformed += map(c);
        }

        if (transformed.equals("{[_<+<$[?|")) {
            System.out.println("true");
        } else {
            System.out.println("false");
        }

    }
	
	public static char map(char c) {
		return dict[c - 'A'];
	}
}