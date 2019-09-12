import java.util.Scanner;

public class HelloWorld {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int aa = in.nextInt();
        float bb = in.nextFloat();
        System.out.println(aa);
        System.out.println(bb);
        int origin = 0x000000FF;
        int originReverse = ~origin;
        int originReverseManually = 0xFFFFFF00;
        System.out.println(origin);
        System.out.println(originReverse);
        System.out.println(originReverseManually);
    }
}