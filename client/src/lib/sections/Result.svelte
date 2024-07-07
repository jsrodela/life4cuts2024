<img bind:this={img} alt="" />

<!-- <img src="/frame1.png" alt="" /> -->
<!-- <canvas bind:this={canvas}></canvas> -->
<button on:click={restartSection}>처음으로</button>

<script lang="ts">
  import { browser } from '$app/environment';

  import type { Session } from '$lib/stores/sessions';
  import type { Writable } from 'svelte/store';

  export let session: Writable<Session>;

  let img = null;

  function process() {
    if (!browser) return;

    const canvas = document.createElement('canvas');

    const imgWidth = $session.width;
    const imgHeight = $session.height;

    const paperWidth = 1040;
    const paperHeight = 720;

    canvas.width = paperWidth;
    canvas.height = paperHeight;

    const lutImgPos = [
      [194, 392],
      [194, 50],
      [619, 392],
      [619, 50],
    ];

    console.log(lutImgPos);

    $session.photos
      .filter((_, i) => i < 4)
      .forEach((photo, idx) => {
        const img = document.createElement('img');
        img.src = photo;
        canvas
          .getContext('2d')
          .drawImage(
            img,
            lutImgPos[idx][0],
            lutImgPos[idx][1],
            372,
            (imgHeight / imgWidth) * 372,
          );
      });

    let frame = new Image();
    frame.src = '/frame1.png';

    frame.onload = () => {
      canvas.getContext('2d').drawImage(frame, 0, 0, paperWidth, paperHeight);

      const rotatedImg = document.createElement('canvas');

      rotatedImg.width = paperHeight;
      rotatedImg.height = paperWidth;

      const rotatedCtx = rotatedImg.getContext('2d');

      rotatedCtx.save();
      rotatedCtx.translate(paperHeight / 2, paperWidth / 2);
      rotatedCtx.rotate(Math.PI / 2);
      rotatedCtx.drawImage(canvas, -paperWidth / 2, -paperHeight / 2);
      rotatedCtx.restore();

      const data = rotatedImg.toDataURL();

      img.src = data;
    };
  }

  const restartSection = () => ($session.section = 0);

  process();
</script>
