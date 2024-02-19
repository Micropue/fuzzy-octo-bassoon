import time

def focus_timer(minutes):
    seconds = minutes * 60
    print(f"Focus timer set for {minutes} minutes.")
    time.sleep(seconds)
    print("Time's up! Your focus session has ended.")

if __name__ == "__main__":
    focus_time = int(input("Enter the duration of your focus session in minutes: "))
    focus_timer(focus_time)
