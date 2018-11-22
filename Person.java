//Phil Prosapio, Andrew ID: pprosapi
package hw3;

import hw3.NutriProfiler.AgeGroupEnum;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.collections.ObservableMap;

public abstract class Person {

	//Define variables for use in class
	float age, weight, height, physicalActivityLevel; //age in years, weight in kg, height in cm
	String ingredientsToWatch;
	float[][] nutriConstantsTable = new float[NutriProfiler.RECOMMENDED_NUTRI_COUNT][NutriProfiler.AGE_GROUP_COUNT];
	
	public ObservableList<RecommendedNutrient> recommendedNutrientsList = FXCollections.observableArrayList();
	public ObservableList<Product> dietProductsList = FXCollections.observableArrayList();
	public ObservableMap<String, RecommendedNutrient> dietNutrientsMap = FXCollections.observableHashMap();

	NutriProfiler.AgeGroupEnum ageGroup;

	//Abstract methods for child class implementation
	abstract void initializeNutriConstantsTable();
	abstract float calculateEnergyRequirement();

	//Explicit Person constructor for initializing variables
	Person(float age, float weight, float height, float physicalActivityLevel, String ingredientsToWatch) {
		this.age = age;
		this.weight = weight;
		this.height = height;
		this.physicalActivityLevel = physicalActivityLevel;
		this.ingredientsToWatch = ingredientsToWatch;
		//Handle age group differences
		if(this.age <= .25) {
			ageGroup = AgeGroupEnum.MAX_AGE_3M;
		} else if(this.age <= .5) {
			ageGroup = AgeGroupEnum.MAX_AGE_6M;
		} else if(this.age <= 1) {
			ageGroup = AgeGroupEnum.MAX_AGE_1Y;
		} else if(this.age <= 3) {
			ageGroup = AgeGroupEnum.MAX_AGE_3Y;
		} else if(this.age <= 8) {
			ageGroup = AgeGroupEnum.MAX_AGE_8Y;
		} else if(this.age <= 13) {
			ageGroup = AgeGroupEnum.MAX_AGE_13Y;
		} else if(this.age <= 18) {
			ageGroup = AgeGroupEnum.MAX_AGE_18Y;
		} else if(this.age <= 30) {
			ageGroup = AgeGroupEnum.MAX_AGE_30Y;
		} else if(this.age <= 50) {
			ageGroup = AgeGroupEnum.MAX_AGE_50Y;
		} else {
			ageGroup = AgeGroupEnum.MAX_AGE_ABOVE;
		}
	}

	//returns an array of nutrient values of size NutriProfiler.RECOMMENDED_NUTRI_COUNT. 
	//Each value is calculated as follows:
	//For Protein, it multiples the constant with the person's weight.
	//For Carb and Fiber, it simply takes the constant from the 
	//nutriConstantsTable based on NutriEnums' nutriIndex and the person's ageGroup
	//For others, it multiples the constant with the person's weight and divides by 1000.
	//Try not to use any literals or hard-coded values for age group, nutrient name, array-index, etc. 
	
	float[] calculateNutriRequirement() {
		float[] nutrients = new float[NutriProfiler.RECOMMENDED_NUTRI_COUNT];
		//For-each loop to handle specific nutrient conversion equations
		for (NutriProfiler.NutriEnum nutriEnum : NutriProfiler.NutriEnum.values()) {
			if (nutriEnum.equals(NutriProfiler.NutriEnum.PROTEIN)) {
				nutrients[nutriEnum.getNutriIndex()] = this.weight * this.nutriConstantsTable[nutriEnum.getNutriIndex()][this.ageGroup.getAgeGroupIndex()];
			} else if(nutriEnum.equals(NutriProfiler.NutriEnum.CARBOHYDRATE) || nutriEnum.equals(NutriProfiler.NutriEnum.FIBER)){
				nutrients[nutriEnum.getNutriIndex()] = this.nutriConstantsTable[nutriEnum.getNutriIndex()][this.ageGroup.getAgeGroupIndex()];
			} else {
				nutrients[nutriEnum.getNutriIndex()] = (this.weight / 1000) * this.nutriConstantsTable[nutriEnum.getNutriIndex()][this.ageGroup.getAgeGroupIndex()];
			}
		}
		return nutrients;
	}
	
	//Takes the data from the dietProducList and populates the dietNutrientsMap
	void populateDietNutrientMap() {
		dietNutrientsMap.clear();
		RecommendedNutrient energy = new RecommendedNutrient(NutriProfiler.ENERGY_NUTRIENT_CODE, 0);
		RecommendedNutrient protein = new RecommendedNutrient(NutriProfiler.NutriEnum.PROTEIN.getNutrientCode(), 0);
		RecommendedNutrient carb = new RecommendedNutrient(NutriProfiler.NutriEnum.CARBOHYDRATE.getNutrientCode(), 0);
		RecommendedNutrient fiber = new RecommendedNutrient(NutriProfiler.NutriEnum.FIBER.getNutrientCode(), 0);
		for (Product prod : NutriByte.person.dietProductsList) { 
			for(Product.ProductNutrient pnut : prod.getProductNutrients().values()) {
				if (pnut.getNutrientCode().equals(NutriProfiler.ENERGY_NUTRIENT_CODE)) {
					energy.setNutrientQuantity(energy.getNutrientQuantity() + (pnut.getNutrientQuantity()*(prod.getServingSize()/100.0f)));
				}else if (pnut.getNutrientCode().equals(NutriProfiler.NutriEnum.PROTEIN.getNutrientCode())) {
					protein.setNutrientQuantity(protein.getNutrientQuantity() + (pnut.getNutrientQuantity()*(prod.getServingSize()/100.0f)));
				}else if (pnut.getNutrientCode().equals(NutriProfiler.NutriEnum.CARBOHYDRATE.getNutrientCode())) {
					carb.setNutrientQuantity(carb.getNutrientQuantity() + (pnut.getNutrientQuantity()*(prod.getServingSize()/100.0f)));
				}else if (pnut.getNutrientCode().equals(NutriProfiler.NutriEnum.FIBER.getNutrientCode())) {
					fiber.setNutrientQuantity(fiber.getNutrientQuantity() + (pnut.getNutrientQuantity()*(prod.getServingSize()/100.0f)));
				}
			}
		}
		dietNutrientsMap.put(NutriProfiler.ENERGY_NUTRIENT_CODE, energy);
		dietNutrientsMap.put(NutriProfiler.NutriEnum.PROTEIN.getNutrientCode(), protein);
		dietNutrientsMap.put(NutriProfiler.NutriEnum.CARBOHYDRATE.getNutrientCode(), carb);
		dietNutrientsMap.put(NutriProfiler.NutriEnum.FIBER.getNutrientCode(), fiber);
	}
}

