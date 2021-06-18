import subprocess


def push():
    title = input('Choose a title for the commit ')
    subprocess.run(['git add .'], shell=True)
    subprocess.run(['git commit -m ' + title], shell=True)


if __name__ == '__main__':
    push()