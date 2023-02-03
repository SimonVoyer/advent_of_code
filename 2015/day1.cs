
using System;
using System.IO;
using System.Text;
using System.Linq;


namespace Advent2015 {
	
	class Day1 {
		
		const char UpSymbol = '(';
		const char DownSymbol = ')';
		const int Basement = -1;


		public static void Main(string[] args) {
			String instructions = File.ReadAllText("input/day1.txt", Encoding.UTF8);
			Console.WriteLine(String.Format("The floor Santa is looking for is {0}.", instructions.Count(x => x == UpSymbol) - instructions.Count(x => x == DownSymbol)));
			Console.WriteLine(String.Format("The position where the instructions lead Santa to the basement for this first time is {0}.", FindFirstBasementInstruction(instructions)));
		}


		/// <summary>
    	/// Returns the first position where the sequence of instructions would lead Santa into the basement of the apartment.
		/// Any instructions passed to this method needs to lead to the basement at least once.
		/// As such, an exception is thrown if the basement isn't found.
    	/// </summary>
		public static int FindFirstBasementInstruction(String instructions){
			char[] instructionsArray = instructions.ToCharArray();
			int levelCounter = 0;
			for (int i = 0; i < instructionsArray.Length; i++){

				if (instructionsArray[i] == UpSymbol){
					levelCounter++;
				} else { //instructionsArray[i] == DownSymbol
					levelCounter--;
				}

				if (levelCounter == Basement){
					//instructions are counted starting from 1, unlike i
					return i+1;
				}
			}
			throw new ArgumentException("The instructions need to lead to the basement at least once.");
		}
	}
}
