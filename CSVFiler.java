//Phil Prosapio, Andrew ID: pprosapi
package hw3;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

//CSV reader class to handle CSV input
public class CSVFiler extends DataFiler {
	
	@Override
	public void writeFile(String filename) {
		// TODO Auto-generated method stub
		// Saving this till HW3
	}

	@Override
	public boolean readFile(String filename) {
		try {
			//Initialize objects for method
			File file = new File(filename);
			Scanner fileScan = new Scanner(file);
			String line = fileScan.nextLine();
			try{
				//Call validation check
				NutriByte.person = validatePersonData(line);
			}catch(InvalidProfileException e) {
				fileScan.close();
				throw new InvalidProfileException("Person unable to be created");
			}
			try {
				while(fileScan.hasNext()) {
					line = fileScan.nextLine();
					NutriByte.person.dietProductsList.add(validateProductData(line)); //this should throw an error for the catch to handle
				}
			}catch(InvalidProfileException e) {
				
			}catch(NumberFormatException e) {
				System.out.println("The row with the following data has some invalid data: " + line);
			}finally {
				NutriByte.view.dietProductsTableView.setItems(NutriByte.person.dietProductsList);
				NutriByte.person.populateDietNutrientMap();
				NutriByte.view.nutriChart.updateChart();
			}
			fileScan.close();
			return true;
		}catch(FileNotFoundException e) {
			e.printStackTrace();
			return false;
		}
	}
	
	//Need to code this one
	public Person validatePersonData(String data) {
		String[] elements = data.split(",");
		StringBuilder food2Watch = new StringBuilder();
		Person peep;
		float age, weight, height, pAct;
		//Handle gender for line
		if(elements[0].toUpperCase().equals("FEMALE")) {
			//Collect the ingredients/foods to watch out for into a StringBuilder object
			for(int i = 5; i < elements.length; i++) {
				if(i == 5) {
					food2Watch.append(elements[i].trim());
				}else {
					food2Watch.append(", " + elements[i].trim());
				}
			}
			//Create female object based on file input, with added error handling
			try {
				age = Float.parseFloat(elements[1]);
			}catch(NumberFormatException e) {
				throw new InvalidProfileException("Invalid Age in File: " + elements[1]);
			}
			try {
				weight = Float.parseFloat(elements[2]);
			}catch(NumberFormatException e) {
				throw new InvalidProfileException("Invalid Weight in File: " + elements[2]);
			}
			try {
				height = Float.parseFloat(elements[3]);
			}catch(NumberFormatException e) {
				throw new InvalidProfileException("Invalid Height in File: " + elements[3]);
			}
			try {
				pAct = Float.parseFloat(elements[4]);
				System.out.println(pAct);
				if(pAct != 1.0f && pAct != 1.1f && pAct != 1.25f && pAct != 1.48f) {
					throw new InvalidProfileException("Invalid Physical Activity In File: " + elements[4]);
				}
			}catch(NumberFormatException e) {
				throw new InvalidProfileException("Invalid Physical Activity In File: " + elements[4]);
			}
			peep = new Female(age, weight, height, pAct, food2Watch.toString());
		}else {
			//Collect the ingredients/foods to watch out for into a StringBuilder object
			for(int i = 5; i < elements.length; i++) {
				if(i == 5) {
					food2Watch.append(elements[i].trim());
				}else {
					food2Watch.append(", " + elements[i].trim());
				}
			}
			//Create male object based on file input, with added error handling
			try {
				age = Float.parseFloat(elements[1]);
			}catch(NumberFormatException e) {
				throw new InvalidProfileException("Invalid Age in File: " + elements[1]);
			}
			try {
				weight = Float.parseFloat(elements[2]);
			}catch(NumberFormatException e) {
				throw new InvalidProfileException("Invalid Weight in File: " + elements[2]);
			}
			try {
				height = Float.parseFloat(elements[3]);
			}catch(NumberFormatException e) {
				throw new InvalidProfileException("Invalid Height in File: " + elements[3]);
			}
			try {
				pAct = Float.parseFloat(elements[4]);
				if(pAct != 1.0f && pAct != 1.1f && pAct != 1.25f && pAct != 1.48f) {
					throw new InvalidProfileException("Invalid Physical Activity In File: " + elements[4]);
				}
			}catch(NumberFormatException e) {
				throw new InvalidProfileException("Invalid Physical Activity In File: " + elements[4]);
			}
			peep = new Male(age, weight, height, pAct, food2Watch.toString());
		}
		return peep;
	}
	
	public Product validateProductData(String data) {
		String[] elements = data.split(",");
		System.out.println(elements[0]);
		Product prod;
		try{
			prod = Model.productsMap.get(elements[0]);
			prod.setServingSize(Float.parseFloat(elements[1]));
			prod.setHouseholdSize(Float.parseFloat(elements[2]));
		}catch(IndexOutOfBoundsException e) {
			throw new InvalidProfileException("One or more line in the file has invalid data in it.");
		}catch(NumberFormatException e) {
			throw new InvalidProfileException("One or more line in the file has invalid data in it.");
		}
		return prod;
	}
}
