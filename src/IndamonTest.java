import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

public class IndamonTest {
    private Indamon indamon;

    @Before
    public void setUp() {
        indamon = new Indamon("Glassey", 10, 5, 5);
    }

    @Test
    public void testGetName() {
        assertEquals("Glassey", indamon.getName());
    }

    @Test
    public void testGetHp() {
        assertEquals(10, indamon.getHp());
    }

    @Test
    public void testGetAttack() {
        assertEquals(5, indamon.getAttack());
    }

    @Test
    public void testGetDefense() {
        assertEquals(5, indamon.getDefense());
    }

    @Test
    public void testGetFainted() {
        assertEquals(false, indamon.getFainted());
    }

    @Test
    public void testSetName() {
        indamon.setName("NewName");
        assertEquals("NewName", indamon.getName());
    }

    @Test
    public void testSetHp() {
        indamon.setHp(20);
        assertEquals(20, indamon.getHp());
    }

    @Test
    public void testSetAttack() {
        indamon.setAttack(7);
        assertEquals(7, indamon.getAttack());
    }

    @Test
    public void testSetDefense() {
        indamon.setDefense(8);
        assertEquals(8, indamon.getDefense());
    }
    
    // Currently setFainted() method has no implementation or parameters to set
    // If setFainted(boolean) was the intention
    /*
    @Test
    public void testSetFainted() {
        indamon.setFainted(true);
        assertEquals(true, indamon.getFainted());
    }
    */
}
