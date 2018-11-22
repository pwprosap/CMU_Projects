package hw3;

import hw3.Person;
import hw3.NutriProfiler.AgeGroupEnum;

//Male-person object class
public class Male extends Person{
	
	//Nutrient Constants table for females. Houses the 14 nutrients default values for each age group
	float[][] nutriConstantsTableMale = new float[][]{
		//AgeGroups: 3M, 6M, 1Y, 3Y, 8Y, 13Y, 18Y, 30Y, 50Y, ABOVE 
		{1.52f, 1.52f, 1.2f, 1.05f, 0.95f, 0.95f, 0.73f, 0.8f, 0.8f, 0.8f}, //Protein
		{60, 60, 95, 130, 130, 130, 130, 130, 130, 130}, //Carbohydrate
		{19, 19, 19, 19, 25, 31, 38, 38, 38, 30},       //Fiber 
		{36, 36, 32, 21, 16, 17, 15, 14, 14, 14	},  //Histidine
		{88, 88, 43, 28, 22, 22, 21, 19, 19, 19	}, 	//isoleucine
		{156, 156, 93, 63, 49, 49, 47, 42, 42, 42},//leucine
		{107, 107, 89, 58, 46, 46, 43, 38, 38, 38 },//lysine
		{59, 59, 43, 28, 22, 22, 21, 19, 19, 19	}, 	//methionine 
		{59, 59, 43, 28, 22, 22, 21, 19, 19, 19	}, 	//cysteine
		{135, 135, 84, 54, 41, 41, 38, 33, 33, 33 },//phenylalanine 
		{135, 135, 84, 54, 41, 41, 38, 33, 33, 33 },//tyrosine
		{73, 73, 49, 32, 24, 24, 22, 20, 20, 20}, 	//threonine
		{28, 28, 13, 8, 6, 6, 6, 5, 5, 5}, 			//tryptophan
		{87, 87, 58, 37, 28, 28, 27, 24, 24, 24}  	//valine
	};
	
	//Explicit Male constructor to initialize everything
	Male(float age, float weight, float height, float physicalActivityLevel, String ingredientsToAvoid) {
		super(age, weight, height, physicalActivityLevel, ingredientsToAvoid);
		initializeNutriConstantsTable();
	}

	//Method to calculate the amount of energy a male with the specific age/weight/height needs daily
	@Override
	float calculateEnergyRequirement() {
		//Use correct formula for the age group
		float energy = 0.0f;
		if(this.ageGroup == AgeGroupEnum.MAX_AGE_3M) {
			energy = 89 * this.weight + 75;
		} else if(this.ageGroup == AgeGroupEnum.MAX_AGE_6M) {
			energy = 89 * this.weight - 44;
		} else if(this.ageGroup == AgeGroupEnum.MAX_AGE_1Y) {
			energy = 89 * this.weight - 78;
		} else if(this.ageGroup == AgeGroupEnum.MAX_AGE_3Y) {
			energy = 89 * this.weight - 80;
		} else if(this.ageGroup == AgeGroupEnum.MAX_AGE_8Y || this.ageGroup == AgeGroupEnum.MAX_AGE_13Y || this.ageGroup == AgeGroupEnum.MAX_AGE_18Y) {
			energy = 88.5f - (61.9f * this.age) + this.physicalActivityLevel * (26.7f * this.weight + 903 * this.height / 100) + 20;
		} else if(this.ageGroup == AgeGroupEnum.MAX_AGE_30Y || this.ageGroup == AgeGroupEnum.MAX_AGE_50Y || this.ageGroup == AgeGroupEnum.MAX_AGE_ABOVE) {
			energy = 662 - (9.53f * this.age) + this.physicalActivityLevel * (15.91f * this.weight + 539.6f * this.height / 100);
		}
		return energy;
	}

	//Initialize the nutrients constants table variable.
	@Override
	void initializeNutriConstantsTable() {
		this.nutriConstantsTable = this.nutriConstantsTableMale.clone();
	}
}
