//Phil Prosapio, Andrew ID: pprosapi
package hw3;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.beans.binding.ObjectBinding;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.value.ObservableValue;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.collections.ObservableMap;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.TableColumn.CellDataFeatures;
import javafx.scene.control.TextField;
import javafx.scene.layout.Background;
import javafx.scene.layout.BackgroundFill;
import javafx.scene.layout.CornerRadii;
import javafx.scene.paint.Color;
import javafx.stage.Stage;
import javafx.util.Callback;

public class NutriByte extends Application{
	static Model model = new Model();  	//made static to make accessible in the controller
	static View view = new View();		//made static to make accessible in the controller
	static Person person;				//made static to make accessible in the controller
	
	
	Controller controller = new Controller();	//all event handlers 

	/**Uncomment the following three lines if you want to try out the full-size data files */
//	static final String PRODUCT_FILE = "data/Products.csv";
//	static final String NUTRIENT_FILE = "data/Nutrients.csv";
//	static final String SERVING_SIZE_FILE = "data/ServingSize.csv";
	
	/**The following constants refer to the data files to be used for this application */
	static final String PRODUCT_FILE = "data/Nutri2Products.csv";
	static final String NUTRIENT_FILE = "data/Nutri2Nutrients.csv";
	static final String SERVING_SIZE_FILE = "data/Nutri2ServingSize.csv";
	
	static final String NUTRIBYTE_IMAGE_FILE = "NutriByteLogo.png"; //Refers to the file holding NutriByte logo image 

	static final String NUTRIBYTE_PROFILE_PATH = "profiles";  //folder that has profile data files

	static final int NUTRIBYTE_SCREEN_WIDTH = 1015;
	static final int NUTRIBYTE_SCREEN_HEIGHT = 675;

	//Start method with all initialization
	@Override
	public void start(Stage stage) throws Exception {
		model.readProducts(PRODUCT_FILE);
		model.readNutrients(NUTRIENT_FILE);
		model.readServingSizes(SERVING_SIZE_FILE );
		view.setupMenus();
		view.setupNutriTrackerGrid();
		view.root.setCenter(view.setupWelcomeScene());
		Background b = new Background(new BackgroundFill(Color.WHITE, CornerRadii.EMPTY, Insets.EMPTY));
		view.root.setBackground(b);
		Scene scene = new Scene (view.root, NUTRIBYTE_SCREEN_WIDTH, NUTRIBYTE_SCREEN_HEIGHT);
		view.root.requestFocus();  //this keeps focus on entire window and allows the textfield-prompt to be visible
		setupBindings();
		//Change Listener is attached here so that I can keep my table bindings up to date. This ensures eager evaluation occurs
		tableBinding.addListener((observable, oldValue, newValue) -> {}	);  
		controller.comboBoxBinding.addListener((observable, oldValue, newValue) -> {} );
		stage.setTitle("NutriByte 3.0");
		stage.setScene(scene);
		stage.show();
	}

	public static void main(String[] args) {
		launch(args);
	}

