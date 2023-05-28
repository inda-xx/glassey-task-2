public class IndamonTest {

    @Test
    public void testAttack() {
        // Create a new Indamon object for the attacker
        Indamon attacker = new Indamon();
        attacker.name = "Attacker";
        attacker.hp = 10;
        attacker.attack = 5;
        attacker.defense = 2;

        // Create a new Indamon object for the defender
        Indamon defender = new Indamon();
        defender.name = "Defender";
        defender.hp = 10;
        defender.attack = 3;
        defender.defense = 2;

        // The attacker attacks the defender. According to the attack logic,
        // the defender's HP should decrease by the attacker's attack value minus the defender's defense value (5 - 2 = 3).
        // So, the defender's HP should become 7 (10 - 3).
        attacker.attack(defender);

        // Check that the defender's HP is 7 and that the defender hasn't fainted
        assertEquals("After the first attack, defender's HP should be 7.", 7, defender.hp);
        assertFalse("Defender should not be fainted after the first attack.", defender.fainted);

        // Repeat the process to further decrease the defender's HP
        attacker.attack(defender);

        // Check that the defender's HP is now 4 and that the defender still hasn't fainted
        assertEquals("After the second attack, defender's HP should be 4.", 4, defender.hp);
        assertFalse("Defender should not be fainted after the second attack.", defender.fainted);

        // Repeat the process to further decrease the defender's HP
        attacker.attack(defender);

        // Check that the defender's HP is now 1 and that the defender still hasn't fainted
        assertEquals("After the third attack, defender's HP should be 1.", 1, defender.hp);
        assertFalse("Defender should not be fainted after the third attack.", defender.fainted);

        // Repeat the process to further decrease the defender's HP
        attacker.attack(defender);

        // Check that the defender's HP is now 0 and that the defender has fainted
        assertEquals("After the fourth attack, defender's HP should be 0.", 0, defender.hp);
        assertTrue("Defender should be fainted after the fourth attack.", defender.fainted);
    }
}
