# fake-name-generator
A python parser to retrieve fake names from https://www.fakenamegenerator.com/

## Usage

```python
from generator import generate_random_names

generate_random_names(k = 50)
```

to generate 50 random gender french names (as it is by default on FR)

Try also : 

```python
from generator import generate_random_names, Country, Gender

generate_random_names(Gender.FEMALE,Country.US,k = 10)
```

to generate 10 US female names.