	//Majority of binding occurs here
	void setupBindings() {
		//Menu button bindings via setOnAction
		view.newNutriProfileMenuItem.setOnAction(controller.new NewMenuItemHandler());
		view.openNutriProfileMenuItem.setOnAction(controller.new OpenMenuItemHandler());
		view.closeNutriProfileMenuItem.setOnAction(controller.new CloseMenuItemHandler());
		view.saveNutriProfileMenuItem.setOnAction(controller.new SaveMenuItemHandler());
		view.exitNutriProfileMenuItem.setOnAction(event -> Platform.exit());
		view.aboutMenuItem.setOnAction(controller.new AboutMenuItemHandler());
		
		//CellValueFactory calls
		view.recommendedNutrientNameColumn.setCellValueFactory(recommendedNutrientNameCallback);
		view.recommendedNutrientQuantityColumn.setCellValueFactory(recommendedNutrientQuantityCallback);
		view.recommendedNutrientUomColumn.setCellValueFactory(recommendedNutrientUomCallback);
		
		view.productNutrientNameColumn.setCellValueFactory(productNutrientNameCallback);
		view.productNutrientQuantityColumn.setCellValueFactory(productNutrientQuantityCallback);
		view.productNutrientUomColumn.setCellValueFactory(productNutrientUomCallback);

		//Button binding via setOnAction
		view.createProfileButton.setOnAction(controller.new RecommendNutrientsButtonHandler());
		view.clearButton.setOnAction(controller.new ClearButtonHandler());
		view.searchButton.setOnAction(controller.new SearchButtonHandler());
		view.addDietButton.setOnAction(controller.new AddDietButtonHandler());
		view.removeDietButton.setOnAction(controller.new RemoveDietButtonHandler());
	}
	
	
	//I have the binding set up to dynamically react when I do things in the text fields, just no idea how to get the table updated.
	ObjectBinding<String> tableBinding = new ObjectBinding<String>() {
		{
			super.bind(view.ageTextField.textProperty(), view.weightTextField.textProperty(), view.heightTextField.textProperty(), view.physicalActivityComboBox.valueProperty(), view.genderComboBox.valueProperty());
		}

		@Override
		protected String computeValue() {
			//Initialize variables and textfield variable
			float age = 0, weight = 0, height = 0, pActF = 0.0f;
			String gender = view.genderComboBox.getValue();
			String pAct = NutriByte.view.physicalActivityComboBox.getValue();
			TextField textField = view.ageTextField;
			ObservableList<Product> tempProducts = FXCollections.observableArrayList();
			ObservableMap<String, RecommendedNutrient> rnMap = FXCollections.observableHashMap();
			try {
				//Save off the diet list and maps for later use
				tempProducts = NutriByte.person.dietProductsList;
				rnMap = NutriByte.person.dietNutrientsMap;
			}catch(Exception e){}
	
			boolean fail = false;
			
			try {
				//Translate physical activity combo box input into float 
				if(pAct.equals("Sedentary")) {
					pActF = 1.0f;
				} else if (pAct.equals("Low active")) {
					pActF = 1.1f;
				} else if (pAct.equals("Active")) {
					pActF = 1.25f;
				} else if (pAct.equals("Very active")) {
					pActF = 1.48f;
				}
			}catch(NullPointerException e){
				//Hold
			}
				
			//Handle coloring
			textField.setStyle("-fx-text-inner-color: black;");
			if(!NutriByte.view.ageTextField.getText().isEmpty()) {
				try {
					age = Float.parseFloat(textField.getText().trim());
				}catch(NumberFormatException e) {
					textField.setStyle("-fx-text-inner-color: red;");
					fail = true;
				}
				if(age < 0) {
					textField.setStyle("-fx-text-inner-color: red;");
					fail = true;
				}
			}else {
				fail = true;
			}

			textField = view.weightTextField;
			textField.setStyle("-fx-text-inner-color: black;");
			if(!NutriByte.view.weightTextField.getText().isEmpty()) {
				try {
					weight = Float.parseFloat(textField.getText().trim());
				}catch(NumberFormatException e) {
					textField.setStyle("-fx-text-inner-color: red;");
					fail = true;
				}
				
				if(weight < 0) {
					textField.setStyle("-fx-text-inner-color: red;");
					fail = true;
				}
			}else {
				fail = true;
			}
			
			textField = view.heightTextField;
			textField.setStyle("-fx-text-inner-color: black;");
				
			if(!NutriByte.view.heightTextField.getText().isEmpty()) {
				try {
					height = Float.parseFloat(textField.getText().trim());
				}catch(NumberFormatException e) {
					textField.setStyle("-fx-text-inner-color: red;");
					fail = true;
				}
				
				if(height < 0) {
					textField.setStyle("-fx-text-inner-color: red;");
					fail = true;
				}
			}else {
				fail = true;
			}
				
			//Check gender box
			if(gender == null) {
				return null;
			}
			
			if(fail) {
				return null;
			}
			
			//Either make new person object or update current one
			if(!(NutriByte.person == null)) {
				if(NutriByte.person instanceof Female) {
					if(gender.toUpperCase().equals("FEMALE")) {
						NutriByte.person.age = age;
						NutriByte.person.weight = weight;
						NutriByte.person.height = height;
						NutriByte.person.physicalActivityLevel = pActF;
						NutriByte.person.ingredientsToWatch = NutriByte.person.ingredientsToWatch;
					}else {
						NutriByte.person = new Male(age, weight, height, pActF, NutriByte.view.ingredientsToWatchTextArea.getText());
					} 
				}else if(NutriByte.person instanceof Male) {
					if(gender.toUpperCase().equals("MALE")) {
						NutriByte.person.age = age;
						NutriByte.person.weight = weight;
						NutriByte.person.height = height;
						NutriByte.person.physicalActivityLevel = pActF;
						NutriByte.person.ingredientsToWatch = NutriByte.person.ingredientsToWatch;
					}else {
						NutriByte.person = new Female(age, weight, height, pActF, NutriByte.view.ingredientsToWatchTextArea.getText());
					}
				} 
			}else {
				if(gender.toUpperCase().equals("MALE")) {
					NutriByte.person = new Male(age, weight, height, pActF, NutriByte.view.ingredientsToWatchTextArea.getText());
				}else {
					NutriByte.person = new Female(age, weight, height, pActF, NutriByte.view.ingredientsToWatchTextArea.getText());
				}
			}
			try {
				NutriByte.person.dietNutrientsMap = rnMap;
				NutriByte.person.dietProductsList = tempProducts;
			}catch(NullPointerException e) {}
			
			
			System.out.println("udpate?");
			//Populate recommendedNutrientsList via the createNutriProfile method and bind that data to the table
			NutriProfiler.createNutriProfile(NutriByte.person);
			NutriByte.view.recommendedNutrientsTableView.setItems(NutriByte.person.recommendedNutrientsList);
			NutriByte.view.nutriChart.updateChart();
			return null;
		}
	};
	
