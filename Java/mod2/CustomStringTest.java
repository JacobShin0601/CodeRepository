import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class CustomStringTest {

	//declare custom string for testing
	CustomString myCustomString;

	@BeforeEach
	public void setUp() throws Exception {
		//initialize custom string for testing
		this.myCustomString = new CustomString();
	}

	@Test
	void testGetString() {
		
		//string should be null to start, before setting it
		assertNull(this.myCustomString.getString());
		
		this.myCustomString.setString("hello");
		assertEquals("hello", this.myCustomString.getString());
		
		// TODO write at least 3 additional test cases 
        this.myCustomString.setString("working");
        assertEquals("working", this.myCustomString.getString());
        
        this.myCustomString.setString("find");
        assertEquals("find", this.myCustomString.getString());
        
        this.myCustomString.setString("Yes");
        assertEquals("Yes", this.myCustomString.getString());
	}
	
	@Test
	void testSetString() {
		
		//string should be null to start, before setting it
		assertNull(this.myCustomString.getString());
		
		this.myCustomString.setString("Good-bye!");
		assertEquals("Good-bye!", this.myCustomString.getString());
		
		// TODO write at least 3 additional test cases 
        this.myCustomString.setString("glad to hear that~");
		assertEquals("glad to hear that~", this.myCustomString.getString());
        
        this.myCustomString.setString("1, 2, 3, launch!");
		assertEquals("1, 2, 3, launch!", this.myCustomString.getString());
        
        this.myCustomString.setString("oh MG");
		assertEquals("oh MG", this.myCustomString.getString());
	}
	
	@Test
	void testRemove() {
		assertEquals("", this.myCustomString.remove(""));
		
		this.myCustomString.setString(null);
		assertEquals("", this.myCustomString.remove(""));
		
		this.myCustomString.setString("my lucky numbers are 6, 8, and 19.");
		assertEquals("my lucky numbes e 6, 8, nd 19.", this.myCustomString.remove("ra6"));
		
		// TODO write at least 3 additional test cases 
        assertEquals("my ucky numers are 6, 8, and 19.", this.myCustomString.remove("bl7"));
        assertEquals("y lucky nubers are 6, 8, and 19.", this.myCustomString.remove("cm1"));
        assertEquals("m luck numbers are 6, 8, an 19.", this.myCustomString.remove("yd2"));
	}

	@Test
	void testReverse() {
		assertEquals("", this.myCustomString.reverse(""));
		
		this.myCustomString.setString(null);
		assertEquals("", this.myCustomString.reverse(""));
		
		this.myCustomString.setString("abc, XYZ; 123.");
		assertEquals("aBC, xyz; 123.", this.myCustomString.reverse("bcdxyz@3210."));
		
		// TODO write at least 3 additional test cases 
        assertEquals("ABC, XYZ; 123.", this.myCustomString.reverse("abc"));
        assertEquals("abc, xyz; 123.", this.myCustomString.reverse("XYZ"));
        assertEquals("abc, xyz; 123.", this.myCustomString.reverse("xyz"));
	}

	@Test
	void testFilterLetters() {
		assertEquals("", this.myCustomString.filterLetters('E', false));
		
		this.myCustomString.setString(null);
		assertEquals("", this.myCustomString.filterLetters('E', false));
		
		// TODO write at least 3 additional test cases 
        this.myCustomString.setString("ABCDEFGHIJKLMNOP");
		assertEquals("IJKLMNOP", this.myCustomString.filterLetters('H', false));
        assertEquals("P", this.myCustomString.filterLetters('O', false));
        assertEquals("ABCDEFGHIJKLMN", this.myCustomString.filterLetters('O', true));
        
	}

}