//Phil Prosapio, Andrew ID: pprosapi
package hw3;

//Java Bean property types needed for this class
import javafx.beans.property.StringProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.FloatProperty;
import javafx.beans.property.SimpleFloatProperty;

public class RecommendedNutrient {
	//Initialize property variables
	private final StringProperty nutrientCode = new SimpleStringProperty();
	private final FloatProperty nutrientQuantity = new SimpleFloatProperty();
	
	//Default constructor for this class to initialize variables
	public RecommendedNutrient() {
		nutrientCode.set("");
	}
	
	//Non-default constructor for this class to initialize variables
	public RecommendedNutrient(String nc, float nq) {
		nutrientCode.set(nc);
		nutrientQuantity.set(nq);
	}
	
	//All getters for this class
	public final String getNutrientCode() { return nutrientCode.get(); }
	public final float getNutrientQuantity() { return nutrientQuantity.get(); }
				
	//All setters for this class
	public final void setNutrientCode(String in) { this.nutrientCode.set(in); }
	public final void setNutrientQuantity(float in) { this.nutrientQuantity.set(in); }
				
	//All property getters for this class
	public final StringProperty nutrientCodeProperty() { return nutrientCode; }
	public final FloatProperty nutrientQuantityProperty() { return nutrientQuantity; }
}
