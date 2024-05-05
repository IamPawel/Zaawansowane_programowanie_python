# plik odpowiedzialny za wykonywanie zapisanej pracy
import time


def read_tasks(filename):
    tasks = []
    with open(filename, "r") as file:
        for line in file:
            if "status: pending" in line:
                tasks.append(line.strip())
    return tasks


def update_task_status(filename, task_line, new_status):
    with open(filename, "r") as file:
        lines = file.readlines()
    with open(filename, "w") as file:
        for line in lines:
            if line.strip() == task_line:
                file.write(line.replace("pending", new_status))
            else:
                file.write(line.replace("in_progress", new_status))


def execute_task(task_line, tasks_file):
    # Zmiana statusu zadania na "in_progress"
    update_task_status(tasks_file, task_line, "in_progress")
    # Pobranie numeru zadania
    task_id = task_line.split(";")[0].split(": ")[1]
    # Symulacja wykonania zadania przez 30 sekund
    print(f"Executing task {task_id}: {task_line}")
    for remaining in range(30, 0, -1):
        time.sleep(1)
        print(f"Time remaining for task {task_id}: {remaining} seconds", end="\r")
    update_task_status(tasks_file, task_line, "done")
    print(f"Task {task_id} done.")


def process_tasks(tasks_file):
    tasks = read_tasks(tasks_file)
    for task in tasks:
        execute_task(task, tasks_file)


if __name__ == "__main__":
    while True:
        process_tasks("zadania.txt")
        time.sleep(5)  # Sprawdzanie zadań co 5 sekund
