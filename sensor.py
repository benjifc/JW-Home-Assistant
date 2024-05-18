import json
import datetime
import os
from homeassistant.helpers.entity import Entity

# Ruta al archivo JSON
json_file_path = 'json/2024_daily_text.json'

class DailyTextSensor(Entity):
    def __init__(self, json_file,language):
        self._json_file = json_file
        self._state = None
        self._language = language
        self._attributes = {}
        self.update()

    @property
    def name(self):
        return 'Daily Text'

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes

    def update(self):
        today = datetime.datetime.now().strftime('%Y%m%d')
        with open(self._json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for item in data:
            if item['date'] == today:
                self._state = item['title']
                self._attributes['content'] = item['content']
                break
        else:
            self._state = 'Not available'
            self._attributes['content'] = 'there is not day text content for today'

# Registro del sensor en Home Assistant
def setup_platform(hass, config, add_entities, discovery_info=None):
    language = hass.config.language    
    add_entities([DailyTextSensor(json_file_path)], True)
