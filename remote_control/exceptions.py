class CommandNotRegistered(ValueError):
    """
    An error that is raised when the requested command is not registered.
    """
    pass


class CommandNotFound(ValueError):
    """
    An error that is raised when the requested command is not found.
    """
    pass
