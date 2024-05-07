import time


def printProgressBar(
    iteration,
    total,
    prefix="",
    suffix="",
    decimals=1,
    length=100,
    fill="█",
    printEnd="\r",
):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + "-" * (length - filledLength)
    print(f"\r{prefix} |{bar}| {percent}% {suffix}", end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


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
                items = list(range(30, 0, -1))
                l = len(items)
                # Initial call to print 0% progress
                printProgressBar(0, 1, prefix="Progress:", suffix="Complete", length=50)
                for i, item in enumerate(items):
                    # Do stuff...
                    time.sleep(1)
                    # Update Progress Bar
                    printProgressBar(
                        i + 0.1, l, prefix="Progress:", suffix="Complete", length=50
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
