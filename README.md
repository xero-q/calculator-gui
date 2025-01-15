## Calculator (GUI using Tkinter)

### Steps to install

- Install Tkinter according to your OS.

Windows: 
```sh
python -m pip install tk
```  

MacOS
```sh
brew install python-tk
```

Linux
- Debian based:
```sh
sudo apt-get install python3-tk
```

- Red Hat based:
```sh
sudo dnf install python3-tkinter
```

- Arch Linux:
```sh
sudo pacman -S tk
```

### Install requirements

```sh
pip install -r requirements.txt
```

### Running the app:

```sh
python main.py
```


### Highlights

- Showcase use of Tkinter library for creating desktop applications.
- Uses Observer pattern for notifying GUI of changes in the Calculator.