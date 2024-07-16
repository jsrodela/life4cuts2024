<div>
  <img class="border-2 border-neutral-800" bind:this={img} alt="" />

  <!-- <img src="/frame1.png" alt="" /> -->
  <!-- <canvas bind:this={canvas}></canvas> -->
  <button on:click={restartSection}>처음으로</button>
</div>

<script lang="ts">
  import { browser } from '$app/environment';

  import type { Session } from '$lib/stores/sessions';
  import { createNDownloadVideo } from '$lib/utils/createVideo';
  import { downloadDataUrl } from '$lib/utils/downloadImg';
  import type { Writable } from 'svelte/store';

  export let session: Writable<Session>;

  let img = null;

  const lutImgData = {
    '/frame1.png': {
      poses: [
        [194, 392],
        [194, 50],
        [619, 392],
        [619, 50],
      ],
      photoWidth: 372,
      demension: [1040, 720],
    },
    '/frame2.png': {
      poses: [
        [108, 820],
        [108, 100],
        [1050, 820],
        [1050, 100],
      ],
      photoWidth: 907,
      demension: [2400, 1600],
    },
  };

  function process() {
    if (!browser) return;

    const canvas = document.createElement('canvas');

    const imgWidth = $session.width;
    const imgHeight = $session.height;

    const [paperWidth, paperHeight] = lutImgData[$session.frame].demension;

    canvas.width = paperWidth;
    canvas.height = paperHeight;

    $session.photos
      .filter((_, i) => i < 4)
      .forEach((photo, idx) => {
        const img = document.createElement('img');
        img.src = photo;
        const place = lutImgData[$session.frame];
        canvas
          .getContext('2d')
          .drawImage(
            img,
            place.poses[idx][0],
            place.poses[idx][1],
            place.photoWidth,
            (imgHeight / imgWidth) * place.photoWidth,
          );
      });

    let frame = new Image();
    frame.src = $session.frame;

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

      img.style.height = `${(paperWidth / paperHeight) * 720}px`;
      img.style.width = `720px`;

      img.src = data;

      // img.addEventListener('load', () => {
      //   console.log('asdas');
      //   downloadDataUrl(data, `cuts-${$session.people}-${$session.id}`);

      //   createNDownloadVideo($session.record);
      // });
    };
  }

  const restartSection = () => ($session.state = 'end');

  process();
</script>
