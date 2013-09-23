from fabric.api import local
from fabric.context_managers import lcd
import os
try:
    import SimpleHTTPServer as httpserver
    import SocketServer as socketserver
except ImportError:
    import http.server as httpserver
    import socketserver


BASE_DIR = os.path.realpath(os.path.dirname(__file__))
BUILD_DIR = os.path.join(BASE_DIR, '_build')
SOURCE_DIR = os.path.join(BASE_DIR, 'source')
LOCALE_DIR = os.path.join(SOURCE_DIR, 'locale',
                          '%s', 'LC_MESSAGES')
LANGUAGES = {'en', 'de'}
MAIN_TARGET = 'html'
REPOSITORY = 'git@github.com:OpenTechSchool/python-beginners.git'
SERVE_PORT = 8000


def setup():
    """Setup html build directory to push to repo"""
    clean()
    target_dir = os.path.join(BUILD_DIR, MAIN_TARGET)
    local('mkdir -p %s' % target_dir)
    local('git clone %s -b %s --single-branch %s' %
          (REPOSITORY, 'gh-pages', target_dir))
    with lcd(target_dir):
        local('rm -rf ./*')
        local('touch .nojekyll')
    build()


def build(target=MAIN_TARGET):
    for language in LANGUAGES:
        build_language(language, target)
    if 'html' in target:
        static_files = os.path.join(BASE_DIR, '_static', '*')
        target_dir = os.path.join(BUILD_DIR, target)
        local('cp %s %s' % (static_files, target_dir))


def clean(target=MAIN_TARGET):
    local('rm -rf %s' % os.path.join(BUILD_DIR, target))


def serve(serve_dir=BUILD_DIR+'/'+MAIN_TARGET):
    """Run a web server to serve the built project"""
    os.chdir(serve_dir)
    handler = httpserver.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", SERVE_PORT), handler)
    print("serving on http://%s:%s" % httpd.server_address)
    httpd.serve_forever()


def build_language(language, target=MAIN_TARGET):
    if os.path.isdir(LOCALE_DIR % language):
        compile_pos(language)
    args = [
        'sphinx-build',
        '-b',  # builder type
        target,
        '-d',  # doctree path
        os.path.join(BUILD_DIR, 'doctrees'),
        '-D',
        'language=%s' % language,
        SOURCE_DIR,
        os.path.join(BUILD_DIR, target, language),  # output path
    ]
    local(' '.join(args))


def update_pos(language=None):
    """Update .po files if the source has changed"""
    gen_pots(language)
    if language is None:
        lang_set = LANGUAGES - {'en'}
    else:
        lang_set = language
    for language in lang_set:
        args = [
            'sphinx-intl update',
            '-l %s ' % language,
            '-p',
            os.path.join(BUILD_DIR, 'locale', language),
            '-c',
            os.path.join(SOURCE_DIR, 'conf.py'),
        ]
        local(' '.join(args))


def compile_pos(language):
    """Compile .po files into .mo files"""
    args = [
        'sphinx-intl build',
        '-l %s' % language,
        '-c',
        os.path.join(SOURCE_DIR, 'conf.py'),
    ]
    local(' '.join(args))


def gen_pots(language=None):
    """Generate .pot templates from sphinx source files"""
    if language is None:
        lang_set = LANGUAGES - {'en'}
    else:
        lang_set = language
    for language in lang_set:
        args = [
            'sphinx-build',
            '-b gettext',
            '-D language=%s' % language,
            SOURCE_DIR,
            os.path.join(BUILD_DIR, 'locale', language),
        ]
        local(' '.join(args))
