FROM fedora:27

RUN dnf install -y ansible

COPY . /playbook

WORKDIR /playbook

RUN ansible-playbook -i inventory clients.yml
