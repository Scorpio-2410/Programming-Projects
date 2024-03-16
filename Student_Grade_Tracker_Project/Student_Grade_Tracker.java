package Student_Grade_Tracker_Project;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Student_Grade_Tracker{
    public void sem_subjects(){
        Scanner sc = new Scanner(System.in);
        Map<String, Integer> subjectDetails = new HashMap<>();
        System.out.println("How many courses are you doing this semester?");
        int numSubject = sc.nextInt();
        System.out.println("Enter your course name & credit points it is. If it's a pass/fail course enter 0 credit points.");
        for(int i = 0; i < numSubject; i++){
            System.out.println("Enter the name of course " + (i+1) + ":");
            String subjectName = sc.nextLine();
            System.out.println("Enter the credit points for " + subjectName + ":");
            int subjectCredit = sc.nextInt();
            subjectDetails.put(subjectName, subjectCredit);
        }
        sc.close();
    }
    
    public void selected_option(){
        Scanner sc = new Scanner(System.in);
        int userChoice = sc.nextInt();
        System.out.println("Your seleted option is: " + userChoice);
        if(userChoice == 1){
            sem_subjects();
        }
        sc.close();
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