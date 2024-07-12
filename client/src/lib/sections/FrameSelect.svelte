<div class="w-full">
  <h2 class="text-5xl text-center mb-10">프레임을 선택해 주세요</h2>

  <div class="flex w-full justify-evenly">
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
