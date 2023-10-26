import threading
import time

# stop thread toggle
stopTask = False

# Task function
def task(id):
    global stopTask
    while not stopTask:
        print(f"Task {id} running")
        time.sleep(1)

def main():

    global stopTask
    
    print("Program start")

    # create task thread array
    threadArray = []
    for i in range(1, 11):
        threadArray.append(threading.Thread(target=task, args=(i, )))

    # foreach start thread
    for thread in threadArray:
        thread.start()

    # while true listen [ctrl + c] to stop all thread and program
    while True:
        try: 
            time.sleep(1)

        except KeyboardInterrupt:
            # switch stopTask value
            stopTask = True

            # thead join
            for thread in threadArray:
                thread.join()

            # program stopped
            print('Program stopped')
            quit()

        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()