<div class="w-full">
  <h2 class="text">프레임을 선택해 주세요</h2>

  <div class="flex">
    <button on:click={handleFrameSelection} data-id="/frame1.png">
      <img
        src="/frame1-preview.webp"
        alt=""
        class="w-96 border-2 border-neutral-800"
      />
    </button>
    <button on:click={handleFrameSelection} data-id="/frame2.png">
      <img
        src="/frame2-preview.webp"
        alt=""
        class="w-96 border-2 border-neutral-800"
      />
    </button>
  </div>
</div>

<script lang="ts">
  import type { Session } from '$lib/stores/sessions';
  import type { Writable } from 'svelte/store';

  export let session: Writable<Session>;

  function handleFrameSelection(e: MouseEvent) {
    const result = e.currentTarget.getAttribute('data-id');

    $session.frame = result;

    $session.section += 1;
  }
</script>

<style>
  .w-full {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
    font-family: 'Noto Sans', Arial, sans-serif;
    padding: 0;
    width: 100vw;
  }
  .flex {
    float: center;
  }
  button {
    padding-left: 50px;
    padding-right: 50px;
  }
  .text {
    font-size: xx-large;
    font-weight: bolder;
    font-family: 'Noto Sans', Arial, sans-serif;
  }

</style>