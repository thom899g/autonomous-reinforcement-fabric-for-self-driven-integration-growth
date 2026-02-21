class MiddlewareConfig:
    def __init__(self):
        self.learning_rate = 0.1
        self.convergence_threshold = 0.95
        self.max_reinforcement_attempts = 20

    @classmethod
    def from_env(cls):
        """
        Initializes configuration from environment variables.
        
        Returns:
            MiddlewareConfig: An instance of MiddlewareConfig.
        """
        config = cls()
        try:
            config.learning_rate = float(os.getenv('REINFORCEMENT_LEARNING_RATE', '0.1'))
            config.convergence_threshold = float(os.getenv('CONVERGENCE_THRESHOLD', '0.95'))
            config.max_reinforcement_attempts = int(os.getenv('MAX_REINFORCEMENT_ATTEMPTS', '20'))
        except ValueError:
            raise ConfigurationError("Failed to parse configuration values from environment variables")