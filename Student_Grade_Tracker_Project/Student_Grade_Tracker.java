package Student_Grade_Tracker_Project;
import java.util.Scanner;

public class Student_Grade_Tracker{
    public int selected_option(){
        Scanner sc = new Scanner(System.in);
        int user_choice = sc.nextInt();
        System.out.println("Your seleted option is: " + user_choice);
        sc.close();
        return user_choice;
    }

    public void user_menu(){
        System.out.println("Please select one of the following options below:");
        System.out.println("Option 1: Create new student report");
        System.out.println("Option 2: Load existing student report");
        selected_option();
    }

    public static void main(String[] args) {
        System.out.println("Welcome to you student grade tracker!");
        Student_Grade_Tracker record = new Student_Grade_Tracker();
        record.user_menu();
    }
}