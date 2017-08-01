from __future__ import absolute_import

import importlib
import json

import requests
from django.core import signing

from remote_control import settings
from remote_control.exceptions import CommandNotFound, CommandNotRegistered


def call(endpoint, command, *args, **kwargs):
    """
    Run a registered command on the endpoint.
    Returns the response from the command.
    """
    # Create the request data
    request = {
        'command': command,
        'args': args,
        'kwargs': kwargs
    }

    # Sign the request
    signed_request = signing.dumps(obj=request, key=settings.SECRET)

    # Send the request
    res = requests.post(endpoint, data=json.dumps({
        'request': signed_request
    }))

    # Return the parsed response
    return res.json()


def handle_request(signed_request):
    """
    Parse the signed request and executes the command.
    Returns the response from the command.
    """
    # Parse the request
    request = signing.loads(signed_request, key=settings.SECRET,
                            max_age=settings.REQUEST_MAX_AGE)

    # Get the command function
    command_func = get_command(request['command'])

    # Execute it
    return command_func(*request['args'], **request['kwargs'])


def get_command(command):
    """
    Retrieve the function for the command path.
    """
    # Get the command's path
    try:
        command_path = settings.COMMANDS[command]
    except KeyError:
        raise CommandNotRegistered(
            "The {} command is not registered.".format(command)
        )

    # Load the python module
    module_name, func_name = command_path.rsplit('.', 1)
    module = importlib.import_module(module_name)

    # Return the function
    try:
        return getattr(module, func_name)
    except AttributeError:
        raise CommandNotFound(
            "The {} function does not exist.".format(command_path)
        )
