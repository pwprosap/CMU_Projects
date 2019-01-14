//Phil Prosapio, Andrew ID: pprosapi
package hw3;

import javafx.beans.property.FloatProperty;
import javafx.beans.property.SimpleFloatProperty;
import javafx.beans.property.SimpleStringProperty;
//Java Bean property types needed for this class
import javafx.beans.property.StringProperty;
import javafx.collections.FXCollections;
import javafx.collections.ObservableMap;

public class Product {
	
	//Initialize property variables
	protected final StringProperty ndbNumber = new SimpleStringProperty();
	protected final StringProperty productName = new SimpleStringProperty();
	protected final StringProperty manufacturer = new SimpleStringProperty();
	protected final StringProperty ingredients = new SimpleStringProperty();
	protected final FloatProperty servingSize = new SimpleFloatProperty();
	protected final StringProperty servingUom = new SimpleStringProperty();
	protected final FloatProperty householdSize = new SimpleFloatProperty();
	protected final StringProperty householdUom = new SimpleStringProperty();
	
	protected ObservableMap<String, ProductNutrient> productNutrients = FXCollections.observableHashMap();
	
	//Default Constructor that initializes all string properties to empty strings
	public Product() {
		ndbNumber.set("");
		productName.set("");
		manufacturer.set("");
		ingredients.set("");
		servingUom.set("");
		householdUom.set("");
	}
	
	//Non-default constructor to initialize member variables
	public Product(String ndb, String pN, String man, String ing) {
		ndbNumber.set(ndb);
		productName.set(pN);
		manufacturer.set(man);
		ingredients.set(ing);
	}
	
	//Overrides Object's toString() method to return the product name in all caps
	@Override
	public String toString() {
		return this.productName.get().toString().toUpperCase();
	}
	
	//All getters for this class
	public final String getndbNumber() { return ndbNumber.get(); }
	public final String getProductName() { return productName.get(); }
	public final String getManufacturer() { return manufacturer.get(); }
	public final String getIngredients() { return ingredients.get(); }
	public final float getServingSize() { return servingSize.get(); }
	public final String getServingUom() { return servingUom.get(); }
	public final float getHouseholdSize() { return householdSize.get(); }
	public final String getHouseholdUom() { return householdUom.get(); }
	
	//All setters for this class
	public final void setndbNumber(String in) { this.ndbNumber.set(in); }
	public final void setProductName(String in) { this.productName.set(in); }
	public final void setManufacturer(String in) { this.manufacturer.set(in); }
	public final void setIngredients(String in) { this.ingredients.set(in); }
	public final void setServingSize(float in) { this.servingSize.set(in); }
	public final void setServingUom(String in) { this.servingUom.set(in); }
	public final void setHouseholdSize(float in) { this.householdSize.set(in); }
	public final void setHouseholdUom(String in) { this.householdUom.set(in); }
	
	//All property getters for this class
	public final StringProperty ndbNumberProperty() { return ndbNumber; }
	public final StringProperty ProductNameProperty() { return productName; }
	public final StringProperty ManufacturerProperty() { return manufacturer; }
	public final StringProperty IngredientsProperty() { return ingredients; }
	public final FloatProperty ServingSizeProperty() { return servingSize; }
	public final StringProperty servingUomProperty() { return servingUom; }
	public final FloatProperty HouseholdSizeProperty() { return householdSize; }
	public final StringProperty HouseholdUomProperty() { return householdUom; }
	public final ObservableMap<String, ProductNutrient> getProductNutrients( ) { return this.productNutrients;};
	
	//Inner class of ProductNutrient
	public class ProductNutrient {
		
		//Initialize property variables
		protected final StringProperty nutrientCode = new SimpleStringProperty();
		protected final FloatProperty nutrientQuantity = new SimpleFloatProperty();
		
		//Default constructor for the ProductNutrient inner class
		public ProductNutrient() {
			nutrientCode.set("");
		}
		
		//Non-default constructor for the ProductNutrient inner class
		public ProductNutrient(String nc, float nq) {
			nutrientCode.set(nc);
			nutrientQuantity.set(nq);
		}
		
		//All getters for this inner class
		public final String getNutrientCode() { return nutrientCode.get(); }
		public final float getNutrientQuantity() { return nutrientQuantity.get(); }
			
		//All setters for this inner class
		public final void setNutrientCode(String in) { this.nutrientCode.set(in); }
		public final void setNutrientQuantity(float in) { this.nutrientQuantity.set(in); }
			
		//All property getters for this inner class
		public final StringProperty nutrientCodeProperty() { return nutrientCode; }
		public final FloatProperty nutrientQuantityProperty() { return nutrientQuantity; }
	}
}