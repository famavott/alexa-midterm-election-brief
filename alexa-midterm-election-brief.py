# coding=utf-8

import logging
from datetime import datetime
from flask import Flask, json, render_template
from flask_ask import Ask, request, session, question, statement

__author__ = "Matt Favoino"
__email__ = "mattfavoino@gmail.com"


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


ENDPONT = "https://www.realclearpolitics.com/epolls/json/35_map.js"

ALL_RACES = [
    "arizona",
    "florida",
    "texas",
    "montana",
    "north dakota",
    "nevada",
    "missouri",
    "west virginia",
    "wisconsin",
    "minnesota",
    "new jersey",
    "tennesse",
]


@ask.on_session_started
def start_session():
    """
    Fired at the start of the session.
    """
    logging.debug("Session started at {}".format(datetime.now().isoformat()))


# Launch intent
#
# This intent is fired automatically at the point of launch.
# Use it as a way to introduce your Skill and say hello to the user. If you envisage your Skill to work using the
# one-shot paradigm (i.e. the invocation statement contains all the parameters that are required for returning the
# result


@ask.launch
def handle_launch():
    """
    (QUESTION) Responds to the launch of the Skill with welcome statement.
    """
    welcome_text = render_template("welcome")
    welcome_re_text = render_template("welcome_re")
    welcome_card_text = render_template("welcome_card")

    return (
        question(welcome_text)
        .reprompt(welcome_re_text)
        .standard_card(title="Quick Midterm Brief", text=welcome_card_text)
    )


@ask.intent("AllSenateRacesIntent")
def list_senate_races():
    """
    List all Senate races availabile.
    """
    senate_races = ALL_RACES
    list_senate_races_text = render_template(
        "list_senate_races", senate_races=senate_races
    )
    list_senate_races_reprompt_text = render_template("list_senate_races_reprompt")
    return statement(list_senate_races_text).reprompt(list_senate_races_reprompt_text)


@ask.intent("AMAZON.StopIntent")
def handle_stop():
    """
    (STATEMENT) Handles the 'stop' built-in intention.
    """
    farewell_text = render_template("stop_bye")
    return statement(farewell_text)


@ask.intent("AMAZON.CancelIntent")
def handle_cancel():
    """
    (STATEMENT) Handles the 'cancel' built-in intention.
    """
    farewell_text = render_template("cancel_bye")
    return statement(farewell_text)


@ask.intent("AMAZON.HelpIntent")
def handle_help():
    """
    (QUESTION) Handles the 'help' built-in intention.
    """

    help_text = render_template("help_text")
    return question(help_text)


@ask.intent("AMAZON.NoIntent")
def handle_no():
    """
    (?) Handles the 'no' built-in intention.
    """
    pass


@ask.intent("AMAZON.YesIntent")
def handle_yes():
    """
    (?) Handles the 'yes'  built-in intention.
    """
    pass


@ask.intent("AMAZON.PreviousIntent")
def handle_back():
    """
    (?) Handles the 'go back!' built-in intention.
    """
    pass


@ask.intent("AMAZON.StartOverIntent")
def start_over():
    """
    (QUESTION) Handles the 'start over!' built-in intention.
    """
    pass


@ask.session_ended
def session_ended():
    return statement("")


if __name__ == "__main__":
    app.run(debug=True)
