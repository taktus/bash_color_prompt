Role Name
=========

bash_color_promot sets up colored prompt for existing linux users

Requirements
------------

Users must exist

Role Variables
--------------

bash_color_prompt_users:- a hash with users\

default []

example:
```
bash_color_prompt_users:
  - name: test_yes
    color_prompt: yes
    color: '33'
  - name: test_no
    color_prompt: no
    color: '32'
```


Dependencies
------------

none

Example Playbook
----------------
```
- name: set up color prompts
  hosts: all

  vars:
    bash_color_prompt_users:
      - name: test_yes
        color_prompt: yes
        color: '33'
      - name: test_no
        color_prompt: no
        color: '32'

  roles:

    - role: bash_color_prompt
      become: yes
```

License
-------

BSD

Author Information
------------------

author: Marek Krasnowski
company: TAKTUS Marek Krasnowski

