import XCTest

final class RolePickerUITests: XCTestCase {
    private func launch() -> XCUIApplication {
        let app = XCUIApplication()
        app.launchArguments = ["-resetState"]
        app.launch()
        return app
    }

    func testPickHapticRoleShowsHapticScreenAndPersists() {
        let app = launch()
        XCTAssertTrue(app.staticTexts["Where is this phone?"].waitForExistence(timeout: 5))

        let continueButton = app.buttons["rolePicker.continue"]
        XCTAssertFalse(continueButton.isEnabled)
        app.buttons["rolePicker.option.left"].tap()
        XCTAssertTrue(continueButton.isEnabled)
        continueButton.tap()

        XCTAssertTrue(app.staticTexts["haptic.title"].waitForExistence(timeout: 5))
        XCTAssertEqual(app.staticTexts["haptic.title"].label, "Left shoulder")
        app.buttons["haptic.testBuzz"].tap()
        XCTAssertTrue(app.staticTexts["Buzzes: 1"].waitForExistence(timeout: 2))

        // Relaunch without reset: role should stick.
        app.terminate()
        let again = XCUIApplication()
        again.launch()
        XCTAssertTrue(again.staticTexts["haptic.title"].waitForExistence(timeout: 5))
        XCTAssertEqual(again.staticTexts["haptic.title"].label, "Left shoulder")
    }

    func testFrontRoleRunsQueryLoopAndSettingsChangeInterval() {
        // Real devices show the camera permission prompt on first Start; allow it.
        addUIInterruptionMonitor(withDescription: "Camera permission") { alert in
            for label in ["Allow", "OK", "Allow While Using App"] where alert.buttons[label].exists {
                alert.buttons[label].tap()
                return true
            }
            return false
        }
        let app = launch()
        app.buttons["rolePicker.option.front"].tap()
        app.buttons["rolePicker.continue"].tap()

        XCTAssertTrue(app.staticTexts["Front"].waitForExistence(timeout: 5))
        XCTAssertTrue(app.staticTexts["front.queryInterval"].label.contains("Stopped"))

        app.buttons["front.start"].tap()
        app.tap() // gives the interruption monitor a chance to dismiss a permission alert
        XCTAssertTrue(app.staticTexts["front.queryInterval"].waitForExistence(timeout: 2))
        XCTAssertEqual(app.staticTexts["front.queryInterval"].label, "Every 200 ms")

        // About 1.5 s later the loop should have ticked several times and skipped (no token).
        let skipped = app.staticTexts["front.stat.skipped"]
        let predicate = NSPredicate { _, _ in
            let value = skipped.label.split(separator: ":").last.map { Int($0.trimmingCharacters(in: .whitespaces)) ?? 0 } ?? 0
            return value >= 3
        }
        let exp = XCTNSPredicateExpectation(predicate: predicate, object: nil)
        XCTAssertEqual(XCTWaiter().wait(for: [exp], timeout: 6), .completed, "loop did not tick: \(skipped.label)")

        app.buttons["front.stop"].tap()
        XCTAssertTrue(app.buttons["front.start"].waitForExistence(timeout: 2))

        // Change the interval in settings and confirm the front screen reflects it.
        app.buttons["front.settings"].tap()
        XCTAssertTrue(app.navigationBars["Settings"].waitForExistence(timeout: 3))
        app.buttons["settings.captureInterval"].tap()
        XCTAssertTrue(app.buttons["300 ms"].waitForExistence(timeout: 3))
        app.buttons["300 ms"].tap()
        app.buttons["settings.done"].tap()
        app.buttons["front.start"].tap()
        XCTAssertTrue(app.staticTexts["Every 300 ms"].waitForExistence(timeout: 3))
        app.buttons["front.stop"].tap()

        // Change role from settings returns to the picker.
        app.buttons["front.settings"].tap()
        XCTAssertTrue(app.navigationBars["Settings"].waitForExistence(timeout: 3))
        app.swipeUp()
        XCTAssertTrue(app.buttons["settings.changeRole"].waitForExistence(timeout: 3))
        app.buttons["settings.changeRole"].tap()
        XCTAssertTrue(app.staticTexts["Where is this phone?"].waitForExistence(timeout: 5))
    }
}
