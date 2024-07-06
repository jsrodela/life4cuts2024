<div>
  {#if loading}
    <h1>LOADING</h1>
  {/if}
  <!-- svelte-ignore a11y-media-has-caption -->
  <div bind:this={wrapper} class="block">
    <div bind:this={wrapperInner} class="block">
      <video class="rotate-90 block" bind:this={videoSource} />
    </div>
  </div>
  <button class="border-stone-800 border-2 p-1 rounded-sm" on:click={capture}
    >CAPTURE</button
  >
  <img bind:this={photo} alt="captured" />
  <p>
    {$session.people} 명
  </p>
  <button on:click={nextSection}>다음으로</button>
</div>

<script lang="ts">
  import { browser } from '$app/environment';
  import { goto } from '$app/navigation';
  import { session } from '$lib/stores/sessions';

  const width = 720;
  let height = 0;

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
        session.update((s) => {
          s.width = width;
          s.height = height;
          return s;
        });
      }, 40);
      loading = false;
    } catch (error) {
      console.log(error);
    }
  };

  async function capture() {
    const context = canvas.getContext('2d');
    context.drawImage(videoSource, 0, 0, width, height);

    const data = canvas.toDataURL('image/png');
    photo.setAttribute('src', data);

    session.update((s) => {
      s.photos.push(data);
      return s;
    });

    console.log($session);
  }

  function nextSection() {
    goto('/edit');
  }

  obtenerVideoCamara();
</script>
