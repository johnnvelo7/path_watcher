import os
import pyinotify
import datetime
import argparse

#DESIGN
def print_design():
    RESET = "\033[0m"
    GREEN = "\033[92m"
    BOLD = "\033[1m"
    width = 50
    print(GREEN + "+" + "-" * (width - 2) + "+" + RESET)
    print(GREEN + "|" + " " * (width - 2) + "|" + RESET)
    title = "PATH WATCHER"
    title_padding = (width - len(title) - 2) // 2
    print(GREEN + "|" + " " * title_padding + BOLD + title + RESET + GREEN + " " * title_padding + "|" + RESET)
    print(GREEN + "|" + " " * (width - 2) + "|" + RESET)
    print(GREEN + "|" + "-" * (width - 2) + "|" + RESET)
    print(GREEN + "|" + " " * (width - 2) + "|" + RESET)
    info = "Version: 1.6"
    info_padding = (width - len(info) - 2) // 2
    print(GREEN + "|" + " " * info_padding + info + " " * info_padding + "|" + RESET)
    print(GREEN + "|" + " " * (width - 2) + "|" + RESET)
    author = "Author: FOREVER NOOB"
    author_padding = (width - len(author) - 2) // 2
    print(GREEN + "|" + " " * author_padding + BOLD + author + RESET + GREEN + " " * author_padding + "|" + RESET)
    print(GREEN + "|" + " " * (width - 2) + "|" + RESET)
    support_text = "Currently Supporting Linux OS Only"
    support_padding = (width - len(support_text) - 2) // 2
    print(GREEN + "|" + " " * support_padding + support_text + " " * support_padding + "|" + RESET)
    print(GREEN + "|" + " " * (width - 2) + "|" + RESET)
    print(GREEN + "+" + "-" * (width - 2) + "+" + RESET)

#CLASS_for_event_handler
class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print(f'{datetime.datetime.now()} - CREATED: {event.pathname}')
    def process_IN_CLOSE_WRITE(self, event):
        print(f'{datetime.datetime.now()} - CLOSED: {event.pathname}')
        self.display_file_contents(event.pathname)
    def display_file_contents(self, file_path):
        try:
            with open(file_path, 'r') as file:
                contents = file.read()
                print(f'Contents of the file {file_path}:\n{contents}')
        except IOError as e:
            print(f'Failed to open {file_path}. Reason: {e.strerror}')
        except Exception as e:
            print(f'An error occurred: {e}')

#GET_path
def get_directory_to_monitor():
    while True:
        folder_to_monitor = input("Please enter the path or directory to monitor: ").strip()
        if os.path.exists(folder_to_monitor):
            return folder_to_monitor
        else:
            print(f"Error: The folder {folder_to_monitor} does not exist. Please try again.")

#MONITOR_modus
def start_monitoring(folder_to_monitor):
    event_handler = EventHandler()
    watch_manager = pyinotify.WatchManager()
    watch_manager.add_watch(folder_to_monitor, pyinotify.IN_CREATE | pyinotify.IN_CLOSE_WRITE, rec=True, auto_add=True)
    notifier = pyinotify.Notifier(watch_manager, event_handler)
    print(f'Starting monitor on {folder_to_monitor}')
    try:
        notifier.loop()
    except KeyboardInterrupt:
        print("\nStopping monitor.")
    finally:
        notifier.stop()

#FILE_description
def parse_arguments():
    parser = argparse.ArgumentParser(description="Monitor a directory for file creation and closing after writing events. It displays the contents of the file after it's written.")
    return parser.parse_args()

#MAIN_function
def main():
    print_design()
    args = parse_arguments()
    folder_to_monitor = get_directory_to_monitor()
    start_monitoring(folder_to_monitor)

if __name__ == "__main__":
    main()
