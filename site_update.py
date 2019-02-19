from flask import Flask, request
import json
import os

app = Flask(__name__)

app_dir = os.path.dirname(os.path.realpath(__file__))

@app.route('/')
def hello():
    return 'Use POST /changed with colors body in JSON'

@app.route('/changed', methods=['POST'])
def changed():
    body = request.data
    print(body)
    success = handle_color_spec(json.loads(body))
    return json.dumps({'success':success}), (200 if success else 400), {'ContentType':'application/json'}


block_content_cache = {}

def get_block_content(name):
    global app_dir
    global block_content_cache
    if name not in block_content_cache:
        try:
            with open(f'{app_dir}/blocks/{name}.txt', 'r') as fh:
                content = fh.read()
                content = content.replace('\r', '')
                content = content.replace('\n', '')
        except IOError as x:
            print(f'Could not open {name} -- {x}')
            content = None
        block_content_cache[name] = content
        return content
    return block_content_cache[name]


def handle_color_spec(spec_colors):
    cleaned = [(str(name).lower(), x, y) for name, x, y in spec_colors]
    cleaned.sort(key=lambda t: t[2])
    combined = ''
    for name, x, y in cleaned:
        content = get_block_content(name)
        if not content:
            return False
        combined += content
        combined += '  '  # the wp cli command likes having at least two spaces between blocks
    enqueue_content_update(combined)
    return True


def enqueue_content_update(content):
    post_number = 4
    cmd = f"""wpe wp "post update {post_number} --post_content='{content}'" """
    print(content)
    os.system(cmd)
