import time


def process_tasks(filename):
    with open(filename, "r") as f:
        for line in f:
            task = line.strip()
            if task.endswith(";pending"):
                taskinfo = task.split(";")
                id = taskinfo[0]
                print(f"Wykonywanie zadania o id: {id}")
                timestamp = taskinfo[1]
                change_status(filename, id, "in_progress")
                for remaining in range(30, 0, -1):
                    time.sleep(1)
                    print(
                        f"Time remaining for task {id}: {remaining} seconds", end="\r"
                    )
                change_status(filename, id, "done")
                break
            else:
                print("Brak zadan do wykonania")


def change_status(filename, id, status):
    with open(filename, "r") as f:
        lines = f.readlines()

    with open(filename, "w") as f:
        for line in lines:
            task = line.split(";")
            if id == task[0]:
                line = f"{task[0]};{task[1]};{status}\n"
            f.write(line)


while True:
    process_tasks("zadania.txt")
    time.sleep(5)  # Sprawdzanie zadań co 5 sekund
