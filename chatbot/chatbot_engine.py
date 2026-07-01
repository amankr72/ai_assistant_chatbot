from .intents import patterns
from .responses import responses
from .entity_extractor import extract_entities
import random
from .memory import update_params, missing_params, clear_params
from .state import get_state, set_state, clear_state
from .database import find_hotels
from .ml.predict import predict_intent



def regex_match_intent(message):

    message = message.lower().strip()  

    for intent, pattern in patterns.items():

        if pattern.search(message):           
            return intent

   
    return "default"

def format_hotels(params):
    
    
    hotels = find_hotels(params)
   
    if not hotels:
        return "Sorry, I couldn't find any hotels matching your preferences."

    response = "I found these hotels:\n"

    for name, area, price, stars in hotels:
        response += (
            f"⦿ {name}\n"
            f"Area: {area.title()}\n"
            f"Price: {price}\n"
            f"Stars: {stars}\n"
        )
    clear_params()
    clear_state()
    
    return response

def get_response(message):

    # Detect intent
    if len(message.split()) <= 2:
        intent = regex_match_intent(message)
    else:
        intent = predict_intent(message)

    # Extract entities
    entities = extract_entities(message)

   
    # Update memory
    params = update_params(entities)


    # Current conversation state
    state = get_state()

    # -----------------------------
    # Hotel Search
    # -----------------------------
    if intent == "hotel_search":

        missing = missing_params()

        if "area" in missing:
            set_state("waiting_area")
            return "Which area are you looking for?"

        if "price" in missing:
            set_state("waiting_price")
            return "What price range do you prefer?"

        clear_state()

        response = format_hotels(params)
        clear_params()

        return response

    # -----------------------------
    # Search by Stars
    # -----------------------------
    if intent == "search_by_stars":

        if params["stars"] is None:
            return "Are you looking for a 3-star, 4-star, or 5-star hotel?"

        clear_state()

        response = format_hotels(params)
        clear_params()

        return response

    # -----------------------------
    # Search by Name
    # -----------------------------
    if intent == "search_by_name":

        response = format_hotels(params)
        clear_params()

        return response

    # -----------------------------
    # Waiting for Area
    # -----------------------------
    if state == "waiting_area":

        if "area" in entities:

            missing = missing_params()

            if "price" in missing:
                set_state("waiting_price")
                return "What price range do you prefer?"

            clear_state()

            response = format_hotels(params)
            clear_params()

            return response

    # -----------------------------
    # Waiting for Price
    # -----------------------------
    if state == "waiting_price":

        if "price" in entities:

            clear_state()

            response = format_hotels(params)
            clear_params()

            return response

    # -----------------------------
    # Default Responses
    # -----------------------------
    if intent not in responses:
        intent = "default"

    return random.choice(responses[intent])
