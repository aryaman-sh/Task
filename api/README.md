# API 

## Notes
- Used Poetry for dependency management.
- The API uses FastAPI for handling requests.
- The sample data list, `items` in `autosuggest.py`, was generated using AI toold.
- Similarity matching is based on cosine similarity. While the current implementation is not fully optimised, it performs well for small datasets.
  - The similarity threshold is arbitrarily set at 0.6.

## Endpoints

### GET `/autosuggest`
Returns the category of the queried item or suggests the closest match if no exact match is found. 
#### Parameters:  
- query (str): The item to be queried.

#### Responses:
- 200 OK:

If an exact match is found:
```
{
  "message": "Category for banana is fruit"
}
```
If a similar match is found:
```
{
  "message": "Category for banan is fruit"
}
```
Match not found:
```
If no match is found:
{
  "message": "No category found for banana"
}
```
#### Example:
```
curl -X GET "http://localhost:8000/autosuggest?query=banana"
```
Response
```
{
    "message": "Category for banana is fruit"
}
```

## Setup
Getting poetry
```
pip install poetry
```
Running the development server
```
poetry install
poetry run fastapi run src/main.py --host 0.0.0.0 --port 8000
```

## Files
- src/main.py: File containing the FastAPI application.
- src/autosuggest.py: File containing the autosuggest logic.

