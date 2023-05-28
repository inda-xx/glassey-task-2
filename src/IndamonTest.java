import org.junit.Test;
import static org.junit.Assert.*;

public class IndamonTest {

    @Test
    public void testAttack() {
        Indamon attacker = new Indamon();
        attacker.name = "Attacker";
        attacker.hp = 10;
        attacker.attack = 5;
        attacker.defense = 2;

        Indamon defender = new Indamon();
        defender.name = "Defender";
        defender.hp = 10;
        defender.attack = 3;
        defender.defense = 2;

        // Attacker attacks defender, defender's HP should decrease by 3 (5 attack - 2 defense)
        attacker.attack(defender);
        assertEquals(7, defender.hp);
        assertFalse(defender.fainted);

        // Attacker attacks defender again, defender's HP should be 4
        attacker.attack(defender);
        assertEquals(4, defender.hp);
        assertFalse(defender.fainted);

        // Attacker attacks defender again, defender's HP should be 1
        attacker.attack(defender);
        assertEquals(1, defender.hp);
        assertFalse(defender.fainted);

        // Attacker attacks defender again, defender's HP should be 0 and fainted should be true
        attacker.attack(defender);
        assertEquals(0, defender.hp);
        assertTrue(defender.fainted);
    }
}
