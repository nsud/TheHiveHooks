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
def caseIsIoc(event):
    print(event)
    if event['details']['ioc']:
        app.logger.info('{} has been marked as IOC'.format(event['data']))
