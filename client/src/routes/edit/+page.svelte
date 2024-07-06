<img alt="" />
<canvas bind:this={canvas}></canvas>
<button on:click={process}>작업</button>

<script>
  import { session } from '$lib/stores/sessions';
  import { browser } from '$app/environment';

  let canvas = null;

  function process() {
    if (!browser) return;

    // const canvas = document.createElement('canvas');

    const imgWidth = $session.width;
    const imgHeight = $session.width;

    canvas.width = imgWidth * 3;
    canvas.height = imgHeight * 2;

    const lutImgPos = [
      [0, 0],
      [imgWidth, 0],
      [imgWidth * 2, 0],
      [0, imgHeight],
      [imgWidth, imgHeight],
      [imgWidth * 2, imgHeight],
    ];

    $session.photos.forEach((photo, idx) => {
      const img = document.createElement('img');
      img.src = photo;
      canvas
        .getContext('2d')
        .drawImage(
          img,
          lutImgPos[idx][0],
          lutImgPos[idx][1],
          imgWidth,
          imgHeight,
        );
    });
  }
</script>
