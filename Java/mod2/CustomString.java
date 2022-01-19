//import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.*;  

/**
 * In this assignment, you will implement a simple class called CustomString.  This class represents a more customizable version 
 * of a String, with additional attributes and methods.  
 * For example, the CustomString class has a “reverse” method which returns a new string version of the current string where the 
 * capitalization is reversed (i.e., lowercase to uppercase and uppercase to lowercase) for the alphabetical characters specified 
 * in the given arg.  For CustomString “abc, XYZ; 123.”, calling reverse("bcdxyz@3210.") will return "aBC, xyz; 123.".  
 * 
 * The CustomString class also has a “remove” method which returns a new string version of the current string where the alphabetical 
 * characters specified in the given arg, are removed.  For CustomString "my lucky numbers are 6, 8, and 19.", calling remove("ra6") 
 * will return "my lucky numbes e 6, 8, nd 19.".
 * 
 */
public class CustomString {

	private static final boolean False = false;

	//instance variables

	/**
	 * Current string.
	 */
	String myString;

	/**
	 * Indicates if the current string myString has been set (not null).
	 */
	boolean isSet;

	private boolean True;

	//constructor

	/**
	 * Initializes current string myString to null.
	 * Initializes isSet to false.
	 */
	public CustomString() {
		// TODO Implement constructor
		myString = null;
		isSet = false;
	}

	// methods 

	/**
	 * Returns the current string.
	 * If the current string is null, or has not been set to a value with setString, it should return null.
	 * @return current string
	 */
	public String getString() {
		// TODO Implement method

		//if(myString != "") {
		//     return this.myString;
		//}
		//else {return null;}
		if(myString == null || isSet == false) {
			return null;
		}
		else {return this.myString;}
	}

	/**
	 * Sets the value of the current string and sets this.isSet to true.
	 * If the given string is null, sets this.isSet to false.
	 * @param string value to be set
	 */
	public void setString(String string) {
		// TODO Implement method
		//        if(string != null){
		//            myString = string;
		//            isSet = True;
		//        }
		//        else {
		//            isSet = False;
		//        }
		if (string == null) {
			isSet = false;
		}
		else {
			isSet = true;
			this.myString = string;
		}
	}

	/**
	 * Returns a new string version of the current string where the alphabetical characters specified in the given arg, are removed.
	 *   
	 * The alphabetical characters to be removed are case insensitive.  
	 * All non-alphabetical characters are unaffected.
	 * If the current string is null, empty, or has not been set to a value, this method should return an empty string.
	 *
	 * Example(s):
	 * - For a current string "my lucky numbers are 6, 8, and 19.", calling remove("ra6") would return "my lucky numbes e 6, 8, nd 19."
	 * - For a current string "my lucky numbers are 6, 8, and 19.", calling remove("6,.") would return "my lucky numbers are 6, 8, and 19."
	 * - For a current string "my lucky numbers are 6, 8, and 19.", calling remove("") would return "my lucky numbers are 6, 8, and 19."
	 * 
	 * Remember: This method builds and returns a new string, and does not directly modify the myString field.
	 * 
	 * @param arg the string containing the alphabetical characters to be removed from the current string
	 * @return 
	 * @return new string in which the alphabetical characters specified in the arg are removed
	 */

	
	
