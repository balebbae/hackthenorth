import Foundation
import CoreImage
import CoreVideo
import UIKit

/// Downscales a camera pixel buffer and encodes it as JPEG for upload.
struct FrameEncoder: Sendable {
    let maxDimension: Int
    let quality: Double

    private static let context = CIContext(options: [.useSoftwareRenderer: false])

    func encode(_ pixelBuffer: CVPixelBuffer) -> (data: Data, width: Int, height: Int)? {
        var image = CIImage(cvPixelBuffer: pixelBuffer).oriented(.right) // portrait mount
        let longest = max(image.extent.width, image.extent.height)
        if longest > CGFloat(maxDimension) {
            let scale = CGFloat(maxDimension) / longest
            image = image.transformed(by: CGAffineTransform(scaleX: scale, y: scale))
        }
        let colorSpace = CGColorSpaceCreateDeviceRGB()
        guard let data = Self.context.jpegRepresentation(
            of: image,
            colorSpace: colorSpace,
            options: [kCGImageDestinationLossyCompressionQuality as CIImageRepresentationOption: quality]
        ) else { return nil }
        return (data, Int(image.extent.width.rounded()), Int(image.extent.height.rounded()))
    }

    /// A flat gray test frame used when no camera is available, such as on the simulator.
    static func makePlaceholderPixelBuffer(width: Int = 640, height: Int = 480) -> CVPixelBuffer? {
        var buffer: CVPixelBuffer?
        let attrs: [CFString: Any] = [kCVPixelBufferCGImageCompatibilityKey: true,
                                      kCVPixelBufferCGBitmapContextCompatibilityKey: true]
        CVPixelBufferCreate(kCFAllocatorDefault, width, height, kCVPixelFormatType_32BGRA, attrs as CFDictionary, &buffer)
        guard let buffer else { return nil }
        CVPixelBufferLockBaseAddress(buffer, [])
        if let base = CVPixelBufferGetBaseAddress(buffer) {
            memset(base, 0x80, CVPixelBufferGetBytesPerRow(buffer) * height)
        }
        CVPixelBufferUnlockBaseAddress(buffer, [])
        return buffer
    }
}
