class Indamon {

    String name;
    int hp;
    int attack;
    int defense;
    boolean fainted;

    public static void main(String[] args) {
        // create a new "Indamon" object
        Indamon glassey = new Indamon();
    
        // assign the instance variables to meaningful values
        glassey.name = "Glassey";
        glassey.hp = 10;
        glassey.attack = 5;
        glassey.defense = 5;
    
        // get the information of the assigned values
        System.out.println("Name: " + glassey.name);
        System.out.println("HP: " + glassey.hp);
        System.out.println("Attack value: " + glassey.attack);
        System.out.println("Defense value: " + glassey.defense);
      } // end main method
}