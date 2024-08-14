<div class="flex flex-col justify-center gap-4">
  <!-- svelte-ignore a11y-media-has-caption -->
  <video
    class="h-[480px] block aspect-[4/3] bg-neutral-600 video"
    bind:this={videoSource}
  />

  <div class="flex justify-center">
    <button class="bg-neutral-300 rounded-full w-fit" on:click={capture}
      ><IcOutlineCamera class="text-8xl" /></button
    >
  </div>
  <!-- <img bind:this={photo} alt="captured" /> -->
  <!-- <button class="next" on:click={nextSection}>다음으로</button> -->
</div>

<script lang="ts">
  import { browser, dev } from '$app/environment';

  import type { Session } from '$lib/stores/sessions';
  import type { Writable } from 'svelte/store';
  import { onMount } from 'svelte';

  import IcOutlineCamera from '$lib/components/icons/IcOutlineCamera.svelte';

  export let session: Writable<Session>;

  const width = 720;
  let height = 0;

  let started = false;

  let canvas = null;
  if (browser) canvas = document.createElement('canvas');
  // let photo = null;
  let wrapper = null;
  let wrapperInner = null;
  let videoSource = null;
  let loading = false;
  const obtenerVideoCamara = async () => {
    try {
      loading = true;
      const stream = await navigator.mediaDevices.getUserMedia({
        video: true,
      });
      videoSource.srcObject = stream;
      videoSource.play();
      console.log(videoSource);
      setTimeout(() => {
        height = (videoSource.videoHeight / videoSource.videoWidth) * width;
        wrapper.style.width = `${height}px`;
        wrapper.style.height = `${width}px`;
        wrapperInner.style.width = `${width}px`;
        wrapperInner.style.height = `${height}px`;
        videoSource.style.width = `${width}px`;
        videoSource.style.height = `${height}px`;
        videoSource.style.transformOrigin = `${height / 2}px ${height / 2}px`;
        canvas.setAttribute('width', width);
        canvas.setAttribute('height', height);
        $session.width = width;
        $session.height = height;
        console.log('🚀 ~ setTimeout ~ height:', $session.height);
      }, 40);
      loading = false;
    } catch (error) {
      console.log(error);
    }
  };

  async function capture() {
    started = true;
    // this.classList.add('hidden');

    let i = 0;
    const intervalId = setInterval(
      () => {
        const context = canvas.getContext('2d');
        context.drawImage(videoSource, 0, 0, width, height);

        const data = canvas.toDataURL('image/png');
        // photo.setAttribute('src', data);

        $session.photos.push(data);

        // console.log($session.photos);

        if (i === 3) {
          clearInterval(intervalId);
          nextSection();
        }
        i++;
      },
      (dev ? 1 : 10) * 1000,
    );

    // let downloadButton = null;
    // if (browser) downloadButton = document.createElement('a');
    // navigator.mediaDevices
    //   .getUserMedia({
    //     video: true,
    //     audio: true,
    //   })
    //   .then((stream) => {
    //     // preview.srcObject = stream;
    //     downloadButton.href = stream;
    //     videoSource.captureStream =
    //       videoSource.captureStream || videoSource.mozCaptureStream;
    //     return new Promise((resolve) => (videoSource.onplaying = resolve));
    //   })
    //   .then(() => startRecording(videoSource.captureStream(), recordingTimeMS))
    //   .then((recordedChunks) => {
    //     let recordedBlob = new Blob(recordedChunks, { type: 'video/webm' });
    //     const result = URL.createObjectURL(recordedBlob);
    //     downloadButton.href = result;
    //     downloadButton.download = 'RecordedVideo.webm';
    //     downloadButton.click();

    //     console.log(
    //       `Successfully recorded ${recordedBlob.size} bytes of ${recordedBlob.type} media.`,
    //     );
    //   })
    //   .catch((error) => {
    //     if (error.name === 'NotFoundError') {
    //       console.log("Camera or microphone not found. Can't record.");
    //     } else {
    //       console.log(error);
    //     }
    //   });
  }

  const nextSection = () => ($session.section += 1);

  // function wait(delayInMS) {
  //   return new Promise((resolve) => setTimeout(resolve, delayInMS));
  // }

  // function stop(stream) {
  //   stream.getTracks().forEach((track) => track.stop());
  // }

  // function startRecording(stream: MediaStream, lengthInMS: number) {
  //   let recorder = new MediaRecorder(stream);
  //   let data = [];

  //   recorder.ondataavailable = (event) => data.push(event.data);
  //   recorder.start();
  //   console.log(`${recorder.state} for ${lengthInMS / 1000} seconds…`);

  //   let stopped = new Promise((resolve, reject) => {
  //     recorder.onstop = resolve;
  //     recorder.onerror = (event) => reject(event.name);
  //   });

  //   let recorded = wait(lengthInMS).then(() => {
  //     if (recorder.state === 'recording') {
  //       recorder.stop();
  //     }
  //   });

  //   return Promise.all([stopped, recorded]).then(() => data);
  // }

  onMount(obtenerVideoCamara);
</script>
