from fabric.api import local
from fabric.context_managers import lcd
import os


BASE_DIR = os.path.realpath(os.path.dirname(__file__))
BUILD_DIR = os.path.join(BASE_DIR, '_build')
LANGUAGES = ['en']
MAIN_TARGET = 'html'
REPOSITORY = 'https://github.com/SonOfLilit/python-beginners.git'


def setup():
    clean()
    target_dir = os.path.join(BUILD_DIR, MAIN_TARGET)
    with lcd(BASE_DIR):
        local('mkdir -p %s' % target_dir)
        local('git clone %s %s' % (REPOSITORY, target_dir))
    with lcd(target_dir):
        local('git symbolic-ref HEAD refs/heads/gh-pages')
        local('rm -rf .git/index')
        local('git clean -fdx')
        local('git pull origin gh-pages')
        local('touch .nojekyll')


def build(target='html'):
    for language in LANGUAGES:
        build_language(language, target)
    if 'html' in target:
        static_files = os.path.join(BASE_DIR, '_static', '*')
        target_dir = os.path.join(BUILD_DIR, target)
        local('cp %s %s' % (static_files, target_dir))
        

def build_language(language, target='html'):
    args = [
        'sphinx-build',
        '-b',
        target,
        '-d',
        os.path.join(BUILD_DIR, 'doctrees', language),
        os.path.join(BASE_DIR, language),
        os.path.join(BUILD_DIR, target, language),
    ]
    command = ' '.join(args)
    local(command)


def clean():
    local('rm -rf %s' % os.path.join(BUILD_DIR, '*', '*'))