	//Callback for recommended nutrient name, was hard coded for us
	Callback<CellDataFeatures<RecommendedNutrient, String>, ObservableValue<String>> recommendedNutrientNameCallback = new Callback<CellDataFeatures<RecommendedNutrient, String>, ObservableValue<String>>() {
		@Override
		public ObservableValue<String> call(CellDataFeatures<RecommendedNutrient, String> arg0) {
			Nutrient nutrient = Model.nutrientsMap.get(arg0.getValue().getNutrientCode());
			return nutrient.nutrientNameProperty();
		}
	};
	
	//Callback for recommended nutrient quantity
	Callback<CellDataFeatures<RecommendedNutrient, String>, ObservableValue<String>> recommendedNutrientQuantityCallback = new Callback<CellDataFeatures<RecommendedNutrient, String>, ObservableValue<String>>() {
		@Override
		public ObservableValue<String> call(CellDataFeatures<RecommendedNutrient, String> arg0) {
			for(RecommendedNutrient rn : NutriByte.person.recommendedNutrientsList) {
				if(rn.getNutrientCode().equals(arg0.getValue().getNutrientCode())) {
					//Handle formating down to two decimals for quantity
					return new SimpleStringProperty(String.format("%.2f", rn.getNutrientQuantity()));
				}
			}
			return null; 
		}
	};
	
	//Callback for recommended nutrient uom
	Callback<CellDataFeatures<RecommendedNutrient, String>, ObservableValue<String>> recommendedNutrientUomCallback = new Callback<CellDataFeatures<RecommendedNutrient, String>, ObservableValue<String>>() {
		@Override
		public ObservableValue<String> call(CellDataFeatures<RecommendedNutrient, String> arg0) {
			Nutrient nutrient = Model.nutrientsMap.get(arg0.getValue().getNutrientCode());
			return nutrient.nutrientNameUom();
		}
	};
	
	//Callback for for found product's nutrients name
	Callback<CellDataFeatures<Product.ProductNutrient, String>, ObservableValue<String>> productNutrientNameCallback = new Callback<CellDataFeatures<Product.ProductNutrient, String>, ObservableValue<String>>() {
		@Override
		public ObservableValue<String> call(CellDataFeatures<Product.ProductNutrient, String> arg0) {
			return Model.nutrientsMap.get(arg0.getValue().getNutrientCode().toString().trim()).nutrientNameProperty();
		}
	};
		
	//Callback for found product's nutrients quantity
	Callback<CellDataFeatures<Product.ProductNutrient, String>, ObservableValue<String>> productNutrientQuantityCallback = new Callback<CellDataFeatures<Product.ProductNutrient, String>, ObservableValue<String>>() {
		@Override
		public ObservableValue<String> call(CellDataFeatures<Product.ProductNutrient, String> arg0) {
			return new SimpleStringProperty(String.format("%.2f", arg0.getValue().getNutrientQuantity())); 
		}
	};
		
	//Callback for found product's nutrients uom
	Callback<CellDataFeatures<Product.ProductNutrient, String>, ObservableValue<String>> productNutrientUomCallback = new Callback<CellDataFeatures<Product.ProductNutrient, String>, ObservableValue<String>>() {
		@Override
		public ObservableValue<String> call(CellDataFeatures<Product.ProductNutrient, String> arg0) {
			return Model.nutrientsMap.get(arg0.getValue().getNutrientCode().toString().trim()).nutrientNameUom();
		}
	};
}