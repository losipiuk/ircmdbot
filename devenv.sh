#!/bin/bash -e

# stolen from https://raw.githubusercontent.com/kokosing/git-gifi/master/devenv.sh
# thanks grzesiek

if [[ "$VIRTUAL_ENV" == "" ]]; then 
  VIRTUAL_ENV="/Users/losipiuk/workspace/virtualenvs/ircmdbot"
fi
COMMANDS="help init install build release"
SETUP='python setup.py'

function _err() {
  echo $*
  exit 1
}

function _activate_virtual_env() {
  if [ -d $VIRTUAL_ENV ]; then
    source $VIRTUAL_ENV/bin/activate
  else
    _err "Unable to find virtual env at $VIRTUAL_ENV"
  fi
}

function init() {
  sudo apt-get install python-dev 
  virtualenv $VIRTUAL_ENV
  source $VIRTUAL_ENV/bin/activate
  _activate_virtual_env
  $SETUP develop
  pip install wheel
  pip install twine
  echo 
  echo "Remember to 'source $VIRTUAL_ENV/bin/activate', before coding"
}

function build() {
  _activate_virtual_env
  $SETUP flake8
#  $SETUP test
  $SETUP install
}

function release() {
  VERSION=$(cat setup.py  | grep version | sed 's/.*0\.\(.*\)-.*/\1/g')
  _change_version 0.$VERSION
  rm -rf dist
  build
  $SETUP register
  $SETUP bdist_wheel
  $SETUP bdist_wheel --universal
  $SETUP sdist
  twine upload dist/*
  NEXT_VERSION=$(echo $VERSION + 1 | bc)
  _change_version 0.$NEXT_VERSION-SNAPSHOT
  MESSAGE="Release 0.$VERSION"
  git commit -a -m "$MESSAGE"
  git tag -a -m "$MESSAGE" 0.$VERSION
  git push
  git push --tags
}

function _change_version() {
  sed 's/\(.*version=.\).*\(.,.*\)/\1'$1'\2/g' setup.py > tmp
  mv tmp setup.py
}

function help() {
  cat << EOF
$0 COMMAND [command arguments]

Commands:
  help  -   display this window
  init  -   init sandbox (install virtual env and dependencies)
  build -   build project
EOF
}

if [[ $# = 0 ]]; then
  help
  exit
fi

COMMAND=$1
shift
echo $COMMANDS | tr ' ' '\n' | grep -q "${COMMAND}" || _err "Invalid command: $COMMAND, try help command first."

$COMMAND $*
