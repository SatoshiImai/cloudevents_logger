# coding:utf-8
# ---------------------------------------------------------------------------
# __author__ = 'Satoshi Imai'
# __credits__ = ['Satoshi Imai']
# __version__ = '0.9.0'
# ---------------------------------------------------------------------------

import logging

from cloudevents import conversion
from cloudevents.http import CloudEvent


class CloudEventsJsonFormatter(logging.Formatter):
    def __init__(self,
                 app: str,
                 type: str,
                 source: str):

        self._attributes = {
            'app': app,
            'type': type,
            'source': source,
        }

        super().__init__()
        # end def

    def format(self, record: logging.LogRecord) -> str:
        this_attributes = self._attributes
        this_attributes['msg'] = record.getMessage()
        this_attributes['file'] = record.filename
        this_attributes['line'] = record.lineno
        this_attributes['func'] = record.funcName

        if 'data' in record.__dict__:
            data = record.__dict__['data']
            event = CloudEvent(this_attributes, data)
        else:
            event = CloudEvent(this_attributes)
            # end if

        payload = conversion.to_json(event).decode()

        return payload
        # end def
    # end class


class CloudEventsLogger(logging.Logger):
    def __init__(self,
                 logger_name: str,
                 app: str,
                 type: str,
                 source: str,
                 level: int = logging.INFO):

        self._attributes = {
            'type': type,
            'source': source,
        }

        super().__init__(logger_name, level=level)

        my_handler = logging.StreamHandler()
        my_formatter = CloudEventsJsonFormatter(app, type, source)
        my_handler.setFormatter(my_formatter)
        self.addHandler(my_handler)
        # end def
    # end class