	public String remove(String arg) {
		// TODO Implement method

		//make an empty RemovedStrings and ArrayOfRemovedStrings for containing


		//if string is not null or isSet is not False
		if (myString != null && isSet != false) {
			int size = myString.length();
			String RemovedStrings = "";
			char[] arrayOfRemovedStrings = new char[size];

			//make arrays of arguments and strings to compare
			char[] arrayOfArg = arg.toCharArray();   
			char[] arrayOfStrings = myString.toCharArray();

			//let's start with strings array
			for (int i=0; i<size; i++){
				int cnt = 0;
				//if string component is the letter
				if (Character.isLetter(arrayOfStrings[i]) == true){

					//let's do argument loop to check
					for (int j=0; j<arg.length(); j++){

						//if argument is lower case
						if (Character.isLowerCase(arrayOfArg[j]) == true){
							char Lower = arrayOfArg[j]; // put it as it is 
							char Upper = Character.toUpperCase(arrayOfArg[j]); // change them and store it as upper case

							//if lower or upper case of argument is matched with string, not to store it to new array : skip it
							if (Lower == arrayOfStrings[i] || Upper == arrayOfStrings[i]){
								continue;
							}
							// if there's no match between string and arguments of lower and upper case
							else{
								arrayOfRemovedStrings[cnt] = arrayOfStrings[i];
								cnt++;
							}
						}

						//if argument is upper case, do the same thing in an opposite way
						else {
							char Upper = arrayOfArg[j]; // put it as it is 
							char Lower = Character.toLowerCase(arrayOfArg[j]); // change them and store it as upper case

							//if lower or upper case of argument is matched with string, not to store it to new array : skip it
							if (Lower == arrayOfStrings[i] || Upper == arrayOfStrings[i]){
								continue;
							}
							// if there's no match between string and arguments of lower and upper case
							else{
								arrayOfRemovedStrings[cnt] = arrayOfStrings[i];
								cnt++;
							}
						}
					} // end of argument for loop to compare strings and arguments
				}// end of loop for checking whether string is character or not

				// if it's not a letter, always append to new array
				else {
					arrayOfRemovedStrings[cnt] = arrayOfStrings[i];
					cnt++;
				}

			}// end of string for loop

			//since it's the end of for loop, we're going to make strings from new array
			RemovedStrings = String.valueOf(arrayOfRemovedStrings);
			return RemovedStrings;


		}// end of IF to check whether string is null or isSet is False

		//if string is null or isSet is False
		else {
			String RemovedStrings = "";
			return RemovedStrings; // it's empty so far
		}
	}

	/**
	 * Returns a new string version of the current string where the capitalization is reversed (i.e., lowercase to uppercase, 
	 * and uppercase to lowercase) for the alphabetical characters specified in the given arg.
	 *   
	 * All non-alphabetical characters are unaffected.
	 * If the current string is null, empty, or has not been set to a value, this method should return an empty string.
	 *
	 * Example(s):
	 * - For a current string "abc, XYZ; 123.", calling reverse("bcdxyz@3210.") would return "aBC, xyz; 123."
	 * - For a current string "abc, XYZ; 123.", calling reverse("6,.") would return "abc, XYZ; 123."
	 * - For a current string "abc, XYZ; 123.", calling reverse("") would return "abc, XYZ; 123."
	 * - For a current string "", calling reverse("") would return ""
	 * 
	 * Remember: This method builds and returns a new string, and does not directly modify the myString field.
	 * 
	 * @param arg the string containing the alphabetical characters to have their capitalization reversed in the current string
	 * @return new string in which the alphabetical characters specified in the arg are reversed
	 */
	public String reverse(String arg) {
		// TODO Implement method

		//make an empty RemovedStrings and ArrayOfReversedtrings for containing

		//if string is not null or isSet is not False
		if (myString != null && isSet != false) {
			int size = this.myString.length();
			String ReversedStrings = "";
			char[] arrayOfReversedStrings = new char[size];

			//make arrays of arguments and strings to compare
			char[] arrayOfArg = arg.toCharArray();   
			char[] arrayOfStrings = myString.toCharArray();

			//let's start with strings array
			for (int i=0; i<size; i++){
				int cnt = 0;

				//if string component is the letter
				if (Character.isLetter(arrayOfStrings[i]) == true){

					//let's do argument loop to check
					for (int j=0; j<arg.length(); j++){

						// if there's a match between string and argument
						if(arrayOfStrings[i] == arrayOfArg[j]){

							//and string is lower case
							if(Character.isLowerCase(arrayOfStrings[i]) == true){
								//change it to upper case and append to new array
								char Upper = Character.toUpperCase(arrayOfStrings[i]);
								arrayOfReversedStrings[cnt] = Upper;
								cnt++;
							}

							//string is upper case
							else{
								//change it to lower case and append it of new array
								char Lower = Character.toLowerCase(arrayOfStrings[i]);
								arrayOfReversedStrings[cnt] = Lower;
								cnt++;
							}
						}
						else {continue;}
					}
				}// end of argument for loop to compare strings and arguments
				else {
					// if it's not a letter, always append to new array
					arrayOfReversedStrings[cnt] = arrayOfStrings[i];
					cnt++;
				}
			}
			//since it's the end of for loop, we're gonna make strings from new array
			ReversedStrings = String.valueOf(arrayOfReversedStrings);
			return ReversedStrings;
		}
		
		else {
			String ReversedStrings = "";
			return ReversedStrings;
		}
	}

