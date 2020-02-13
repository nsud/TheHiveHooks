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
    'CaseCreation',
    'CaseTaskCreation',
    'CaseTaskLogCreation',
    'CaseTaskUpdate',
    'CaseUpdate'
]

for e in events:
    make_handler_func(e)

# Sample handler for case closing
@ee.on('CaseUpdate')
def caseClosed(event):
    print('caseClosed', event.get('dataType'), event.get('data'), event.get('ioc'))
    if event['ioc']:
        print(event)
        app.logger.info('{}:{} has been marked as IOC'.format(event.get('dataType'), event.get('data')))

def caseIsIOC(event):
    print('caseIsIOC', event.get('dataType'), event.get('data'), event.get('ioc'))
    if event['ioc']:
        print(event)
        app.logger.info('{}:{} has been marked as IOC'.format(event.get('dataType'), event.get('data')))
