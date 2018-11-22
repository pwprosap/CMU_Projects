//Phil Prosapio, Andrew ID: pprosapi
package hw3;

import java.io.File;
import java.util.Iterator;
import java.util.Map;
import java.util.Map.Entry;

import hw3.Product.ProductNutrient;
import javafx.beans.binding.ObjectBinding;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.stage.FileChooser;
import javafx.stage.FileChooser.ExtensionFilter;
import javafx.stage.Stage;

//Controller class to define Button Handler behavior for all GUI buttons
public class Controller {
	
	//Take user entered input/file and recommend nutrients to them
	class RecommendNutrientsButtonHandler implements EventHandler<ActionEvent> {
		@Override
		public void handle(ActionEvent event) {
			//Clear any prior recommendations to ensure everything is good to go
			NutriByte.view.recommendedNutrientsTableView.getItems().clear();
			
			//handle null data
		
			
			//Initialize variables for this method
			float pActF = 1.0f;
			String pAct = NutriByte.view.physicalActivityComboBox.getValue();
			float age = 0.0f;
			float height = 0.0f;
			float weight = 0.0f;
			
			//Ensure that Gender has been selected or don't do anything
			if(NutriByte.view.genderComboBox.getValue() != null) {
				if(NutriByte.view.genderComboBox.getValue().toUpperCase().equals("FEMALE")) {
					//Translate physical activity combo box input into float 
					if(pAct.equals("Sednetary")) {
						pActF = 1.0f;
					} else if (pAct.equals("Low active")) {
						pActF = 1.1f;
					} else if (pAct.equals("Active")) {
						pActF = 1.25f;
					} else if (pAct.equals("Very active")) {
						pActF = 1.48f;
					}
				//Handle null data from users
					try{
						if(NutriByte.view.ageTextField.getText().isEmpty()) {
							throw new InvalidProfileException("Missing age information");
						}
						age = Float.parseFloat(NutriByte.view.ageTextField.getText());
					} catch(NumberFormatException e) {
						throw new InvalidProfileException("Incorrect age input. Must be a number");
					} 

					try {
						if(NutriByte.view.weightTextField.getText().isEmpty()) {
							throw new InvalidProfileException("Missing weight information");
						}
						weight = Float.parseFloat(NutriByte.view.weightTextField.getText());
					} catch(NumberFormatException e) {
						throw new InvalidProfileException("Incorrect weight input. Must be a number");
					}
					
					try {
						if(NutriByte.view.heightTextField.getText().isEmpty()) {
							throw new InvalidProfileException("Missing height information");
						}
						height = Float.parseFloat(NutriByte.view.heightTextField.getText());
					} catch(NumberFormatException e) {
						throw new InvalidProfileException("Incorrect weight input. Must be a number");
					}
					
					//Initialize female object with variables I just populated
					NutriByte.person = new Female(age, weight, height, pActF, NutriByte.view.ingredientsToWatchTextArea.getText());
				} else if (NutriByte.view.genderComboBox.getValue().toUpperCase().equals("MALE")) {
					//Translate physical activity combo box input into float 
					if(pAct.equals("Sednetary")) {
						pActF = 1.0f;
					} else if (pAct.equals("Low active")) {
						pActF = 1.1f;
					} else if (pAct.equals("Active")) {
						pActF = 1.25f;
					} else if (pAct.equals("Very active")) {
						pActF = 1.48f;
					}
					
					try{
						if(NutriByte.view.ageTextField.getText().isEmpty()) {
							throw new InvalidProfileException("Missing age information");
						}
						age = Float.parseFloat(NutriByte.view.ageTextField.getText());
					} catch(NumberFormatException e) {
						throw new InvalidProfileException("Incorrect age input. Must be a number");
					} 
					

					try {
						if(NutriByte.view.weightTextField.getText().isEmpty()) {
							throw new InvalidProfileException("Missing weight information");
						}
						weight = Float.parseFloat(NutriByte.view.weightTextField.getText());
					} catch(NumberFormatException e) {
						throw new InvalidProfileException("Incorrect weight input. Must be a number");
					}

					try {
						if(NutriByte.view.heightTextField.getText().isEmpty()) {
							throw new InvalidProfileException("Missing height information");
						}
						height = Float.parseFloat(NutriByte.view.heightTextField.getText());
					} catch(NumberFormatException e) {
						throw new InvalidProfileException("Incorrect weight input. Must be a number");
					}
				
					//Initialize male object with variables I just populated
					NutriByte.person = new Male(age, weight, height, pActF, NutriByte.view.ingredientsToWatchTextArea.getText());
				} 
				//Populate recommendedNutrientsList via the createNutriProfile method and bind that data to the table
				NutriProfiler.createNutriProfile(NutriByte.person);
				NutriByte.view.recommendedNutrientsTableView.setItems(NutriByte.person.recommendedNutrientsList);
				NutriByte.view.nutriChart.clearChart();
				NutriByte.view.nutriChart.updateChart(); //some error seems to be occurring here
			}else {
				throw new InvalidProfileException("Missing gender information");
			}
		}			
	}

