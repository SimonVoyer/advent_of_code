
using System;
using System.IO;
using System.Text;


namespace Advent2019 {
	
	class Day1 {
		
		public static void Main(string[] args) {
			int[] masses = Day1.ParseMasses("input/day1.txt");
			Console.WriteLine(String.Format("The base fuel requirements are {0} units of fuel.", CalculateBaseFuelRequirements(masses)));
			Console.WriteLine(String.Format("The total fuel requirements are {0} units of fuel.", CalculateTotalFuelRequirements(masses)));
		}

		
		private static int FuelCalculation(int mass){
			return mass / 3 - 2;
		}


		/// <summary>
    	/// Parses the masses from the input file.
    	/// </summary>
		public static int[] ParseMasses(string filePath){
			String[] lines = File.ReadAllLines(filePath, Encoding.UTF8);
			int[] masses = new int[lines.Length];
			for (int i = 0; i < lines.Length; i++){
				Int32.TryParse(lines[i], out masses[i]);
			}
			return masses;
		}


		/// <summary>
    	/// Caculates the fuel requirements without taking the fuel's mass into account.
    	/// </summary>
		public static int CalculateBaseFuelRequirements(int[] masses){
			int fuelRequirements = 0;
			for (int i = 0; i < masses.Length; i++){
				fuelRequirements +=  Day1.FuelCalculation(masses[i]);
			}
			return fuelRequirements;
		}


		/// <summary>
    	/// Caculates the fuel requirements while taking into account the fuel's mass.
    	/// </summary>
		public static int CalculateTotalFuelRequirements(int[] masses){
			int fuelRequirements = 0;
			
			for (int i = 0; i < masses.Length; i++){
				int massFuel = Day1.FuelCalculation(masses[i]);
				fuelRequirements += massFuel;
				int fuelFuel =  Day1.FuelCalculation(massFuel);

				while (fuelFuel > 0){
					fuelRequirements += fuelFuel;
					fuelFuel = Day1.FuelCalculation(fuelFuel);
				}
			}
			return fuelRequirements;
		}
	}
}
