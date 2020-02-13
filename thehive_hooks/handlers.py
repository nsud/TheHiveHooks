import json
from thehive_hooks import app
from thehive_hooks import ee


def make_handler_func(event_name):
    @ee.on(event_name)
    def _handler(event):
        app.logger.info('Handle {}: Event={}'.format(event_name, json.dumps(event, indent=4, sort_keys=True)))

    return _handler

events = [

    'CaseArtifactCreation',
    'CaseArtifactJobCreation',
    'CaseArtifactJobUpdate',
    'CaseArtifactJobUpdate',
    'CaseArtifactUpdate',
    #'CaseCreation',
    'CaseTaskCreation',
    'CaseTaskLogCreation',
    'CaseTaskUpdate',
    'CaseUpdate'
]

for e in events:
    print(e)
    make_handler_func(e)

# Sample handler for case closing
@ee.on('CaseUpdate')
def caseClosed(event):
    print(event)
    print('Example', event.get('dataType'), event.get('data'), event.get('ioc'))
    if not event.get('ioc'):
        print(event)
        app.logger.info('{}:{} has not been marked as IOC'.format(event.get('dataType'), event.get('data')))


@ee.on('CaseArtifactUpdate')
def caseIsIOC(event):
    print('caseIsIOC: ', event.get('dataType'), event.get('data'), event.get('ioc'))
    if event.get('ioc') is True:
        print(event)
        app.logger.info('{}:{} has been marked as IOC'.format(event.get('dataType'), event.get('data')))
