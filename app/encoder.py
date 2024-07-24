# * Overriding de json.dumps(), el método que usa Flask de la librería de
# * json de Python para serializar información. Por defecto, json.dumps()
# * no reconoce objetos de tipo TIME y la serialización por defecto de DATE
# * no es visualmente apelable en el front. (RFC 822) -> (ISO 8601)

from flask.json.provider import DefaultJSONProvider
from datetime import time, date

class TimeEncoder(DefaultJSONProvider):
    def __init__(self, app):
        super().__init__(app)
    def default(self, obj):
        if isinstance(obj, time):
            return obj.strftime('%H:%M:%S')
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)