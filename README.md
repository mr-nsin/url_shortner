
# url_shortener
URL Shortener Service on Flask Framework.
## Pipenv Installation

### 
```bash
$ pip install pipenv
```
### Steps to run locally

#### Step 1: Clone the repo

```bash
$ git clone https://github.com/mr-nsin/url_shortner.git
```
#### Step 2: Install libraries using pipenv
```bash
$ pipenv install
```
#### Step 3: Run the app
```bash
$ python3 app.py
```
## Usage
Test the app using postman by invoking below endpoint.
```
http://localhost:105/?original_url=https://google.com
```
##### Response:
```json
{

	"date_created": "07-22-2021",

	"original_url": "https://google.com",

	"short_url": "http://localhost:105/Lnj",

	"visits": 1

}
```
##### Run the below endpoint in browser of above output
```
http://localhost:105/Lnj
```
