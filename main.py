"""Brug af biblioteker"""
import shutil
import os


class Backup():
    def print_content(self, content):
        content_list = os.listdir(content)
        user_feedback = 'Found files:\n'
        for element in content_list:
            user_feedback += element + '\n'
        print(user_feedback)

    def request_continue(self):
        user_input = input("Do You want to continue with the backup? Type Y to continue or N to cancel\n")
        if user_input.lower() == 'y':
            return
        elif user_input.lower() == 'n':
            exit(0)
        else:
            self.request_continue()

    def copy_folder(self, source, destination):
        """Egen metode. Kopiere fra source til destination"""
        shutil.copytree(source, destination, dirs_exist_ok=True)

"""Bruger input"""
user_input_source = input('Enter source folder:\n')
user_input_destination = input('Enter backup destination:\n')
"""kalder klassen"""
backup = Backup()
"""kald af egen metode"""
backup.print_content(user_input_source)
backup.request_continue()
backup.copy_folder(user_input_source, user_input_destination)
