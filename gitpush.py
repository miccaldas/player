import subprocess


def push():
    title = input('Choose a title for the commit ')
    subprocess.run(['git add .'], shell=True)
    subprocess.run(['git commit -m ' + title], shell=True)
    subprocess.run(['git push origin main'], shell=True)
    subprocess.run(['git push origin_gogs main'], shell=True)


if __name__ == '__main__':
    push()