{#if $session.section === 0}
  <Start {session} />
{:else if $session.section === 1}
  <Cam {session} />
{:else if $session.section === 2}
  <Edit {session} />
{/if}

<script>
  import Cam from '$lib/sections/Cam.svelte';
  import Start from '$lib/sections/Start.svelte';
  import Edit from '$lib/sections/Result.svelte';

  import { newSession } from '$lib/stores/sessions';

  const session = newSession();
</script>
