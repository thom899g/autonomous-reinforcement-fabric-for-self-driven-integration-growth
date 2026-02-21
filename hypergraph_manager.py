from typing import Dict, List, Optional
import logging

class HyperGraphManager:
    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.logger = logging.getLogger(__name__)
        
    def add_node(self, node: object) -> None:
        """
        Adds a new node to the hypergraph.
        
        Args:
            node: The node to be added.
        """
        try:
            if not hasattr(node, 'process'):
                raise NodeIntegrationError("Node does not have process method")
            self.nodes.append(node)
            self.logger.info(f"Added node {id(node)} to hypergraph.")
        except NodeIntegrationError as e:
            self.logger.error(f"Failed to add node: {str(e)}")

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the hypergraph by its ID.
        
        Args:
            node_id: The ID of the node to be removed.
            
        Returns:
            bool: True if removal is successful, False otherwise.
        """
        try:
            index = next((i for i, node in enumerate(self.nodes) if id(node) == node_id), None)
            if index is not None:
                del self.nodes[index]
                return True
            return False
        except Exception as e:
            raise NodeRemovalError(f"Failed to remove node {node_id}: {str(e)}")