#данные
logs = [
    "INFO: Service started",
    "ERROR: Connection timeout",
    "WARNING: CPU usage high",
    "ERROR: Disk full",
    "INFO: Health check passed",
    "ERROR: Out of memory"
]

# фильтруем ERROR
err = [log for log in logs if log.startswith("ERROR")]

#task_1
err_count = len(err)

#task_2
for er in err:
    print(er)

#task_3
if err_count > 2:
    print("Срочно чиним прод!")
else:
    print("Пока держимся")