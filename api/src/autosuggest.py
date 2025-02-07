from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import JSONResponse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re
import json

router = APIRouter()

# Mapping item: Category
items = {
    "banana": "fruit",
    "apple": "fruit",
    "carrot": "vegetable",
    "broccoli": "vegetable",
    "chicken": "meat",
    "beef": "meat",
    "orange": "fruit",
    "grape": "fruit",
    "strawberry": "fruit",
    "blueberry": "fruit",
    "watermelon": "fruit",
    "lettuce": "vegetable",
    "spinach": "vegetable",
    "potato": "vegetable",
    "tomato": "vegetable",
    "pork": "meat",
    "lamb": "meat",
    "turkey": "meat",
    "duck": "meat",
    "salmon": "fish",
    "tuna": "fish",
    "cod": "fish",
    "trout": "fish",
    "shrimp": "seafood",
    "lobster": "seafood",
    "crab": "seafood",
    "oyster": "seafood",
    "milk": "dairy",
    "cheese": "dairy",
    "yogurt": "dairy",
    "butter": "dairy",
    "bread": "grain",
    "rice": "grain",
    "pasta": "grain",
    "quinoa": "grain",
    "almond": "nut",
    "walnut": "nut",
    "peanut": "nut",
    "cashew": "nut"
}

def get_all_similarities(query, items):
    """
    Function to get all similarities using Cosine Similarity.
    :param query: Query text
    :param items: All items (Assuming preprocessed)
    :return: List of similarities
    """
    # Some cleaning
    query = query.lower().strip()
    query = re.sub(r'[^a-z]', '', query) # Getting rid of non alphabets
    # Cosine similarity calc
    vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(2, 3))
    vectors = vectorizer.fit_transform(list(items.keys()) + [query])
    cosine_similarities = cosine_similarity(vectors[-1], vectors[:-1]).flatten()
    similarities = sorted(
        [(item, score) for item, score in zip(list(items.keys()), cosine_similarities)],
        key=lambda x: x[1],
        reverse=True # Descending
    )
    return similarities


@router.get("/autosuggest")
async def autosuggest(query: str, request: Request) -> JSONResponse:
    """
    Autosuggest endpoint
    Arbitrary threshold set at 0.6
    :param query: str: query text
    :param request: HTTP request
    :return: JSONResponse: API response
    """
    # Case: Exact Match
    category = items.get(query.lower())
    if category:
        message = f"Category for {query} is {category}"
        return JSONResponse(
            status_code=200,
            content={
                "message": message
            }
        )

    # Case: Similarity matching
    similar = get_all_similarities(query, items) # Similar is a list of tuples (item, score)
    if similar[0][1] > 0.6: # Arbitrary threshold
        category= items.get(similar[0][0])
        message = f"Category for {similar[0][0]} is {category}"
        return JSONResponse(
            status_code=200,
            content={
                "message": message
            }
        )
    else:
        return JSONResponse(
            status_code=200,
            content={
                "message": f"No category found for {query}"
            }
        )