	//Event handler for opening a file and reading in data
	class OpenMenuItemHandler implements EventHandler<ActionEvent> {
		@Override
		public void handle(ActionEvent event) {
			//Initialize variables
			FileChooser fc = new FileChooser();
		    Stage stage = new Stage();
		    NutriByte.view.initializePrompts();
		    //Set up file chooser box settings
			fc.setTitle("Select File");
			fc.setInitialDirectory(new File(NutriByte.NUTRIBYTE_PROFILE_PATH));
			fc.getExtensionFilters().addAll(
					new ExtensionFilter("CSV Files", "*.csv"),
					new ExtensionFilter("XML Files", "*.xml"),
					new ExtensionFilter("All Files", "*.*"));
			File file = null;
			if((file = fc.showOpenDialog(stage)) != null) {
				boolean fileFound = NutriByte.model.readProfiles(file.getAbsolutePath());
				if(fileFound == false) { //Handle failed file
					NutriByte.view.root.setCenter(NutriByte.view.nutriTrackerPane);
				}else {
					//Set GUI background
					NutriByte.view.root.setCenter(NutriByte.view.nutriTrackerPane);
					
					//Set gender combo box value based on file input
					if(NutriByte.person instanceof Female) {
						NutriByte.view.genderComboBox.setValue("Female");
					} else if(NutriByte.person instanceof Male) {
						NutriByte.view.genderComboBox.setValue("Male");
					}
					
					//Handle physical activity input and correctly set dropdown box value
					float pAct = NutriByte.person.physicalActivityLevel;
					if(pAct <= 1f) {
						NutriByte.view.physicalActivityComboBox.setValue("Sedentary");
					} else if (pAct <= 1.1f) {
						NutriByte.view.physicalActivityComboBox.setValue("Low active");
					} else if (pAct <= 1.25f) {
						NutriByte.view.physicalActivityComboBox.setValue("Active");
					} else if (pAct <= 1.48f) {
						NutriByte.view.physicalActivityComboBox.setValue("Very active");
					}
					
					//Set the input values into the different age, weight, height fields and populates the Ingredients to Watch area.
					NutriByte.view.ageTextField.setText(Float.toString(NutriByte.person.age));
					NutriByte.view.weightTextField.setText(Float.toString(NutriByte.person.weight));
					NutriByte.view.heightTextField.setText(Float.toString(NutriByte.person.height));
					NutriByte.view.ingredientsToWatchTextArea.setText(NutriByte.person.ingredientsToWatch);
					
					//Populate recommendedNutrientsList via the createNutriProfile method and bind data to table
					NutriProfiler.createNutriProfile(NutriByte.person);
					NutriByte.view.recommendedNutrientsTableView.setItems(NutriByte.person.recommendedNutrientsList);
				}
			} else {
				NutriByte.view.root.setCenter(NutriByte.view.nutriTrackerPane);
				throw new InvalidProfileException("Error while opening file. Make sure you selected a valid file.");
			}
		}
	}

	//Event handler to bring up a blank data entry screen
	class NewMenuItemHandler implements EventHandler<ActionEvent> {

