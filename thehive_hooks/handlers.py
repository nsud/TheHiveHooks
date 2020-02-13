import json
from thehive_hooks import app
from thehive_hooks import ee


def make_handler_func(event_name):
    @ee.on(event_name)
    def _handler(event):
        app.logger.info('Handle {}: Event={}'.format(event_name, json.dumps(event, indent=4, sort_keys=True)))

    return _handler

events = [

    'CaseArtifactUpdate',
    'CaseTaskUpdate'
]

for e in events:
    print(e)
    make_handler_func(e)


@ee.on('CaseArtifactUpdate')
def caseIsIOC(event):
    if event.get('details').get('ioc'):
        print(event)
        print('caseIsIOC: ', event.get('object').get('dataType'),
              event.get('object').get('data'), event.get('details').get('ioc'))

        app.logger.info('{}:{} has been marked as IOC'.format(
            event.get('object').get('dataType'), event.get('object').get('data')))
