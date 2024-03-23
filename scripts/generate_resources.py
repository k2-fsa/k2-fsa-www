import requests
import re
from typing import Dict, List, Set

def generate_html(resources: Dict[str, str]):
    html = """
    {% extends "main.html" %}

    {% block styles %}
    {{ super() }}
    <style>
        .md-source-file {
        display : none;
        }
        #filelist {
        border: none;
        }
        #filelist td {
        border: none;
        padding: 0px;
        }
    </style>
    {% endblock %}

    {% block content %}
    {{ super() }}
    <div style="margin: 20px 0px; width: 100%;">
        <input id="search" style="width: 75%;" class="md-input md-input--stretch" placeholder="Type to search...">
        <table id="filelist">
            <tbody>
    """

    for k, v in resources.items():
        html += f'<tr><td><a href="{v}" target="_blank">{k}</a></td></tr>\n'

    html += """
            </tbody>
        </table>
    </div>

    {% endblock %}

    {% block scripts %}
    {{ super() }}
    <script src="https://unpkg.com/xregexp/xregexp-all.js"></script>

    <script>
        var listItems = [].slice.call(document.querySelectorAll('#filelist tbody tr'));

        document.getElementById("search").addEventListener('keyup', function () {
            var i,
            // Word sequence _matching_ to input. All, except last, words must be _complete_.
            e = "(^|.*[^\\pL])" + this.value.trim().split(/\s+/).join("([^\\pL]|[^\\pL].*[^\\pL])") + ".*$",
            n = RegExp(e, "i");
            listItems.forEach(function(item) {
                item.removeAttribute('hidden');
            });
            listItems.filter(function(item) {
                i = item.querySelector('td').textContent.replace(/\s+/g, " ");
                return !n.test(i);
            }).forEach(function(item) {
                item.hidden = true;
            });
        });
        var q = "";
        var query = window.location.search.substring(1);
        var vars = query.split("&");
        for (var i=0;i<vars.length;i++) {
            var pair = vars[i].split("=");
            if(pair[0] == "s") {
            q = pair[1];
            break;
            }
        }
        if (q != "") {
        document.getElementById("search").value = q;
        document.getElementById("search").dispatchEvent(new KeyboardEvent('keyup', {
            'key': q[q.length-1]
        }));
        }
    </script>
    {% endblock %}
    """
    return html

def get_apks(link: str, resources: Dict[str, str]):
    r = requests.get(link)
    url_pattern = r"href=\"(.*)\".*>"
    latest_version = None
    for line in r.text.split("<br/>"):
        m = re.search(url_pattern, line)
        if m is None:
            continue
        url = m.group(1).strip()
        name = url.split("/")[-1]
        if name.endswith("apk"):
            version = "-".join(name.split("-")[0:3])
            if latest_version is None:
                latest_version = version
            else:
                if version != latest_version:
                    continue
            resources[name] = url

def get_releases(link: str, resources: Dict[str, str], tags: Set[str]):
    r = requests.get(link)
    releases = r.json()
    for i, release in enumerate(releases):
        if i == 0 or release["tag_name"] in tags:
            for asset in release["assets"]:
                url = asset["browser_download_url"]
                name = url.split("/")[-1]
                resources[name] = url


SHERPA_ONNX_RELEASE="https://api.github.com/repos/k2-fsa/sherpa-onnx/releases"
SHERPA_NCNN_RELEASE="https://api.github.com/repos/k2-fsa/sherpa-ncnn/releases"
SP_ID_APK="https://k2-fsa.github.io/sherpa/onnx/speaker-identification/apk.html"
TTS_APK="https://k2-fsa.github.io/sherpa/onnx/tts/apk.html"
TTS_ENGINE_APK="https://k2-fsa.github.io/sherpa/onnx/tts/apk-engine.html"
resources = {}

get_apks(SP_ID_APK, resources)
get_apks(TTS_APK, resources)
get_apks(TTS_ENGINE_APK, resources)
get_releases(SHERPA_ONNX_RELEASE, resources, set(["kws-models", "speaker-recongition-models", "tts-models", "asr-models"]))
get_releases(SHERPA_NCNN_RELEASE, resources, set(["models"]))

with open("custom/resources.html", "w") as f:
    f.write(generate_html(resources))
