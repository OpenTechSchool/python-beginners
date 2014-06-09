from fabric.api import local
import os
import sys
if sys.version_info[0] < 3:
    import SimpleHTTPServer as httpserver
    import SocketServer as socketserver
else:
    import http.server as httpserver
    import socketserver


BASE_DIR = os.path.realpath(os.path.dirname(__file__))
BUILD_DIR = os.path.join(BASE_DIR, '_build')
SOURCE_DIR = os.path.join(BASE_DIR, 'source')
LOCALE_DIR = os.path.join(SOURCE_DIR, 'locale',
                          '%s', 'LC_MESSAGES')
LANGUAGES = set(['en', 'de', 'ru', 'ko', 'es_CL'])
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


def build(language=None, target=MAIN_TARGET):
    if language is None:
        print('Please build a specific language; one of')
        print(', '.join(LANGUAGES))
        exit()
    elif language not in LANGUAGES:
        exit('Language %s not available.' % language)
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
    if 'html' in target:
        static_files = os.path.join(BASE_DIR, '_static', '*')
        target_dir = os.path.join(BUILD_DIR, target)
        local('cp %s %s' % (static_files, target_dir))
    print("build finished; the %s files are in %s." %
            (target, os.path.join(BUILD_DIR, target, language)))


def clean(language=None, target=MAIN_TARGET):
    if language is not None:
        local('rm -rf %s' % os.path.join(BUILD_DIR, target, language))
    else:
        local('rm -rf %s' % os.path.join(BUILD_DIR, target))


def serve(port=SERVE_PORT, serve_dir=None):
    """Run a web server to serve the built project"""
    if serve_dir is None:
        serve_dir = os.path.join(BUILD_DIR, MAIN_TARGET)
    port = int(port)
    os.chdir(serve_dir)
    handler = httpserver.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), handler)
    print("serving on http://%s:%s" % httpd.server_address)
    httpd.serve_forever()


def update_pos(language):
    """Update .po files from the source pot files"""
    if language not in LANGUAGES:
        exit('Language %s not available.' % language)
    gen_pots(language)
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
    if language not in LANGUAGES:
        exit('Language %s not available.' % language)
    args = [
        'sphinx-intl build',
        '-l %s' % language,
        '-c',
        os.path.join(SOURCE_DIR, 'conf.py'),
    ]
    local(' '.join(args))


def gen_pots(language='en'):
    """Generate .pot templates from sphinx source files"""
    args = [
        'sphinx-build',
        '-b gettext',
        '-D language=%s' % language,
        SOURCE_DIR,
        os.path.join(BUILD_DIR, 'locale', language),
    ]
    local(' '.join(args))
