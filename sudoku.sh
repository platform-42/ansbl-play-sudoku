#!/usr/bin/env bash
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
BRANCH=main
cd ${SCRIPTPATH}

ansible-galaxy collection install git@github.com:platform-42/platform42.neo4j.git,${BRANCH}
ansible-playbook -i hosts/hosts.yml $(basename ${0%.*}).yml