	/**
	 * Returns a new string version of the current string where all the letters either >= or <= the given char n, are removed.  
	 * 
	 * The given letter may be a-z or A-Z, inclusive.
	 * The letters to be removed are case insensitive.
	 *
	 * If 'more' is false, all letters less than or equal to n will be removed in the returned string.
	 * If 'more' is true, all letters greater than or equal to n will be removed in the returned string.
	 *
	 * If the current string is null, the method should return an empty string.
	 * If n is not a letter (and the current string is not null), the method should return an empty string.
	 *
	 * Example(s):
	 * - For a current string "Hello 90, bye 2", calling filterLetters('h', false) would return "llo 90, y 2"
	 * - For a current string "Abcdefg", calling filterLetters('c', false) would return "defg"
	 * - For a current string "Hello 90, bye 2", calling filterLetters('h', true) would return "e 90, be 2"
	 * - For a current string "Abcdefg", calling filterLetters('c', true) would return "Ab"
	 * 
	 * Remember: This method builds and returns a new string, and does not directly modify the myString field.
	 *
	 * @param n char to compare to
	 * @param more indicates whether letters <= or >= n will be removed
	 * @return new string with letters removed 
	 */
	public String filterLetters(char n, boolean more) {
		// TODO Implement method

		//if string is not null or isSet is not False
		if (myString != null && isSet !=false) {
			int size = myString.length();
			String FilteredStrings = "";
			char[] arrayOfFilteredStrings = new char[size];
			
			
			int cnt = 0;

			//make arrays of arguments and strings to compare
			char[] arrayOfStrings = myString.toCharArray();

			//let's start with strings array
			for (int i=0; i<size; i++){
				if(Character.isLetter(arrayOfStrings[i])==true){
					//let's check the status of more
					//if more is false
					if (more == false) {
						// and string is less or equal to n
						if (arrayOfStrings[i]<=n){
							continue; // don't append it
						}
						// string is over than n, append it
						else{
							//arrayOfStrings.append(arrayOfFilteredStrings);
							arrayOfFilteredStrings[cnt] = arrayOfStrings[i];
							cnt++;
						}
					}
					else{
						if (arrayOfStrings[i]>=n){
							continue; // don't append it
						}
						// string is over than n, append it
						else{
							arrayOfFilteredStrings[cnt] = arrayOfStrings[i];
							cnt++;
						}
					}                                
				} // end of IF to check it's letter or not
				else {
					arrayOfFilteredStrings[cnt] = arrayOfStrings[i];
					cnt++;
				}

			}// end of FOR loop to check each component of string

			//need to transform array to string
			FilteredStrings = String.valueOf(arrayOfFilteredStrings);
			return FilteredStrings;

		}// end of IF to check if the string is null or not
		//return empty string if it's null string
		else {
			String FilteredStrings = "";
			return FilteredStrings;
		}

	} // end of method
	
	public static void main(String[] arg){
		setString("ddd");
	}
}