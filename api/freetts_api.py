import requests
import json

class FreettsApi:
    _BASE_URL = "https://freetts.ru" 
    _PREFIX = "/api/v1"

    def __init__(self):
        pass

    def get_synthesized_text(self, text, voice_id):
        try:
            json_body = json.dumps({
                "text": text,
                "voiceid": voice_id
            })

            response = requests.post(self.get_base_url_api() + "/tts", json_body).json()

            if (response['status'] == 400 and response['message'] == "Ошибка синтеза"):
                self.get_synthesized_text(text, voice_id)
            
            return response
        except:
            return {
                "status": 500,
                "message": None
            }

    def get_base_url(self):
        return self._BASE_URL
    
    def get_base_url_api(self):
        return self._BASE_URL + self._PREFIX