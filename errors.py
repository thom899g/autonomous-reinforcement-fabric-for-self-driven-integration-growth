class IntegrationError(Exception):
    pass

class ReinforcementError(Exception):
    pass

class DataProcessingError(ReinforcementError):
    pass

class PolicyUpdateError(ReinforcementError):
    pass

class NodeIntegrationError(IntegrationError):
    pass

class NodeRemovalError(IntegrationError):
    pass

def handle_reinforcement_error(error: Exception) -> Dict:
    """
    Handles reinforcement-related errors and returns an error dictionary.
    
    Args:
        error: The exception that was raised.
        
    Returns:
        Dict: An error dictionary with details about the error.
    """
    return {
        'error_type': type(error).__name__,
        'message': str(error),
        'stack_trace': format_exc(),
    }