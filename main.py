from Data.Scripts import UiPresets
import Runtime

def main():
    UiPresets.call("homescreen")
    while True:
        Runtime.start_frame()
        Runtime.end_frame()

if __name__ == "__main__":
    main()