		@Override
		public void handle(ActionEvent event) {
			//Set starting background and/or clear/reset all data
			NutriByte.view.root.setCenter(NutriByte.view.nutriTrackerPane);
			NutriByte.view.recommendedNutrientsTableView.getItems().clear();
			NutriByte.view.nutriChart.clearChart();
			NutriByte.view.initializePrompts();
			NutriByte.view.servingSizeLabel.setText("0.00");
			NutriByte.view.householdSizeLabel.setText("0.00");
			NutriByte.view.physicalActivityComboBox.setValue("Sedentary");
			}
	}

	//About information event handler, was pre-coded for me
	class AboutMenuItemHandler implements EventHandler<ActionEvent> {
		@Override
		public void handle(ActionEvent event) {
			Alert alert = new Alert(AlertType.INFORMATION);
			alert.setTitle("About");
			alert.setHeaderText("NutriByte");
			alert.setContentText("Version 2.0 \nRelease 1.0\nCopyleft Java Nerds\nThis software is designed purely for educational purposes.\nNo commercial use intended");
			Image image = new Image(getClass().getClassLoader().getResource(NutriByte.NUTRIBYTE_IMAGE_FILE).toString());
			ImageView imageView = new ImageView();
			imageView.setImage(image);
			imageView.setFitWidth(300);
			imageView.setPreserveRatio(true);
			imageView.setSmooth(true);
			alert.setGraphic(imageView);
			alert.showAndWait();
		}
	}
	
	//Event handler to clear product, nutrient and ingredients search text and products combo box.
	class ClearButtonHandler implements EventHandler<ActionEvent> {

		@Override
		public void handle(ActionEvent event) {
			//Clear all values from the Products fields
			NutriByte.view.productSearchTextField.clear();
			NutriByte.view.nutrientSearchTextField.clear();
			NutriByte.view.ingredientSearchTextField.clear();
			NutriByte.view.searchResultSizeLabel.setText("");
			NutriByte.view.productIngredientsTextArea.setText("");
			NutriByte.view.servingSizeLabel.setText("0.00");
			NutriByte.view.householdSizeLabel.setText("0.00");
			NutriByte.view.productNutrientsTableView.setItems(null);
			NutriByte.view.productsComboBox.setItems(null); //Not sure this is how I clear it, but will test
		}
	}
	
	//Handles adding selected product to the diet products table
	class AddDietButtonHandler implements EventHandler<ActionEvent> {

