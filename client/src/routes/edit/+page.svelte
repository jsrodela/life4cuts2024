<img bind:this={img} alt="" />
<!-- <img src="/frame1.png" alt="" /> -->
<!-- <canvas bind:this={canvas}></canvas> -->
<button on:click={process}>작업</button>

<script>
  import { session } from '$lib/stores/sessions';
  import { browser } from '$app/environment';

  let img = null;

  function process() {
    if (!browser) return;

    const canvas = document.createElement('canvas');

    const imgWidth = $session.width;
    const imgHeight = $session.height;

    canvas.width = 1040;
    canvas.height = 720;

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

    const frame = new Image();
    frame.src = '/frame1.png';

    frame.onload = () => {
      canvas.getContext('2d').drawImage(frame, 0, 0, 1040, 720);
      const data = canvas.toDataURL();

      img.src = data;
    };
  }
</script>
