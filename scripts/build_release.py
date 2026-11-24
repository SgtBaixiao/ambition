"""Build deterministic, content-hashed skill and refinement archives."""
import hashlib
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def make_archive(folder, destination):
    files = sorted(p for p in folder.rglob('*') if p.is_file())
    assert files and not any(p.is_symlink() for p in folder.rglob('*'))
    manifest = {}
    with zipfile.ZipFile(destination, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            relative = str(path.relative_to(folder))
            # Historical entrypoints are snapshots, so installers discover only the final Skill.
            name = 'ambition/' + ('SKILL.md' if relative == 'SKILL.md.snapshot' else relative)
            content = path.read_bytes()
            info = zipfile.ZipInfo(name, date_time=(2026, 11, 24, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)
            manifest[name] = hashlib.sha256(content).hexdigest()
        if 'ambition/LICENSE' not in manifest:
            content = (ROOT / 'LICENSE').read_bytes()
            info = zipfile.ZipInfo('ambition/LICENSE', date_time=(2026, 11, 24, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)
            manifest['ambition/LICENSE'] = hashlib.sha256(content).hexdigest()
    with zipfile.ZipFile(destination) as archive:
        assert archive.testzip() is None
        assert set(archive.namelist()) == set(manifest)
        for name in archive.namelist():
            assert hashlib.sha256(archive.read(name)).hexdigest() == manifest[name]
    return manifest


def main():
    folder = ROOT / 'skills/ambition'
    drafts = ROOT / 'drafts'
    folders = {'final': folder, **{label: drafts / label
               for label in ['pass-1-article', 'pass-2-user']}}
    reference_counts = {}
    for label, source in folders.items():
        local_links = 0
        for path in list(source.rglob('*.md')) + list(source.glob('SKILL.md.snapshot')):
            text = path.read_text()
            assert '/Users/' not in text and '/private/tmp/' not in text
            for target in re.findall(r'\]\(([^)]+)\)', text):
                if '://' in target or target.startswith('#'):
                    continue
                assert (path.parent / target.split('#')[0]).is_file(), (path, target)
                local_links += 1
        reference_counts[label] = local_links
    destination = ROOT / 'dist'
    destination.mkdir(exist_ok=True)
    manifest = make_archive(folder, destination / 'ambition-v1.0.0.zip')
    draft_manifests = {}
    for label in ['pass-1-article', 'pass-2-user']:
        draft_manifests[label] = make_archive(drafts / label, destination / (label + '.zip'))
    assert manifest == draft_manifests['pass-2-user'], 'Final differs from frozen second pass'
    result = {'version': 'v1.0.0', 'skill_files': manifest,
              'local_reference_counts': reference_counts, 'draft_files': draft_manifests}
    (destination / 'manifest.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    lines = [hashlib.sha256(p.read_bytes()).hexdigest() + '  ' + p.name
             for p in sorted(destination.iterdir()) if p.is_file() and p.name != 'SHA256SUMS']
    (destination / 'SHA256SUMS').write_text('\n'.join(lines) + '\n')
    print(json.dumps({'skill_files': len(manifest), 'local_references': reference_counts,
                      'refinement_archives': len(draft_manifests)}, indent=2))


if __name__ == '__main__':
    main()