		@Override
		public void handle(ActionEvent event) {
			if(NutriByte.view.productsComboBox.getSelectionModel().getSelectedItem() == null) {
				throw new InvalidProfileException("Invalid Product Info, make sure a product is selected");
			}
			
			//Added this to handle if you have not created a person object yet. I create a dummy person object for use here.
			if(NutriByte.person == null) {
				NutriByte.person = new Male(1, 1, 1, 1, "");
			}
			
			Product selectedProduct = NutriByte.model.searchResultsList.get(NutriByte.view.productsComboBox.getSelectionModel().getSelectedIndex());
			Product customProduct;
			if(NutriByte.view.dietHouseholdSizeTextField.getText().isEmpty() && NutriByte.view.dietServingSizeTextField.getText().isEmpty()) {
				//Neither field populated
				customProduct = selectedProduct;
				NutriByte.person.dietProductsList.add(customProduct);
			}else if(NutriByte.view.dietServingSizeTextField.getText().isEmpty() && !(NutriByte.view.dietHouseholdSizeTextField.getText().isEmpty())) {
				//Just household size entered
				customProduct = new Product(selectedProduct.getndbNumber(), selectedProduct.getProductName(), selectedProduct.getManufacturer(), selectedProduct.getIngredients());
				customProduct.setServingUom(selectedProduct.getServingUom());
				customProduct.setHouseholdUom(selectedProduct.getHouseholdUom());
				customProduct.productNutrients = selectedProduct.productNutrients;
				customProduct.setHouseholdSize(Float.parseFloat(NutriByte.view.dietHouseholdSizeTextField.getText()));
				float ratio = Model.productsMap.get(selectedProduct.getndbNumber()).getServingSize() / Model.productsMap.get(selectedProduct.getndbNumber()).getHouseholdSize();
				customProduct.setServingSize(customProduct.getHouseholdSize() * ratio);
				NutriByte.person.dietProductsList.add(customProduct);
			}else if(NutriByte.view.dietHouseholdSizeTextField.getText().isEmpty() && !(NutriByte.view.dietServingSizeTextField.getText().isEmpty())) {
				//Just serving size info entered
				customProduct = new Product(selectedProduct.getndbNumber(), selectedProduct.getProductName(), selectedProduct.getManufacturer(), selectedProduct.getIngredients());
				customProduct.setServingUom(selectedProduct.getServingUom());
				customProduct.setHouseholdUom(selectedProduct.getHouseholdUom());
				customProduct.productNutrients = selectedProduct.productNutrients;
				customProduct.setServingSize(Float.parseFloat(NutriByte.view.dietServingSizeTextField.getText()));
				float ratio = Model.productsMap.get(selectedProduct.getndbNumber()).getServingSize() / Model.productsMap.get(selectedProduct.getndbNumber()).getHouseholdSize();
				customProduct.setHouseholdSize(customProduct.getServingSize() / ratio);
				NutriByte.person.dietProductsList.add(customProduct);
			}else {
				//Both entered
				customProduct = new Product(selectedProduct.getndbNumber(), selectedProduct.getProductName(), selectedProduct.getManufacturer(), selectedProduct.getIngredients());
				customProduct.setServingUom(selectedProduct.getServingUom());
				customProduct.productNutrients = selectedProduct.productNutrients;
				customProduct.setHouseholdUom(selectedProduct.getHouseholdUom());customProduct.setServingSize(Float.parseFloat(NutriByte.view.dietServingSizeTextField.getText()));
				float ratio = Model.productsMap.get(selectedProduct.getndbNumber()).getServingSize() / Model.productsMap.get(selectedProduct.getndbNumber()).getHouseholdSize();
				customProduct.setHouseholdSize(customProduct.getServingSize() / ratio);
				NutriByte.person.dietProductsList.add(customProduct);
			}
			
			int dupCount = 0;
			for(int i = 0; i < NutriByte.person.dietProductsList.size(); i++) {
				if(NutriByte.person.dietProductsList.get(i).getProductName().equals(customProduct.getProductName()) && 
						NutriByte.person.dietProductsList.get(i).getServingSize() == customProduct.getServingSize() &&
						NutriByte.person.dietProductsList.get(i).getHouseholdSize() == customProduct.getHouseholdSize()) {
					dupCount++;	
				}
			}
			if(dupCount == 2) {
				NutriByte.person.dietProductsList.remove(customProduct);
			}
			NutriByte.view.dietProductsTableView.setItems(NutriByte.person.dietProductsList);
			NutriByte.person.populateDietNutrientMap();
			NutriByte.view.nutriChart.updateChart();
		}
	}
	
	//Removes diet products from the diet table
	class RemoveDietButtonHandler implements EventHandler<ActionEvent> {

		@Override
		public void handle(ActionEvent event) {
			try {
				NutriByte.person.dietProductsList.remove(NutriByte.view.dietProductsTableView.getSelectionModel().getSelectedIndex());
				NutriByte.view.dietProductsTableView.setItems(NutriByte.person.dietProductsList);
				NutriByte.person.populateDietNutrientMap();
				NutriByte.view.nutriChart.updateChart();
			}catch(ArrayIndexOutOfBoundsException e) {}
			catch(NullPointerException e) {}
		}
		
	}
	
	//Handles all searching of products, nutrients and ingredients in the lower left hand quadrant
	class SearchButtonHandler implements EventHandler<ActionEvent> {

