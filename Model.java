package hw3;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.collections.ObservableMap;

public class Model {
	
	//Initialize my two Hash maps to house product and nutrient objects
	public static ObservableMap<String, Product> productsMap = FXCollections.observableHashMap();
	public static ObservableMap<String, Nutrient> nutrientsMap = FXCollections.observableHashMap();
	
	public ObservableList<Product> searchResultsList = FXCollections.observableArrayList();
	
	//Read in product info from files
	public void readProducts(String filename) {
		try {
			//Set up file reading objects
			FileReader file = new FileReader(filename);
			Scanner fileScan = new Scanner(file);
			String[] elements;
			fileScan.nextLine(); //Flush out the first line of the file
			String line = "";
			
			//Loop through file and populate two Map files
			while(fileScan.hasNextLine()) {
				line = fileScan.nextLine();
				elements = line.split("\",\"");
				//Initialize product info to be added to the map
				Product prod = new Product(elements[0].substring(1), elements[1], elements[4], elements[7]);
				productsMap.put(elements[0].substring(1), prod);
			}
			fileScan.close();
		} catch(FileNotFoundException e) {
			e.printStackTrace();
		}
	}
	
	//Read in nutrient info from files
	public void readNutrients(String filename) {
		try {
			//Set up file reading objects
			FileReader file = new FileReader(filename);
			Scanner fileScan = new Scanner(file);
			String[] elements;
			fileScan.nextLine(); //Flush out the first line of the file
			String line = "";
			
			//Loop through file and populate two Map files
			while(fileScan.hasNextLine()) {
				line = fileScan.nextLine();
				elements = line.split("\",\"");
				//Initialize nutrient info to be added to the map
				Nutrient nut = new Nutrient(elements[1], elements[2], elements[5].substring(0, (elements[5].length()-1)));
				nutrientsMap.put(elements[1], nut);
				Product tempProd = new Product();
				
				//Create ProductNutrient objects seperately
				Product.ProductNutrient pn = tempProd.new ProductNutrient(elements[1], Float.parseFloat(elements[4]));
				if(elements[4].equals("0.0")) {
					continue;
				}else {
					productsMap.get(elements[0].substring(1)).productNutrients.put(elements[1], pn);
				}
			}
			fileScan.close();
		} catch(FileNotFoundException e) {
			e.printStackTrace();
		}
	}
	
	//Read in serving size info from files
	public void readServingSizes(String filename) {
		try {
			//Set up file reading objects
			FileReader file = new FileReader(filename);
			Scanner fileScan = new Scanner(file);
			String[] elements;
			fileScan.nextLine(); //Flush out the first line of the file
			String line = "";
			//Loop through file and populate product objects from productsMap with serving size info
			while(fileScan.hasNextLine()) {
				line = fileScan.nextLine();
				elements = line.split("\",\"");
				//Handle values when there is some bad data entry from the file, with error handling built in
				if(elements[1].length() < 1) {
						productsMap.get(elements[0].substring(1)).setServingSize(0.0f);
					try {
						productsMap.get(elements[0].substring(1)).setServingUom(elements[2]);
					} catch(NumberFormatException e) {
						productsMap.get(elements[0].substring(1)).setServingUom("N/A");
					}
					try {
						productsMap.get(elements[0].substring(1)).setHouseholdSize(Float.parseFloat(elements[3]));
					} catch(NumberFormatException e) {
						productsMap.get(elements[0].substring(1)).setHouseholdSize(0.0f);
					}
					try {
						if(productsMap.get(elements[0].substring(1)).getProductName().toUpperCase().equals("NATURADE, PEA PROTEIN VEGAN SHAKE, VANILLA")) {
							productsMap.get(elements[0].substring(1)).setHouseholdUom(elements[4].substring(0, 6));
						}else {
							productsMap.get(elements[0].substring(1)).setHouseholdUom(elements[4]);
						}
					} catch(NumberFormatException e) {
						productsMap.get(elements[0].substring(1)).setHouseholdUom("N/A");
					}
				}else {
					try {
						productsMap.get(elements[0].substring(1)).setServingSize(Float.parseFloat(elements[1]));
					} catch(NumberFormatException e) {
						productsMap.get(elements[0].substring(1)).setServingSize(0.0f);
					}
					try {
						productsMap.get(elements[0].substring(1)).setServingUom(elements[2]);
					} catch(NumberFormatException e) {
						productsMap.get(elements[0].substring(1)).setServingUom("N/A");
					}
					try {
						productsMap.get(elements[0].substring(1)).setHouseholdSize(Float.parseFloat(elements[3]));
					} catch(NumberFormatException e) {
						productsMap.get(elements[0].substring(1)).setHouseholdSize(0.0f);
					}
					try {
						if(productsMap.get(elements[0].substring(1)).getProductName().toUpperCase().equals("NATURADE, PEA PROTEIN VEGAN SHAKE, VANILLA")) {
							productsMap.get(elements[0].substring(1)).setHouseholdUom(elements[4].substring(0, 6));
						}else {
							productsMap.get(elements[0].substring(1)).setHouseholdUom(elements[4]);
						}
					} catch(NumberFormatException e) {
						productsMap.get(elements[0].substring(1)).setHouseholdUom("N/A");
					}
				}
			}
			fileScan.close();
		} catch(FileNotFoundException e) {
			e.printStackTrace();
		}
	}
	
	//Read in the profile files for male/female object creation and screen updating
	public boolean readProfiles(String filename) {
		DataFiler xmlFiler = new XMLFiler();
		DataFiler csvFiler = new CSVFiler();
		try{
			if(filename.contains("xml")) {
				return xmlFiler.readFile(filename);
			}else {
				return csvFiler.readFile(filename);
			}
		}catch(InvalidProfileException e) {
			return false;
		}
	}
	
	//Method to allow users to save their profile data and diet products into a new profile file as a CSV
	public void writeProfile(String filename) {
		CSVFiler csv = new CSVFiler();
		csv.writeFile(filename);
	}
}

