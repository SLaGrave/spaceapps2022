# Dijon

`Dijon` was created by team [Jupiter Isn't Real](https://2022.spaceappschallenge.org/challenges/2022-challenges/jovian-system/teams/jupiter-isnt-real/project) for the [2022 NASA Space Apps Challenge](https://www.spaceappschallenge.org/)

---

Dijon is an all-in-one solution to explore and create with data from NASA's JunoCam. Currently, compiling and editing JunoCam images requires access to and knowledge of tools such as Photoshop or python (sometimes both). Dijon provides one specific tool to download the imagery, merge the channels into one image, and apply common filters. We hope this will prompt more people to interact with this imagery. We also allow the more advanced user to interact with the individual pixel data via a python interpreter included in the environment.

## Usage

1. The user selects an image dataset they would like to use from [NASA's JunoCam Website](https://www.missionjuno.swri.edu/junocam/processing)
2. They paste the *Share Link* into the `Dijon` startup page
3. Apply filters
   1. `Gaussian Blur` - A blur filter
   2. `Mean`, `Mode`, & `Min`/`Max` Filters - Filters which will perform those mathematical functions over a neighborhood of pixels in the image
   3. `Unsharp Mask` - An image sharpening technique
4. The user can also use the built in python interpreter to apply custom code
5. Click the `Run` button to generate an image
6. Click the `Save` button to save the image to the local folder set in `config.json`

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