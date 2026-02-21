from typing import Dict, List, Optional
import logging
from .hypergraph_manager import HyperGraphManager
from .reinforcement_handler import ReinforcementHandler

class NeuralHyperGraphMiddleware:
    def __init__(self):
        self.hypergraph_manager = HyperGraphManager()
        self.reinforcement_handler = ReinforcementHandler()
        self.logger = logging.getLogger(__name__)
        
    def integrate_module(self, module: object) -> bool:
        """
        Integrates a new module into the hypergraph.
        
        Args:
            module: The module to be integrated.
            
        Returns:
            bool: True if integration is successful, False otherwise.
        """
        try:
            self.hypergraph_manager.add_node(module)
            self.reinforcement_handler.initialize_policy(module)
            return True
        except Exception as e:
            self.logger.error(f"Integration failed: {str(e)}")
            raise IntegrationError("Failed to integrate module") from e

    def process_data(self, data: Dict) -> Optional[List]:
        """
        Processes data through the hypergraph.
        
        Args:
            data: Input data as a dictionary.
            
        Returns:
            Optional[List]: Output data or None if processing fails.
        """
        try:
            self.hypergraph_manager.process_input(data)
            output = self.reinforcement_handler.apply_policy(data)
            return output
        except DataProcessingError as e:
            self.logger.error(f"Data processing failed: {str(e)}")
            return None

    def update_policy(self, feedback: Dict) -> bool:
        """
        Updates the reinforcement policy based on feedback.
        
        Args:
            feedback: Feedback data as a dictionary.
            
        Returns:
            bool: True if policy update is successful, False otherwise.
        """
        try:
            self.reinforcement_handler.update_policy(feedback)
            return True
        except PolicyUpdateError as e:
            self.logger.error(f"Policy update failed: {str(e)}")
            raise ReinforcementError("Failed to update reinforcement policy") from e

    def get_metrics(self) -> Dict:
        """
        Retrieves system metrics.
        
        Returns:
            Dict: System performance metrics.
        """
        return {
            'integration_success_rate': self.hypergraph_manager.integration_success_rate,
            'reinforcement_policy_strength': self.reinforcement_handler.policy_strength
        }