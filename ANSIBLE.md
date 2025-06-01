## configuration management tools

- To push the changes to multiple machines
- ansible/puppet/saltstack
- difference between other tools and ansible
- puppet - push and pull - agent based
- saltstack - pull - both agent and agentless
- ansible - push - agentless - have used python to build
- idempotency - same changes on all machines
- scaling - ssh based -- keyless authentication 


# Ansible
## Components
- Control node -- Master node -- the machine where we run ansible commands -- it could be local machine
- Worker nodes -- where we actually want to push changes
- Inventory - source of information of all ip address of worker nodes - like sso config
- Playbook - yaml declarative file, where we declare what we want to do
- Modules -- reusable template which can be used by multiple configurations

```
ansible-project/
├── ansible.cfg  -- it is mandatory, core file required for ansible to run. Where we will define ssh based authentication.
├── inventory/
│   ├── dev
│   ├── prod
│   └── staging
├── group_vars/
│   ├── all.yml
│   └── dev.yml
├── host_vars/
│   └── webserver1.yml
├── roles/
│   └── webserver/
│       ├── tasks/       - Contains the main list of tasks to run when this role is included in a playbook
│       │   └── main.yml
│       ├── handlers/   -- Contains handlers, which are special tasks triggered by the notify: keyword (like restarting services)
│       │   └── main.yml
│       ├── templates/  -- Stores Jinja2 template files, such as configuration files (.j2). These are rendered with variables at runtime.
│       │   └── nginx.conf.j2
│       ├── files/
│       │   └── index.html -- nginx copies from index.html
│       ├── vars/
│       │   └── main.yml
│       ├── defaults/
│       │   └── main.yml
│       ├── meta/
│       │   └── main.yml -- who is contributor, what is version will be kept here - dependencies
│       └── README.md
├── playbooks/
│   └── site.yml
└── requirements.yml
```

inverntory can be written in .ini or in yml

`How to ensure worker nodes are running?`
- test -- ansible all -i <inventory-file> -m ping

static inverntory - where we will declare our ips
dynamic inventory - if it's cloud based to get a dynamic response
if the response is unreachable
- ip 
- ssh issue
- user key
- machine up or not

Run ansible playbook
ansible-playbook -i <inventory-file> <playbook.yml>

ansible.cfg
- location of inverntroy
- how to connect - ssh key and all
- user = ubuntu
- host-key-checking
- timeout
- privilege escalation


`ANSIBLE PLAYBOOKS`

- set of tasks that we want to run on vm
- state present - enabling the task
- state absent - disable the setting
- state started - to ensure that the container like nginx, docker is started

Direct apply
Output
- Play
- task
- changes/unchanged

Dry-run 
ansible-playbook  <playbook.yml> --check

`VARS, Templates and handlers`
- VARS -- Inline
- key-value pair 
vars:
 `name: nginx`
- cli -- 
`-e "app-port:8080"`
-e environment-variable

- Handlers:
decouple task of installing and running nginx
notify: `hanler-name` -- which looks for handler and run the task[like restarting nginx]

`Roles`

- ansible-galaxy init <role-directory> -- creates a role structure by running this command
- underplaybooks. Vars can be overwritten
    - 
    ```
    - roles: nginx
    vars: 
      name: nginc
      port: 8080
    ```

ansible-galaxy -- similar to dockerhub, if we want to push our code to public repo

to install others repos/projects
- `ansible-galaxy install <repo>`

testing
- dry-runs --check
- linting -- ansible-lint <playbook.yml>
- syntax checks --syntax-check
- molecule -- to test on local

`Ansible-Vault`

- To store secrets
- `ansible-vault create <secret.yml>`
- `ansible-playbook <secret.yml> --ask-vault-pass`

