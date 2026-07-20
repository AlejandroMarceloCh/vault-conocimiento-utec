"""Parser de frontmatter YAML-subset, SOLO stdlib (no pyyaml — no está en el intérprete).
Soporta: scalars, listas inline [a, b], listas por guiones, y mapas anidados de 1-2 niveles.
Es deliberadamente estricto: si algo no encaja, falla fuerte en vez de adivinar."""
import re

def split(text):
    """Devuelve (frontmatter_dict, body_str). Si no hay frontmatter, ({}, text)."""
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return {}, text
    return parse(m.group(1)), m.group(2)

def _scalar(v):
    v = v.strip()
    if not v:
        return None
    if v[0] in "\"'" and v[-1] == v[0]:
        return v[1:-1]
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        return [_scalar(x) for x in _split_commas(inner)] if inner else []
    return v

def _split_commas(s):
    out, buf, depth, q = [], "", 0, None
    for ch in s:
        if q:
            buf += ch
            if ch == q: q = None
        elif ch in "\"'":
            q = ch; buf += ch
        elif ch in "[{": depth += 1; buf += ch
        elif ch in "]}": depth -= 1; buf += ch
        elif ch == "," and depth == 0:
            out.append(buf); buf = ""
        else:
            buf += ch
    if buf.strip():
        out.append(buf)
    return out

def parse(fm):
    """Parsea el bloque de frontmatter (sin los ---). Indentación = anidamiento (2 espacios)."""
    root = {}
    stack = [(-1, root)]
    lines = fm.split("\n")
    i = 0
    while i < len(lines):
        raw = lines[i]
        if not raw.strip():
            i += 1; continue
        indent = len(raw) - len(raw.lstrip())
        line = raw.strip()
        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if line.startswith("- "):
            item = line[2:].strip()
            if not isinstance(parent, list):
                raise ValueError(f"lista bajo no-lista: {raw!r}")
            if ":" in item and not item.startswith(("\"", "'", "[")):
                d = {}
                k, v = item.split(":", 1)
                if v.strip():
                    d[k.strip()] = _scalar(v)
                else:
                    stack.append((indent, d))  # continua abajo
                parent.append(d)
                stack.append((indent + 1, d))
            else:
                parent.append(_scalar(item))
            i += 1; continue
        # key: value  |  key:
        if ":" not in line:
            raise ValueError(f"línea sin ':': {raw!r}")
        k, v = line.split(":", 1)
        k = k.strip(); v = v.strip()
        if v == "":
            # abre mapa o lista; decidir mirando la próxima línea no vacía
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            nxt = lines[j] if j < len(lines) else ""
            child = [] if nxt.strip().startswith("- ") else {}
            if isinstance(parent, dict):
                parent[k] = child
            stack.append((indent, child))
        else:
            if isinstance(parent, dict):
                parent[k] = _scalar(v)
        i += 1
    return root

def body_sha256(body):
    """Hash determinista del cuerpo: normaliza EOL y quita trailing whitespace por línea."""
    import hashlib
    norm = "\n".join(l.rstrip() for l in body.replace("\r\n", "\n").split("\n")).strip() + "\n"
    return "sha256:" + hashlib.sha256(norm.encode()).hexdigest()
