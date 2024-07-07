{#if $session.section === 0}
  <Start {session} />
{:else if $session.section === 1}
  <FrameSelect {session} />
{:else if $session.section === 2}
  <Cam {session} />
{:else if $session.section === 3}
  <Edit {session} />
{/if}

<script>
  import Cam from '$lib/sections/Cam.svelte';
  import Start from '$lib/sections/Start.svelte';
  import Edit from '$lib/sections/Result.svelte';
  import FrameSelect from '$lib/sections/FrameSelect.svelte';

  import { newSession } from '$lib/stores/sessions';

  import { dev, browser } from '$app/environment';

  let session = newSession();

  $: if ($session.end) session = newSession();

  if (dev && browser) {
    window.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight') $session.section += 1;
      if (e.key === 'ArrowLeft') $session.section -= 1;
    });
  }
</script>
