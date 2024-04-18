import subprocess

"""
Name : Mohammad Faquse
ID : 201014 
GitHub : https://github.com/Mohammad0Faqusa/SIC_Program.git 

"""

"""
start run the program here 
the program will run pass1 then pass2 

"""

def run_python_files(files):
    for file in files:
        subprocess.run(['python', file])

# Example usage:
files_to_run = ['pass1.py', 'pass2.py']
run_python_files(files_to_run)
