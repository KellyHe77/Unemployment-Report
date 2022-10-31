# Unemployment-Report


## Setup


Create and activate a virtual environment:

```sh
conda create -n unemployment-env python=3.8

conda activate unemployment-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```


## Usage

Run an example:
```sh
python app/my_script.py
```

Run the unemployment report:
```sh
python app/unemployment.py
```

# or pass env var from command line
```sh
ALPHAVANTAGE_API_KEY="abc123" python app/unemployment.py
```