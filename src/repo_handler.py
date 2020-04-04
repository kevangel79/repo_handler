#!/usr/bin/env python

import requests
import sys
import subprocess

organization = 'ARGOeu'
repos_list = [
 'argo-nagios-ams-publisher',
 'nagios-plugins-seadatacloud-check_cas',
 'nagios-plugins-seadatacloud-nvs2',
 'sdc-nerc-spqrql',
 'sdc-cdi-httpapi',
 'nagios-plugins-argo',
 'nagios-plugins-fedcloud',
 'nagios-plugins-eudat-gitlab',
 'ams-push-server',
 'argo-api-authn',
 'nagios-plugins-argo-authn',
 'b2share-nagios-plugin',
 'nagios-plugins-eudat-b2note',
 'nagios-plugins-eudat-b2handle',
 'b2note',
 'md-ingestion',
 'nagios-plugins-eudat-b2safe',
 'b2access-probe',
 'agora-probes',
 'nagios-plugins-eudat-b2stage'
]

#Check repos existance
repos = []
for repo_name in repos_list: 
    request = requests.get('https://api.github.com/repos/'+ organization +'/'+repo_name)
    if request.status_code != 200:
        print('---> Error: repo named \"'+repo_name+'\" does not exist in organization '+organization)
    else:
        repos.append(repo_name)
    
#Fork each repo
headers = {'Authorization': 'token ' + sys.argv[1]} 
for repo_name in repos:
    request = requests.post('https://api.github.com/repos/'+ organization +'/'+repo_name+'/forks', headers=headers )
    if request.status_code != 200:
        print('---> Error: repo named \"'+repo_name+'\" can\'t be forked '+organization)
exit(1)
try:
    os.mkdir('repos')
except:
    print('---> Folder already exists')

for repo_name in repos:
    subprocess.run(['git','clone','git@github.com:kevangel79/'+repo_name+'.git'])

