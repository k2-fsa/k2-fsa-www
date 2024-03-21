import json
import requests
import re

K2_CUDA_PAGE="https://k2-fsa.github.io/k2/cuda.html"
K2_CPU_PAGE="https://k2-fsa.github.io/k2/cpu.html"

k2_wheels = {}

# for linux cuda
r = requests.get(K2_CUDA_PAGE)
url_pattern = r"href=\"(.*)\">"
pattern = r"k2-(\d\.\d+\.\d+\.dev\d{8})\+cuda(\d+\.\d)\.torch(\d\.\d+\.\d(\.dev\d{8})?)-(\S+)-(\S+)-(\S+)\.whl"
for line in r.text.split("<br/>"):
    m = re.search(url_pattern, line)
    if m is None:
        continue
    url = m.group(1)
    file_name = url.split("/")[-1]
    m = re.search(pattern, file_name)
    assert m is not None
    k2_version, cuda_version, torch_version, os = m.group(1), m.group(2), m.group(3), m.group(7)
    if "manylinux" not in os:
        continue
    install = f"""# Install Pytorch
    pip install torch=={torch_version} --index-url https://download.pytorch.org/whl/cu{cuda_version.replace(".","")}

    # Install k2
    pip install k2=={k2_version}+cuda{cuda_version}.torch{torch_version} -f https://k2-fsa.github.io/k2/cuda.html
    """
    k2_wheels[(k2_version, "Linux", torch_version, cuda_version)] = install

# for cpu (windows, macos, linux)
r = requests.get(K2_CPU_PAGE)
url_pattern = r"href=\"(.*)\">"
pattern = r"k2-(\d\.\d+\.\d+\.dev\d{8})\+cpu\.torch(\d\.\d+\.\d(\.dev\d{8})?)-(\S+)-(\S+)-(\S+)\.whl"
for line in r.text.split("<br/>"):
    m = re.search(url_pattern, line)
    if m is None:
        continue
    url = m.group(1)
    file_name = url.split("/")[-1]
    m = re.search(pattern, file_name)
    assert m is not None
    k2_version, torch_version, _, _, _, os = m.group(1), m.group(2), m.group(3),m.group(4),m.group(5), m.group(6)
    if "macosx" in os:
        os = "Macos"
    elif "win" in os:
        os = "Windows"
    elif "manylinux" in os:
        os = "Linux"
    else:
        continue

    install = f"""# Install Pytorch
    pip install torch=={torch_version} --index-url https://download.pytorch.org/whl/cpu

    # Install k2
    pip install k2=={k2_version}+cpu.torch{torch_version} -f https://k2-fsa.github.io/k2/cpu.html
    """
    k2_wheels[(k2_version, os, torch_version, "CPU")] = install

En_wheels = []
Cn_wheels = []  # Cn might have different index page
versions = {}  # 
for k in sorted(k2_wheels.keys(), reverse=True):
    v = k2_wheels[k]
    k2, os, torch, platform = k
    # only display version as major.minor.patch
    v_k2 = k2.split(".dev")[0]
    v_torch = torch.split(".dev")[0]
    v_k = (v_k2, os, v_torch, platform)
    if v_k not in versions:
        En_wheels.append({
            "build" : v_k2,
            "os" : os,
            "pytorch" : v_torch,
            "platform" : platform if platform == "CPU" else f"CUDA{platform.replace('.', '')}",
            "install" : v
        })
        Cn_wheels.append({
            "build" : v_k2,
            "os" : os,
            "pytorch" : v_torch,
            "platform" : platform if platform == "CPU" else f"CUDA{platform.replace('.', '')}",
            "install" : v
        })
        versions[v_k] = 1

with open("custom/assets/data/k2_whl_en.json", "w") as f:
    json.dump(En_wheels, f, indent=2)
with open("custom/assets/data/k2_whl_cn.json", "w") as f:
    json.dump(Cn_wheels, f, indent=2)