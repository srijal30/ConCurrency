# ConCurrency
Google mentorship project in which we build a blockchain.

## How to Use

* Clone the repo
```
git clone https://github.com/srijal30/ConCurrency.git
```

* Make sure that you have [Python 3](https://www.python.org/downloads/) installed. 

* Setup the enviorment (NOTE: replace `python` with the path to your python3 executable and replace `Scripts` with `bin` if you are using a unix OS)
```
python -m venv venv
. ./venv/Scripts/activate 
pip install -r requirements.txt
```
* **OPTIONAL:** To compile the ProtoBuf files locally, run the following commands
```
pip install -r dev-requirements.txt
python -m grpc_tools.protoc -I. --python_out=src/model/proto --pyi_out=src/model/proto --grpc_python_out=src/model/proto schema.proto
```
 


