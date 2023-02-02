
using System;
using System.IO;
using System.Text;


namespace Advent2019 {
	
	class Day4 {

		const int LowerBound = 137683;
		const int UpperBound = 596253;
		
		public static void Main(string[] args) {
			Console.WriteLine(String.Format("The number of acceptable passwords between {0} and {1} is {2}.", LowerBound, UpperBound, CountAcceptablePasswords(false)));
			Console.WriteLine(String.Format("The number of acceptable passwords (with more severe rules) between {0} and {1} is {2}.", LowerBound, UpperBound, CountAcceptablePasswords(true)));
		}


		/// <summary>
    	/// Counts the number of acceptable passwords between the LowerBound and the Upperbound.
		/// Acceptable passwords have 6 digits that are, from left to right, never decreasing.
		/// They must also have at least 2 adjacent digits that are the same. 
		/// The only 2 adjacent rule means that any repeating digits in groups larger than 2 don't count.
    	/// </summary>
		public static int CountAcceptablePasswords(bool isOnly2AdjacentRule){
			int acceptablePasswordCounter = 0;
			for (int passwordCandidate = LowerBound; passwordCandidate <= UpperBound; passwordCandidate++){
				
				char[] passwordDigits = passwordCandidate.ToString().ToCharArray();
				bool is2AdjacentSame = false;
				bool isNeverDescrease = true;
				
				for (int j = 0; j < passwordDigits.Length-1; j++){
					if (passwordDigits[j] > passwordDigits[j+1]){
						isNeverDescrease = false;
						break;
					} else if (passwordDigits[j] == passwordDigits[j+1] && !is2AdjacentSame){
						//Note that entering this branch while is2AdjacentSame == true would change results
						if (isOnly2AdjacentRule){
							bool previousDigitDifferent = j == 0 || passwordDigits[j] != passwordDigits[j-1];
							bool nextDigitDifferent = j+2 >= passwordDigits.Length || passwordDigits[j+1] != passwordDigits[j+2];
							is2AdjacentSame = previousDigitDifferent && nextDigitDifferent;
						} else {
							is2AdjacentSame = true;
						}
						
					}
				}

				if (isNeverDescrease && is2AdjacentSame){
					acceptablePasswordCounter++;
				}

			}
			return acceptablePasswordCounter;
		}
	}
}
