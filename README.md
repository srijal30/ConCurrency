# ConCurrency
Google mentorship project in which we build a blockchain.

## How to Use

* Clone the repo
```
git clone https://github.com/srijal30/ConCurrency.git
```

* Make sure that you have [Python 3](https://www.python.org/downloads/) installed. 

* Setup the enviorment (NOTE: replace `python` with the path to your python executable)
```
python -m venv venv
pip install -r requirements.txt
```
* (Optional) To compile the ProtoBuf files locally, first make sure you have [protoc](https://github.com/protocolbuffers/protobuf/releases) installed. Then call this commadn:
```
protoc schema.proto -I=. --python_out=src
```
 


