# coding:utf-8
# ---------------------------------------------------------------------------
# __author__ = 'Satoshi Imai'
# __credits__ = ['Satoshi Imai']
# __version__ = "0.9.0"
# ---------------------------------------------------------------------------

import logging
from logging import Logger, StreamHandler
from typing import Generator

import pytest

from src.cloudevents_logger import CloudEventsLogger


@pytest.fixture(scope='session', autouse=True)
def setup_and_teardown():
    # setup

    yield

    # teardown
    # end def


@pytest.fixture(scope='module')
def logger() -> Generator[Logger, None, None]:
    log = logging.getLogger(__name__)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
    s_handler = StreamHandler()
    s_handler.setLevel(logging.INFO)
    s_handler.setFormatter(formatter)
    log.addHandler(s_handler)

    yield log
    # end def


@pytest.mark.run(order=10)
def test_init_and_logging(logger: Logger):
    logger.info('init_and_logging')

    my_logger = CloudEventsLogger('test_init_and_logging', app='test_cloudevents_logger',
                                  type='com.timberlandchapel.logging',
                                  source='test_cloudevents_logger',
                                  level=logging.DEBUG)

    my_logger.log(logging.INFO, 'test')
    # end def


@pytest.mark.run(order=20)
@pytest.mark.parametrize('func', [('debug'),
                         ('info'), ('warning'), ('error'), ('critical')])
def test_logging_by_level(func: str, logger: Logger):
    logger.info('logging_by_level')

    my_logger = CloudEventsLogger('test_logging_by_level', app='test_cloudevents_logger',
                                  type='com.timberlandchapel.logging',
                                  source='test_cloudevents_logger',
                                  level=logging.DEBUG)

    callable = getattr(my_logger, func)
    callable('test')
    # end def


@pytest.mark.run(order=30)
@pytest.mark.parametrize('func', [('debug'),
                         ('info'), ('warning'), ('error'), ('critical')])
def test_logging_by_level_with_data(func: str, logger: Logger):
    logger.info('logging_by_level_with_data')

    my_logger = CloudEventsLogger('test_logging_by_level_with_data', app='test_cloudevents_logger',
                                  type='com.timberlandchapel.logging',
                                  source='test_cloudevents_logger',
                                  level=logging.DEBUG)

    callable = getattr(my_logger, func)
    callable(
        'test',
        extra={
            'type': 'type_overrides',
            'source': 'source_overrides',
            'data': {
                'attribute_1': 'value_1',
                'attribute_2': 20}})
    # end def
