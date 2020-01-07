import java.io.*;

public class TestReen implements Serializable {
    private int id;
    private String name;
    private SonReen sonReen;
    public TestReen(int id, String name, SonReen sonReen) {
        this.id = id;
        this.name = name;
        this.sonReen = sonReen;
    }
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public SonReen getSonReen() {
        return sonReen;
    }
    public void setSonReen(SonReen sonReen) {
        this.sonReen = sonReen;
    }
    public Object deepClone() throws Exception{

        ByteArrayOutputStream bo = new ByteArrayOutputStream();
        ObjectOutputStream out = new ObjectOutputStream(bo);
        out.writeObject(this);

        ByteArrayInputStream bi = new ByteArrayInputStream(bo.toByteArray());
        ObjectInputStream oi = new ObjectInputStream(bi);
        return oi.readObject();

    }
    public static void main(String[] args) throws Exception{

        SonReen sonReen = new SonReen(1, "张三");
        TestReen t1 = new TestReen(1, "李四", sonReen);
        TestReen t2 = (TestReen)t1.clone();
        System.out.println("t1 ? "+ (t1 == t2));
        System.out.println("sonReen: ? "+ (t1.getSonReen() == t2.getSonReen()));
        System.out.println("T name: ? " + (t1.getName() == t2.getName()));
        System.out.println("S name: ? " + (t1.getSonReen().getSonName() == t2.getSonReen().getSonName()));

        SonReen sonReen1 = new SonReen(1, "王五");
        t2.setSonReen(sonReen1);
        System.out.println("son : "+ t1.getSonReen().getSonName());
        System.out.println("son1 : "+ t2.getSonReen().getSonName());
        System.out.println("son == son1 : ? "+ (t1.getSonReen() ==  t2.getSonReen()));

    }
}
class SonReen implements Serializable{
    private int sonId;
    private String sonName;
    public SonReen(int sonId, String sonName) {
        super();
        this.sonId = sonId;
        this.sonName = sonName;
    }
    public int getSonId() {
        return sonId;
    }
    public void setSonId(int sonId) {
        this.sonId = sonId;
    }
    public String getSonName() {
        return sonName;
    }
    public void setSonName(String sonName) {
        this.sonName = sonName;
    }
}