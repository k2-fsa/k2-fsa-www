import requests
from typing import Dict

K2_CPU_PAGE="https://k2-fsa.github.io/k2/cpu.html"

def generate_html(links: Dict[str, str]):
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

    r = requests.get(K2_CPU_PAGE)
    for line in r.text.split("<br/>"):
        html += f"<tr><td>{line}</td></tr>"

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

a = None
with open("custom/resources.html", "w") as f:
    f.write(generate_html(a))
