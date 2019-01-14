//Phil Prosapio, Andrew ID: pprosapi
package hw3;

//Java Bean property types needed for this class
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;

public class Nutrient {
	
	//Initialize private property variables
	private final StringProperty nutrientCode = new SimpleStringProperty();
	private final StringProperty nutrientName = new SimpleStringProperty();
	private final StringProperty nutrientUom = new SimpleStringProperty();
	
	//Default constructor for this class to initialize variables
	public Nutrient() {
		nutrientCode.set("");
		nutrientName.set("");
		nutrientUom.set("");
	}
	
	//Non-default constructor for this class to initialize variables
	public Nutrient(String nc, String nn, String nu) {
		nutrientCode.set(nc);
		nutrientName.set(nn);
		nutrientUom.set(nu);
	}
	
	//All getters for this class
	public final String getNutrientCode() { return nutrientCode.get(); }
	public final String getNutrientName() { return nutrientName.get(); }
	public final String getNutrientUom() { return nutrientUom.get(); }
				
	//All setters for this class
	public final void setNutrientCode(String in) { this.nutrientCode.set(in); }
	public final void setNutrientQuantity(String in) { this.nutrientName.set(in); }
	public final void setNutrientUom(String in) { this.nutrientUom.set(in); }
				
	//All property getters for this class
	public final StringProperty nutrientCodeProperty() { return nutrientCode; }
	public final StringProperty nutrientNameProperty() { return nutrientName; }
	public final StringProperty nutrientNameUom() { return nutrientUom; }
}
