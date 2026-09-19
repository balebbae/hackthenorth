# Niantic Spatial documentation mirror

Offline mirror of https://www.nianticspatial.com/docs/ captured 2026-09-19 for the
HTN navigation assistant. Nothing here is our code; it is reference material for
the iOS localization work.

## Where to look first (Swift / iOS)

The HTML guide pages render the **Unity** platform tab by default, so the
`nsdk/` markdown mostly shows Unity content. The `llms-*` text files expand
every platform tab under `### Platform: swift|kotlin|unity` headings, so use
those for Swift:

| Need | File |
| --- | --- |
| Install the Swift package, create `NSDKSession`, feed ARKit frames | `llms-nsdk/setup.txt` (search "Platform: swift") |
| Scan a space with the Scaniverse app, publish a Site | `llms-scaniverse/quickstart.txt`, `llms-scaniverse/techniques.txt` |
| First end-to-end localization | `llms-nsdk/first_localization.txt` |
| Five-part VPS2 wayfinding tutorial | `llms-nsdk/vps2e2e/*.txt` |
| VPS2 concepts, tracking states | `llms-nsdk/features/vps2.txt`, `llms-nsdk/core_concepts.txt` |
| Swift API index | `llms-api-swift.txt`, per-class files in `llms-api-swift/` |
| Key Swift classes | `NSDK.class-NSDKSession`, `NSDK.class-NSDKVps2Session`, `NSDK.class-NSDKSitesSession`, `NSDK.class-DefaultSessionDataSource` |

## Layout

| Folder | Contents |
| --- | --- |
| `index.md`, `nsdk/` | Guide pages converted from HTML (Unity tab shown) |
| `nsdk/3.17.0/` | Older 3.17.0 guides and `apiref/` for all three platforms |
| `api/swift/`, `api/unity/`, `api/kotlin/` | Current API reference converted from HTML |
| `scaniverse/` | Scaniverse capture and publishing guides (HTML-derived) |
| `llms-nsdk/` | Guides as plain text with all platform tabs expanded |
| `llms-api-swift/`, `llms-api-unity/`, `llms-api-kotlin/` | One text file per API symbol |
| `llms-scaniverse/` | Scaniverse guides as plain text |
| `llms*.txt` | Index files linking the per-page text files |

Each markdown file starts with `source:` and `title:` frontmatter pointing at the
original URL. Images were not downloaded.

## SDK downloads

- Swift package: https://github.com/nianticspatial/nsdk-library-xcframework
- Swift samples: https://github.com/nianticspatial/nsdk-samples-swift
