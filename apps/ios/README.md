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

## Niantic and backend

Localization uses the Niantic Spatial SDK (Swift package `nsdk-library-xcframework`).
`NianticLocalizer` creates one NSDK session fed by our ARKit session, fetches the
Site's VPS anchor payload through the Sites API, tracks that anchor, and turns each
anchor update into the device pose in the site frame. The SDK submits camera frames
itself at 5 requests a second until the first fix, then once a second.
`LocalizationReporter` posts fixes to the Wander backend's `POST /worlds/{id}/localize`
and in-between ARKit poses to `POST /sessions/{id}/pose`, at most five times a second.

Secrets never go in git. Copy `Resources/LocalConfig.example.plist` to
`Resources/LocalConfig.plist` and fill in the backend URL and key, the Niantic
developer token, and the Site ID. Those values seed Settings on first launch and can
be edited on the phone. Without a token and Site ID the front phone falls back to the
placeholder REST loop, which captures and logs frames without sending them.

The backend world must carry the same `nianticSiteId` and an `alignment.frame` of
`niantic-vps` before `/localize` accepts fixes.
