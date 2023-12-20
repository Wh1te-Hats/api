# To run the project

### Create a virtual environment

```
python -m venv venv
```
### Go inside the virtual environment
```
./venv/script/activate (In Windows)
```
### Install all the requirements
```
pip install -r requirements-dev.txt
```
### Run the server from the root folder
```
uvicorn app.main:app --reload
```
### View swagger docs
```
http://localhost:8000/docs#/]
```
