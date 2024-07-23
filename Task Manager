#include <iostream>
#include <string>

using namespace std;

const int MAX_TASKS = 100;

class Task_Manager {
private:
    string tasks[MAX_TASKS];
    bool completed[MAX_TASKS];
    bool incompleted[MAX_TASKS];
    int task_count = 0;  // In-Class Initialization

public:
    void show_tasks() {
        if (task_count == 0) {
            cout << "No tasks available." << endl;
        } else {
            cout << "Tasks:" << endl;
            for (int i = 0; i < task_count; ++i) {
                cout << i + 1 << ". " << tasks[i];
                if (completed[i]) {
                    cout << " [Complete]";
                }
                if (incompleted[i]) {
                    cout << " [Incomplete]";
                }
                cout << endl;
            }
        }
    }

    void add_task() {
        if (task_count >= MAX_TASKS) {
            cout << "Task list is full. Cannot add more tasks." << endl;
            return;
        }
        cout << "Add task: ";
        cin.ignore();
        getline(cin, tasks[task_count]);
        completed[task_count] = false;
        incompleted[task_count] = false;  // Initialize as not incomplete
        task_count++;
    }

    void remove_task() {
        if (task_count == 0) {
            cout << "No tasks available to remove." << endl;
            return;
        }

        cout << "Enter the task number to remove:\n";
        for (int i = 0; i < task_count; ++i) {
            cout << i + 1 << ". " << tasks[i];
            if (completed[i]) {
                cout << " [Complete]";
            }
            if (incompleted[i]) {
                cout << " [Incomplete]";
            }
            cout << endl;
        }

        int index;
        cin >> index;
        if (index < 1 || index > task_count) {
            cout << "Invalid task number." << endl;
            return;
        }

        for (int i = index - 1; i < task_count - 1; ++i) {
            tasks[i] = tasks[i + 1];
            completed[i] = completed[i + 1];
            incompleted[i] = incompleted[i + 1];
        }

        task_count--;
        cout << "Task removed successfully." << endl;
    }

    void mark_complete() {
        if (task_count == 0) {
            cout << "No tasks available to mark as complete." << endl;
            return;
        }

        cout << "Enter the task number to mark as complete:\n";
        for (int i = 0; i < task_count; ++i) {
            cout << i + 1 << ". " << tasks[i];
            if (completed[i]) {
                cout << " [Complete]";
            }
            if (incompleted[i]) {
                cout << " [Incomplete]";
            }
            cout << endl;
        }

        int index;
        cin >> index;
        if (index < 1 || index > task_count) {
            cout << "Invalid task number." << endl;
            return;
        }

        completed[index - 1] = true;
        incompleted[index - 1] = false;  // Mark as not incomplete
        cout << "Task marked as complete." << endl;
    }

    void mark_incomplete() {
        if (task_count == 0) {
            cout << "No tasks available to mark as incomplete." << endl;
            return;
        }

        cout << "Enter the task number to mark as incomplete:\n";
        for (int i = 0; i < task_count; ++i) {
            cout << i + 1 << ". " << tasks[i];
            if (completed[i]) {
                cout << " [Complete]";
            }
            if (incompleted[i]) {
                cout << " [Incomplete]";
            }
            cout << endl;
        }

        int index;
        cin >> index;
        if (index < 1 || index > task_count) {
            cout << "Invalid task number." << endl;
            return;
        }

        incompleted[index - 1] = true;
        completed[index - 1] = false;  // Mark as not complete
        cout << "Task marked as incomplete." << endl;
    }

    void pin_task() {
        if (task_count == 0) {
            cout << "No tasks available to pin." << endl;
            return;
        }

        int index;
        cout << "Enter the task number to pin: \n";
        for (int i = 0; i < task_count; ++i) {
            cout << i + 1 << ". " << tasks[i] << endl;
        }
        cin >> index;
        if (index < 1 || index > task_count) {
            cout << "Invalid task number." << endl;
            return;
        }

        string task_to_pin = tasks[index - 1];
        bool complete_status = completed[index - 1];
        bool incomplete_status = incompleted[index - 1];

        for (int i = index - 1; i > 0; --i) {
            tasks[i] = tasks[i - 1];
            completed[i] = completed[i - 1];
            incompleted[i] = incompleted[i - 1];
        }

        tasks[0] = task_to_pin;
        completed[0] = complete_status;
        incompleted[0] = incomplete_status;

        cout << "Task pinned successfully." << endl;
    }
};

int main() {
    Task_Manager task_manager;
    int choice;

    do {
        cout << "Enter your choice:\n1. Show tasks\n2. Add task\n3. Remove task\n4. Mark done\n5. Mark incomplete\n6. Pin task\n7. Exit\n";
        cin >> choice;

        switch (choice) {
            case 1:
                task_manager.show_tasks();
                break;
            case 2:
                task_manager.add_task();
                break;
            case 3:
                task_manager.remove_task();
                break;
            case 4:
                task_manager.mark_complete();
                break;
            case 5:
                task_manager.mark_incomplete();
                break;
            case 6:
                task_manager.pin_task();
                break;
            case 7:
                cout << "Exiting..." << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    } while (choice != 7);

    return 0;
}
