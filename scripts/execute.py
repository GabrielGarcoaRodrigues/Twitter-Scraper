import subprocess

def install_packages(packages):
    for package in packages:
        subprocess.call(['pip', 'install', package])


if __name__ == "__main__":
    packages_to_install = ['selenium', 'termcolor', 'xlwt', 'chromedriver_autoinstaller', 'openpyxl', 'logger']
    install_packages(packages_to_install)
  