		@Override
		public void handle(ActionEvent event) {
			//Clear all values from the Products fields
			String productSearchValue = NutriByte.view.productSearchTextField.getText().trim();
			String nutrientSearchValue = NutriByte.view.nutrientSearchTextField.getText().trim();
			String ingredientSearchValue = NutriByte.view.ingredientSearchTextField.getText().trim();
			Iterator<Entry<String, Product>> it = Model.productsMap.entrySet().iterator();
			NutriByte.model.searchResultsList.clear();
			int count = 0;
				
			while(it.hasNext()) {
				Map.Entry<String, Product> product = (Map.Entry<String, Product>)it.next();
				//handle case where no fields are populated and search button is clicked
				if(productSearchValue.isEmpty() && nutrientSearchValue.isEmpty() && ingredientSearchValue.isEmpty()) {
					ObservableList <String> emptyProductNutrients = FXCollections.observableArrayList();
					NutriByte.model.searchResultsList.add(product.getValue());
					emptyProductNutrients.add(product.getValue().getProductName().toUpperCase().trim() + " by " + product.getValue().getManufacturer());
					NutriByte.view.productsComboBox.setItems(emptyProductNutrients);
					count++;
				}
				if(!(productSearchValue.length() < 1)) {
					if(!(nutrientSearchValue.length() < 1)) {
						if(!(ingredientSearchValue.length() < 1)) {
							//check everything
							if(product.getValue().getProductName().toString().toUpperCase().contains(productSearchValue.toUpperCase())) {
								for(ProductNutrient pnut : product.getValue().getProductNutrients().values()) {
									if(nutrientSearchValue.toUpperCase().equals(
											Model.nutrientsMap.get(pnut.nutrientCode.getValue().toString().trim()).getNutrientName().toUpperCase())) {
										if(product.getValue().getIngredients().toUpperCase().contains(ingredientSearchValue.toUpperCase())) {
											NutriByte.model.searchResultsList.add(product.getValue());
											count++;
										}else {
											break;
										}
									}
								}
							}
						}else {
							//check product and nutrient
							if(product.getValue().getProductName().toString().toUpperCase().contains(productSearchValue.toUpperCase())) {
								for(ProductNutrient pnut : product.getValue().getProductNutrients().values()) {
									if(nutrientSearchValue.toUpperCase().equals(
											Model.nutrientsMap.get(pnut.nutrientCode.getValue().toString().trim()).getNutrientName().toUpperCase())) {
										NutriByte.model.searchResultsList.add(product.getValue());
										count++;
									}
								}
							}
						}
					}else if(!(ingredientSearchValue.length() < 1)) {
						//check product and ingredient
						if(product.getValue().getProductName().toString().toUpperCase().contains(productSearchValue.toUpperCase())) {
							if(product.getValue().getIngredients().toUpperCase().contains(ingredientSearchValue.toUpperCase())) {
								NutriByte.model.searchResultsList.add(product.getValue());
								count++;
							}
						}
					}else {
						//check just product
						if(product.getValue().getProductName().toString().toUpperCase().contains(productSearchValue.toUpperCase())) {
							NutriByte.model.searchResultsList.add(product.getValue());
							count++;
						}
					}
				}else if(!(nutrientSearchValue.length() < 1)) {
					if(!(ingredientSearchValue.length() < 1)) {
						//check nutrient and ingredient
						for(ProductNutrient pnut : product.getValue().getProductNutrients().values()) {
							if(nutrientSearchValue.toUpperCase().equals(
									Model.nutrientsMap.get(pnut.nutrientCode.getValue().toString().trim()).getNutrientName().toUpperCase())) {
								if(product.getValue().getIngredients().toUpperCase().contains(ingredientSearchValue.toUpperCase())) {
									NutriByte.model.searchResultsList.add(product.getValue());
									count++;
								}else {
									break;
								}
							}
						}
					}else {
						//check just nutrient
						for(ProductNutrient pnut : product.getValue().getProductNutrients().values()) {
							if(nutrientSearchValue.toUpperCase().equals(
									Model.nutrientsMap.get(pnut.nutrientCode.getValue().toString().trim()).getNutrientName().toUpperCase())) {
								NutriByte.model.searchResultsList.add(product.getValue());
								count++;
							}
						}
					}
				}else if(!(ingredientSearchValue.length() < 1)) {
					//just ingredients
					if(product.getValue().getIngredients().toUpperCase().contains(ingredientSearchValue.toUpperCase())) {
						NutriByte.model.searchResultsList.add(product.getValue());
						count++;
					}
				}
			} 
			NutriByte.view.searchResultSizeLabel.setText(count + " product(s) found");
			NutriByte.view.productsComboBox.setItems(null);
			if(!NutriByte.model.searchResultsList.isEmpty()) {
				NutriByte.view.productsComboBox.setValue(NutriByte.model.searchResultsList.get(0).toString() + " by " + NutriByte.model.searchResultsList.get(0).getManufacturer());
				NutriByte.view.servingSizeLabel.setText(Float.toString(NutriByte.model.searchResultsList.get(0).getServingSize()) + " " + NutriByte.model.searchResultsList.get(0).getServingUom());
				NutriByte.view.dietServingUomLabel.setText(NutriByte.model.searchResultsList.get(0).getServingUom());
				NutriByte.view.householdSizeLabel.setText(Float.toString(NutriByte.model.searchResultsList.get(0).getHouseholdSize()) + " " + NutriByte.model.searchResultsList.get(0).getHouseholdUom());
				NutriByte.view.dietHouseholdUomLabel.setText(NutriByte.model.searchResultsList.get(0).getHouseholdUom());
				NutriByte.view.productIngredientsTextArea.setText("Product Ingredients: " + NutriByte.model.searchResultsList.get(0).getIngredients().substring(0, (NutriByte.model.searchResultsList.get(0).getIngredients().length() - 1)));
				ObservableList<Product.ProductNutrient> firstProduct = FXCollections.observableArrayList(NutriByte.model.searchResultsList.get(0).getProductNutrients().values());
				NutriByte.view.productNutrientsTableView.setItems(firstProduct);
				ObservableList<String> names = FXCollections.observableArrayList();
				if(NutriByte.model.searchResultsList.isEmpty()) {
					NutriByte.model.searchResultsList.clear();
				}
				for(int i = 0; i < NutriByte.model.searchResultsList.size(); i++) {
					names.add(NutriByte.model.searchResultsList.get(i).toString() + " by " + NutriByte.model.searchResultsList.get(i).getManufacturer());
				}
				NutriByte.view.productsComboBox.setItems(names);
			}
		}
	}
	
