<div class="background">
  {#if loading}
    <h1>LOADING</h1>
  {/if}
  <!-- svelte-ignore a11y-media-has-caption -->
  <video class="video" bind:this={videoSource} />
  <button class="capture" on:click={capture}
    >CAPTURE</button
  >
  <img bind:this={photo} alt="captured" />
  <button class="next" on:click={nextSection}>다음으로</button>
</div>

<script lang="ts">
  import { browser, dev } from '$app/environment';

  import type { Session } from '$lib/stores/sessions';
  import type { Writable } from 'svelte/store';
  import { onMount } from 'svelte';

  export let session: Writable<Session>;

  const width = 720;
  let height = 0;

  let recordingTimeMS = 5000;

  let canvas = null;
  if (browser) canvas = document.createElement('canvas');
  let photo = null;
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
      }, 40);
      loading = false;
    } catch (error) {
      console.log(error);
    }
  };

  async function capture() {
    this.classList.add('hidden');

    let i = 0;
    const intervalId = setInterval(
      () => {
        const context = canvas.getContext('2d');
        context.drawImage(videoSource, 0, 0, width, height);

        const data = canvas.toDataURL('image/png');
        photo.setAttribute('src', data);

        $session.photos.push(data);

        console.log($session.photos);

        if (i === 3) clearInterval(intervalId);
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

<style>
  .background {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
    font-family: 'Noto Sans', Arial, sans-serif;
    padding: 0;
    width: 100vw;
  }
  .video {
    transform: rotateY(180deg);
    size: 100%;
  }
  .capture {
    width: 200px;
    height: 60px;
    border: none;
    background-color: #ffffff;
    color: rgb(15, 15, 15);
    font-size: 1.5em;
    cursor: pointer;
    border-radius: 10px;
    margin-top: 40px;
    font-weight: 900;
  }

  .next { 
    width: 140px;
    height: 50px;
    border: none;
    background-color: #ffffff;
    color: rgb(15, 15, 15);
    font-size: 1.5em;
    cursor: pointer;
    border-radius: 10px;
    margin-top: 40px;
    font-weight: 900;
  }
</style>