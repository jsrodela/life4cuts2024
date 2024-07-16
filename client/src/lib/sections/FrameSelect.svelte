<div class="flex flex-col justify-center items-center gap-12">
  <h1
    class="text-6xl font-bold font-ridi-serif drop-shadow-[4px_4px_1px_rgba(0,0,0,0.3)]"
  >
    프레임을 선택해 주세요
  </h1>

  <div class="flex gap-32">
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
