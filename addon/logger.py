import logging
from datetime import datetime

def setup_logger():
    """
    Set up and configure the logger for the addon.
    Returns a configured logger instance that can be used throughout the addon.
    """
    # Create logger
    logger = logging.getLogger('CustomBlenderAddon')
    
    # Only create handlers if they haven't been created already
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        # Create console handler with formatting
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Add formatter to console handler
        console_handler.setFormatter(formatter)
        
        # Add console handler to logger
        logger.addHandler(console_handler)
        
        logger.info("Logger initialized for Custom Blender Addon")
    
    return logger

def log_operator_execution(operator_name, context):
    """
    Helper function to log operator executions with relevant context
    """
    logger = logging.getLogger('CustomBlenderAddon')
    logger.info(f"Executing operator: {operator_name}")
    logger.info(f"Active object: {context.active_object.name if context.active_object else 'None'}")
    logger.info(f"Selected objects: {len(context.selected_objects)}")
    logger.info(f"Mode: {context.mode}")

def log_error(error_msg, exc_info=None):
    """
    Helper function to log errors
    """
    logger = logging.getLogger('CustomBlenderAddon')
    if exc_info:
        logger.error(f"Error occurred: {error_msg}", exc_info=exc_info)
    else:
        logger.error(f"Error occurred: {error_msg}")