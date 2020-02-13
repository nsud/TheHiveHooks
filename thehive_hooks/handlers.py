import json
from thehive_hooks import app
from thehive_hooks import ee


def make_handler_func(event_name):
    @ee.on(event_name)
    def _handler(event):
        app.logger.info('Handle {}: Event={}'.format(event_name, json.dumps(event, indent=4, sort_keys=True)))

    return _handler

events = [

    #'CaseArtifactCreation',
    #'CaseArtifactJobCreation',
    #'CaseArtifactJobUpdate',
    #'CaseArtifactJobUpdate',
    'CaseArtifactUpdate',
    #'CaseCreation',
    #'CaseTaskCreation',
    #'CaseTaskLogCreation',
    #'CaseTaskUpdate',
    #'CaseUpdate'
]

for e in events:
    print(e)
    make_handler_func(e)

# Sample handler for case closing
@ee.on('CaseArtifactUpdate')
def caseNotIsIOC(event):
    print(event)
    print('Example', event.get('details').get('dataType'), event.get('details').get('data'), event.get('details').get('ioc'))
    if not event.get('details').get('ioc'):
        print(event)
        app.logger.info('{}:{} has not been marked as IOC'.format(
            event.get('details').get('dataType'), event.get('details').get('data')))


@ee.on('CaseArtifactUpdate')
def caseIsIOC(event):
    print('caseIsIOC: ', event.get('details').get('dataType'), event.get('details').get('data'), event.get('details').get('ioc'))
    if event.get('details').get('ioc'):
        print(event)
        app.logger.info('{}:{} has been marked as IOC'.format(
            event.get('details').get('dataType'), event.get('details').get('data')))
