#!/usr/bin/env python

import requests
organization = 'ARGOeu'
repos_list = [
'argo-nagios-ams-publisher'
# 'nagios-plugins-seadatacloud-check_cas',
# 'nagios-plugins-seadatacloud-nvs2',
# 'sdc-nerc-spqrql',
# 'sdc-cdi-httpapi',
# 'nagios-plugins-argo',
# 'nagios-plugins-fedcloud',
# 'nagios-plugins-eudat-gitlab',
# 'ams-push-server',
# 'argo-api-authn',
# 'nagios-plugins-argo-authn',
# 'b2share-nagios-plugin',
# 'nagios-plugins-eudat-b2note',
# 'nagios-plugins-eudat-b2handle',
# 'b2note',
# 'md-ingestion',
# 'nagios-plugins-eudat-b2safe',
# 'b2access-probe',
# 'agora-probes',
# 'nagios-plugins-eudat-b2stage'
]

repos = []
for repo_name in repos_list: 
    request = requests.get('https://api.github.com/repos/'+ organization +'/'+repo_name)
    if request.status_code != 200:
        print('---> Error: repo named \"'+repo_name+'\" does not exist in organization '+organization)
    else:
        repos.append(repo_name)

