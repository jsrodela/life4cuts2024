import WebMWriter from 'webm-writer'

export async function createNDownloadVideo(frames: string[]): Promise<string> {
  const videoWriter = new WebMWriter({
      quality: 0.95,    // WebM image quality from 0.0 (worst) to 0.99999 (best), 1.00 (VP8L lossless) is not supported
      fileWriter: null, // FileWriter in order to stream to a file instead of buffering to memory (optional)
      fd: null,         // Node.js file handle to write to instead of buffering to memory (optional)

      // You must supply one of:
      frameDuration: 1000, // Duration of frames in milliseconds
      frameRate: 10,     // Number of frames per second

      transparent: false,      // True if an alpha channel should be included in the video
      alphaQuality: undefined, // Allows you to set the quality level of the alpha channel separately.
                              // If not specified this defaults to the same value as `quality`.
  });

  frames.forEach(frame=>{
    videoWriter.addFrame(frame);
  })

  console.log(await videoWriter.complete())

  return ""
}
