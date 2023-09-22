# cloudevents_logger

This is a simple expansion for Python logger to dump json logs as [CloudEvents](https://github.com/cloudevents/spec) format.
It uses [Python SDK for CloudEvents](https://pypi.org/project/cloudevents/).

## Initializing CloudEventsLogger

```python
from cloudevents_logger import CloudEventsLogger

# init logger instead of logging.getLogger
my_logger = CloudEventsLogger(__name__, 
                              app='my_app',
                              type='com.myapp.sometype',
                              source='https://my_app.com/somepage',
                              level=logging.DEBUG)

# log we go
my_logger.debug('debug message')
my_logger.info('info message')
my_logger.warning('warn message')
my_logger.error('error message')
my_logger.critical('critical message')
```

## init parameters

| param  | description |
| :----: | :---------: |
| app    | An attribute shows event source app. 'app' can be initialized only on init. |
| type   | A default attribute value shows event type. 'type' can be overridden later |
| source | A default attribute value shows event source. 'source' can be overridden later |

## `type` and `source` overriding

`type` and `source` attributes can be overridden at log timing via `extra` parameter.

```python
from cloudevents_logger import CloudEventsLogger

# init logger instead of logging.getLogger
my_logger = CloudEventsLogger(__name__, 
                              app='my_app',
                              type='com.myapp.sometype',
                              source='https://my_app.com/somepage',
                              level=logging.DEBUG)

# log with default value
my_logger.info('info message')

# override
my_logger.info('info message', extra={'type': 'type_override'})
my_logger.info('info message', extra={'source': 'source_override'})
my_logger.info('info message', extra={'type': 'type_override', 'source': 'source_override'})
```

## Adding `data` attribute

Can add `data` attribute by adding `data` key to `extra` parameter.
`data` attribute will be json format and event record will have `"datacontenttype": "application/json"`.

```python
from cloudevents_logger import CloudEventsLogger

# init logger instead of logging.getLogger
my_logger = CloudEventsLogger(__name__, 
                              app='my_app',
                              type='com.myapp.sometype',
                              source='https://my_app.com/somepage',
                              level=logging.DEBUG)

# add data
my_logger.info('info message', extra={'data': {'data_1': 'any data'}})
```

## LICENSE

I inherited Apache License 2.0 from [Python SDK for CloudEvents](https://pypi.org/project/cloudevents/).
