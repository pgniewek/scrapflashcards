# scrapflashcards

### Installation:
This program is written in Python 3. Please, take care to execute a proper version of python during the installation and usage.

* Clone the repository:

```
git clone https://github.com/pgniewek/scrapflashcards.git
```

* Create a virtual environment:

```
cd scrapflashcards
python3 -m venv scrap-env
```
* Activate the environment:

```
source scrap-env/bin/activate
```
Your command line should now read something like: `(scrap-env) user@yourcomputer:~/$`

* Install required packages:

```
pip install -r requirements.txt
```

### Testing:
This package is being developed with unit testing in mind. All the tests will be available in `/tests` directory and will require `pytest` and `mock` as per `requirements.txt`. Testing can be done by executing
```
py.test --cov=scrapflashcards
```
and a full coverage report including missing lines can be obtained further by requesting
```
coverage report -m
```
