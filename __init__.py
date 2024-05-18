"""The Daily Text Sensor integration."""
import logging

# Set up logging for your component
_LOGGER = logging.getLogger(__name__)

# Domain of the component, must match the "domain" field in manifest.json
DOMAIN = "jw.kexpiral.com"

JSON_URL = "https://raw.githubusercontent.com/benjifc/JW-Home-Assistant/main/json/2024_daily_text.json"
LOCAL_JSON_PATH = 'custom_components/jw/json/2024_daily_text.json'


async def download_json(url, session, local_path):
    """Download the JSON file."""
    try:
        async with async_timeout.timeout(10):
            async with session.get(url) as response:
                if response.status != 200:
                    _LOGGER.error("Failed to download JSON file: %s", response.status)
                    return False
                with open(local_path, 'wb') as f:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        f.write(chunk)
        _LOGGER.info("Downloaded JSON file successfully")
        return True
    except Exception as e:
        _LOGGER.error("Error downloading JSON file: %s", e)
        return False





async def async_setup(hass, config):
    """Set up the component using YAML."""
    # Initialization code if necessary
    _LOGGER.info("Setting up Daily Text Sensor component")
    
    # No additional configuration needed in this function
    return True

async def async_setup_entry(hass, config_entry):
    """Set up the component using the user interface."""
    # Initialization code if necessary
    _LOGGER.info("Setting up Daily Text Sensor component from config entry")
    
    # No additional configuration needed in this function
    return True
