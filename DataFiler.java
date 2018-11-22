//Phil Prosapio, Andrew ID: pprosapi
package hw3;

//Abstract class for my specifc file handling child classes. Kids are CSVFiler and XMLFiler
public abstract class DataFiler {
	
	public abstract void writeFile(String filename);
	
	public abstract boolean readFile(String filename);

}