import logging
from datetime import datetime, timezone, timedelta
from pathlib import Path

# Log Directory
LOG_DIR = Path(__file__).resolve().parent.parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

# IST
IST_OFFSET = timedelta(hours=5, minutes=30)

def configure_logging():
    """Configure logging only once"""
    # Check if root logger already has handlers to avoid reconfiguration
    root_logger = logging.getLogger()
    if root_logger.handlers:
        return  # Already configured
    
    # Set custom time converter for IST
    logging.Formatter.converter = lambda *args: (datetime.now(timezone(IST_OFFSET))).timetuple()
    
    formatter_string = "%(asctime)s [%(levelname)s]: %(message)s"
    formatter = logging.Formatter(formatter_string)
    
    # Debug file handler
    dfh = logging.FileHandler(LOG_DIR / "debug.log")
    dfh.setLevel(logging.DEBUG)
    dfh.setFormatter(formatter)
    
    # Info file handler
    ifh = logging.FileHandler(LOG_DIR / "info.log")
    ifh.setLevel(logging.INFO)
    ifh.setFormatter(formatter)
    
    # Console handler
    ich = logging.StreamHandler()
    ich.setLevel(logging.INFO)
    ich.setFormatter(formatter)
    
    # Configure root logger
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(dfh)
    root_logger.addHandler(ifh)
    root_logger.addHandler(ich)

# Configure logging when module is first imported
configure_logging()

# Optional: export a logger instance for convenience
logger = logging.getLogger(__name__)
