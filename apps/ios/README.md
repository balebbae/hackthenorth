# iOS app

One SwiftUI app for all four phones. The role picked on first launch decides what
the phone does:

| Role | What runs |
| --- | --- |
| Front | ARKit session with LiDAR depth, obstacle detection, speech, and a loop that snapshots the camera every 200 ms and posts it to Niantic Spatial |
| Left, Right, Back | Haptic buzzer only. No camera. |

## Layout

| Folder | Contents |
| --- | --- |
| `App/` | Entry point, root view, design tokens from `FRONTEND_STYLE.md` |
| `Features/Roles` | `DeviceRole`, persisted `RoleStore`, role picker screen |
| `Features/Settings` | `CameraSettings`, the one ARKit configuration and capture settings shared by every consumer, plus its form |
| `Features/Front` | `FrontPipeline` wiring and the front screen |
| `Features/Haptic` | Side and back phone screen |
| `Services/AR` | `ARSessionController`, the single ARKit session |
| `Services/Localization` | `LocalizationQueryLoop` (200 ms capture), `FrameEncoder`, `NianticRESTTransport` |
| `Services/Obstacles` | `ObstacleDetector` (after Shepherd) and `ObstacleCuePolicy` |
| `Services/Speech`, `Services/Haptics` | Speech coordinator and haptic controller |
| `Tests/Unit`, `Tests/UI` | XCTest and XCUITest targets |

## Build

The Xcode project is generated from `project.yml` with [xcodegen](https://github.com/yonaskolb/XcodeGen):

```sh
brew install xcodegen
cd apps/ios
xcodegen generate
open NavigationAssistant.xcodeproj
```

Deployment target is iOS 26.4. To run on a phone without a paid developer account,
add your Apple ID under Xcode > Settings > Accounts and let Xcode manage signing.

## Tests

```sh
xcodebuild test -project NavigationAssistant.xcodeproj -scheme NavigationAssistant \
  -destination 'platform=iOS Simulator,name=iPhone 17 Pro'
```

ARKit does not run on the simulator. There the front screen uses a flat placeholder
frame so the query loop, settings, and UI can still be exercised.

## Niantic

Set the developer token and endpoint in Settings on the front phone. Without a token
the loop still captures and encodes frames but reports them as skipped. The request
body shape in `NianticRESTTransport` is a placeholder until the localization endpoint
is confirmed; the supported path in Niantic's docs is the NSDK Swift package, which
person 2 can plug in behind the same `LocalizationTransport` protocol.
