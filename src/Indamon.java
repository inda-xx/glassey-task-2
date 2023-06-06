class Indamon {

    private String name;
    private int hp;
    private int attack;
    private int defense;
    private boolean fainted;
    
    public Indamon(String name, int hp, int, attack, int defense) {
        this.name = name;
        this.hp = hp;
        this.attack = attack;
        this.defense = defense;
        fainted = false;
    }
    
    // getters
    public String getName() { }
    public int getHp() { }
    public int getAttack() { }
    public int getDefense() { }
    public boolean getFainted() { }

    // setters
    public void setName() { }
    public void setHp() { }
    public void setAttack() { }
    public void setDefense() { }
    public void setFainted() { }
        
    
    public static void main(String[] args) {
        // create a new "Indamon" object
        Indamon glassey = new Indamon("Glassey", 10, 5, 5);    
    } // end main method
}
