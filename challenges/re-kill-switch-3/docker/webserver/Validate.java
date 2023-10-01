public class Validate {
    public static void main(String[] args) {
        String keyText = args[0];

        if (keyText.length() != 10) {
            System.out.println("false");
            return;
        }
        
        int[] key = new int[10];

        for (int i = 0; i < 10; i++) {
            key[i] = (int) keyText.charAt(i);
        }

        Boolean check1 = (((key[0] & 0b00001111) | (key[2] & 0b11110000)) == (0b01010100));
        Boolean check2 = ((((key[0] & 0b11110000) | (key[2] & 0b00001111)) & 10111000) == 0);
        Boolean check3 = (key[5] << 2 == 224);
        Boolean check4 = (((key[3] & 0b111) == 0) && ((key[3] >> 3) == 011));
        Boolean check5 = (((key[1] & key[7]) == 0) && ((key[1] | key[7]) == 0b01111111) && (key[7] > 0b01000000) && (key[1] < 0b01000000));
        Boolean check6 = ((key[4] & 1) == 0 && (key[4] & 2) == 2 && (key[4] & 4) == 4 && (key[4] & 8) == 0 && (key[4] & 16) == 16 && (key[4] & 32) == 0 && (key[4] & 64) == 64 && (key[4] & 128) == 0);
        Boolean check7 = (((key[8] - key[6]) == 0b11) && ((key[6] + key[9]) == 0b10010010) && ((key[6] + key[8] + key[9]) == 0b11011101));

        if ( check1 && check2 && check3 && check4 && check5 && check6 && check7 ) {
            System.out.println("true");
        } else {
            System.out.println("false");
        }
    }
}