		//I have the binding set up to dynamically react when I do things in the text fields, just no idea how to get the table updated.
		ObjectBinding<String> comboBoxBinding = new ObjectBinding<String>() {
			{
				super.bind(NutriByte.view.productsComboBox.valueProperty());
			}

			@Override
			protected String computeValue() {
				int index = NutriByte.view.productsComboBox.getSelectionModel().getSelectedIndex();
				if(index < 0) {
					return null;
				}
				NutriByte.view.productIngredientsTextArea.setText("Product Ingredients: " + NutriByte.model.searchResultsList.get(index).getIngredients().substring(0, (NutriByte.model.searchResultsList.get(index).getIngredients().length() - 1)));
				ObservableList<Product.ProductNutrient> selectedProduct = FXCollections.observableArrayList(NutriByte.model.searchResultsList.get(index).getProductNutrients().values());
				NutriByte.view.productNutrientsTableView.setItems(selectedProduct);
				NutriByte.view.servingSizeLabel.setText(Float.toString(NutriByte.model.searchResultsList.get(index).getServingSize()) + " " + NutriByte.model.searchResultsList.get(index).getServingUom());
				NutriByte.view.dietServingUomLabel.setText(NutriByte.model.searchResultsList.get(index).getServingUom());
				NutriByte.view.householdSizeLabel.setText(Float.toString(NutriByte.model.searchResultsList.get(index).getHouseholdSize()) + " " + NutriByte.model.searchResultsList.get(index).getHouseholdUom());
				NutriByte.view.dietHouseholdUomLabel.setText(NutriByte.model.searchResultsList.get(index).getHouseholdUom());
				return NutriByte.view.productsComboBox.selectionModelProperty().getName();
			}
		};
}
