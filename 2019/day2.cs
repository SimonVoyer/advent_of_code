
using System;
using System.IO;
using System.Text;


namespace Advent2019 {
	
	class Day2 {

		public const int Add = 1;
		public const int Multiply = 2;
		public const int Halt = 99;
		public const int NounVerbMaxValue = 99;
		public const int TargetOutput = 19690720;


		public static void Main(string[] args) {
			int[] intcodeProgram = Day2.CompileIntcodeProgram("input/day2.txt");
			Console.WriteLine(String.Format("Output of Intcode program with noun = 12 and verb = 2 is {0}.", ExecuteIntcodeProgram(intcodeProgram, 12, 2)));
			Console.WriteLine(String.Format("For the noun and verb that output {0}, 100 * noun + verb = {1}.", TargetOutput, CrackProgram(intcodeProgram)));
		}


		/// <summary>
    	/// Compiles the Intcode program from the input file.
    	/// </summary>
		public static int[] CompileIntcodeProgram(string filePath){
			String line = File.ReadAllText(filePath, Encoding.UTF8);
			String[] characters = line.Split(',');
			int[] intcodeProgram = new int[characters.Length];
			for (int i = 0; i < characters.Length; i++){
				Int32.TryParse(characters[i], out intcodeProgram[i]);
			}
			return intcodeProgram;
		}


		/// <summary>
    	/// Executes the Intcode program and returns the output (position 0 integer).
		/// Note that baseIntcodeProgram is not modified by this operation.
		/// An exception is thrown if an invalid opcode is found within the program.
    	/// </summary>
		public static int ExecuteIntcodeProgram(int[] baseIntcodeProgram, int noun, int verb){
			int[] intcodeProgram = new int[baseIntcodeProgram.Length];
			Array.Copy(baseIntcodeProgram, intcodeProgram, intcodeProgram.Length);

			//Restore the gravity assist program to the 1202 program alert
			intcodeProgram[1] = noun;
			intcodeProgram[2] = verb;

			//Execute program
			int programCounter = 0;

			while (programCounter < intcodeProgram.Length){
				int opCode = intcodeProgram[programCounter++];
				if (opCode == Halt){
					break;
				} else {
					//Values 1 and 2 are found at the positions defined by the 2 following integers
					int value1 = intcodeProgram[intcodeProgram[programCounter++]];
					int value2 = intcodeProgram[intcodeProgram[programCounter++]];

					int registerPosition = intcodeProgram[programCounter++];

					switch(opCode) 
					{
					case Add:
						intcodeProgram[registerPosition] = value1 + value2;
						break;
					case Multiply:
						intcodeProgram[registerPosition] = value1 * value2;
						break;
					default:
						throw new InvalidOperationException(String.Format("Opcode {0} is undefined. Program terminated.", opCode));
					}
				}
			}
			return intcodeProgram[0];
		}


	/// <summary>
    /// Brute forces the Intcode program to find the noun and verb that output the TargetOutput.
	/// Since noun and verb are elements of integer set {0,99}, there are only 100^2 possibilities, making
	/// brute force extremely fast. Returned value is  100 * noun + verb.
	/// Note that intcodeProgram is not modified by this operation.
	/// It is expected for the program to be able to return the TargetOutput. If it's not possible, an exception 
	/// is thrown, as it means that either or both of the parameters are invalid.
    /// </summary>
	public static int CrackProgram(int[] intcodeProgram){
		for (int noun = 0; noun <= NounVerbMaxValue; noun++){
			for (int verb = 0; verb <= NounVerbMaxValue; verb++){
				if (ExecuteIntcodeProgram(intcodeProgram, noun, verb) == TargetOutput){
					return 100 * noun + verb;
				}
			}
		}
		throw new ArgumentException("Target output is impossible to compute with this program.");
	}

	}
}
