# Dijon

`Dijon` was created by team [Jupiter Isn't Real](https://2022.spaceappschallenge.org/challenges/2022-challenges/jovian-system/teams/jupiter-isnt-real/project) <img src=".ogo.jpeg" width="200" height="200"> for the [2022 NASA Space Apps Challenge](https://www.spaceappschallenge.org/)

---

Dijon is an all-in-one solution to explore and create with data from NASA's JunoCam. Currently, compiling and editing JunoCam images requires access to and knowledge of tools such as Photoshop or python (sometimes both). Dijon provides one specific tool to download the imagery, merge the channels into one image, and apply common filters. We hope this will prompt more people to interact with this imagery. We also allow the more advanced user to interact with the individual pixel data via a python interpreter included in the environment.

## Build Steps

Use the following steps to build `Dijon` from source

**Linux:**

```sh
$ python -m venv ./env
$ source env/bin/activate
$ pip install -r requirements.txt
```

**Windows:**

```sh
$ python -m venv env
$ env\Scripts\activate.bat
$ pip install -r requirements.txt
```

**Run the Program:**

```sh
$ python dijon.py
```