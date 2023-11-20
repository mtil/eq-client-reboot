import functions
import time

functions.kill_clients_all()

functions.client_launch()

#pulse

pulse = True
logs_blue = r'D:\P99\Logs\eqlog_Zerotone_project1999.txt'
logs_green = r'D:\P99\eqlog_Airdiael_P1999Green.txt'
while pulse:
    print("Pulse Started.")
    time.sleep(10)
    if functions.client_alive_check('Blue') == False:
        print("Blue client not found.")
        # functions.kill_clients()
        functions.client_launch_single('Blue')
        time.sleep(10)

    if functions.client_alive_check('Green') == False:
        print("Green client not found.")
        # functions.kill_clients()
        functions.client_launch_single('Green')
        time.sleep(10)

    functions.error_window()
    functions.watch_log_file(logs_blue)
    functions.watch_log_file(logs_green)

time.sleep(3)


